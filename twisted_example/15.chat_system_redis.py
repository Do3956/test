# coding:utf-8
from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor, task, defer
import struct
import json
from twisted.python import log
import sys
import time
import txredisapi as redis
log.startLogging(sys.stdout)

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 4
# REDIS_PASSWORD = 'dahai123'

redis_store = redis.lazyConnectionPool(dbid=4, host='localhost', port=REDIS_PORT)
#
#
@defer.inlineCallbacks
def check_token(phone_number, token):
    token_in_redis = yield redis_store.hget('user:%s' % phone_number, 'token')
    if token != token_in_redis:
        defer.returnValue(False)
    else:
        defer.returnValue(True)


class Chat(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.phone_number = None
        self.state = "VERIFY"
        self.version = 0
        self.last_heartbeat_time = 0
        self.command_func_dict = {
            1: self.handle_verify,
            2: self.handle_single_chat,
            3: self.handle_group_chat,
            4: self.handle_broadcast_chat,
            5: self.handle_heartbeat
        }
        self._data_buffer = bytes()

    def connectionMade(self):
        log.msg("New connection, the info is:", self.transport.getPeer())

    def connectionLost(self, reason):
        log.msg("[%s]:断线" % self.phone_number.encode('utf-8'))
        if self.phone_number in self.factory.users:
            del self.factory.users[self.phone_number]

    def dataReceived(self, data):
        """
        接受到数据以后的操作
        """
        self._data_buffer += data

        while True:
            length, self.version, command_id = struct.unpack('!3I', self._data_buffer[:12])

            if length > len(self._data_buffer):
                return

            content = self._data_buffer[12:length]

            if command_id not in [1, 2, 3, 4, 5]:
                return

            if self.state == "VERIFY" and command_id == 1:
                self.handle_verify(content)

            if self.state == "DATA":
                self.handle_data(command_id, content)

            self._data_buffer = self._data_buffer[length:]

            if len(self._data_buffer) < 12:
                return

    def handle_heartbeat(self, content):
        """
        处理心跳包
        """
        self.last_heartbeat_time = int(time.time())

    @defer.inlineCallbacks
    def handle_verify(self, content):
        """
        验证函数
        """
        content = json.loads(content)
        phone_number = content.get('phone_number')
        token = content.get('token')

        # result = True
        result = yield check_token(phone_number, token)

        if not result:
            send_content = json.dumps({'code': 0})
            self.send_content(send_content, 101, [phone_number])
            length = 12 + len(send_content)
            version = self.version
            command_id = 101
            header = [length, version, command_id]
            header_pack = struct.pack('!3I', *header)
            self.transport.write(header_pack + send_content)
            return

        if phone_number in self.factory.users:
            log.msg("电话号码<%s>存在老的连接." % phone_number.encode('utf-8'))
            self.factory.users[phone_number].connectionLost("")
            self.factory.users.pop(phone_number)

        log.msg("欢迎, %s!" % (phone_number.encode('utf-8'),))
        self.phone_number = phone_number
        self.factory.users[phone_number] = self
        self.state = "DATA"

        send_content = json.dumps({'code': 1})

        self.send_content(send_content, 101, [phone_number])

    def handle_data(self, command_id, content):
        """
        根据command_id来分配函数
        """
        self.command_func_dict[command_id](content)

    def handle_single_chat(self, content):
        """
        单播
        """
        content = json.loads(content)
        chat_from = content.get('chat_from')
        chat_to = content.get('chat_to')
        chat_content = content.get('chat_content')
        send_content = json.dumps(dict(chat_from=chat_from, chat_content=chat_content))

        self.send_content(send_content, 102, [chat_to])

    def handle_group_chat(self, content):
        """
        组播
        """
        content = json.loads(content)
        chat_from = content.get('chat_from')
        chat_to = content.get('chat_to')
        chat_content = content.get('chat_content')
        send_content = json.dumps(dict(chat_from=chat_from, chat_content=chat_content))

        phone_numbers = chat_to
        self.send_content(send_content, 103, phone_numbers)

    def handle_broadcast_chat(self, content):
        """
        广播
        """
        content = json.loads(content)
        chat_from = content.get('chat_from')
        chat_content = content.get('chat_content')
        send_content = json.dumps(dict(chat_from=chat_from, chat_content=chat_content))

        phone_numbers = self.factory.users.keys()
        self.send_content(send_content, 104, phone_numbers)

    def send_content(self, send_content, command_id, phone_numbers):
        """
        发送函数
        """
        length = 12 + len(send_content)
        version = self.version
        command_id = command_id
        header = [length, version, command_id]
        header_pack = struct.pack('!3I', *header)
        for phone_number in phone_numbers:
            if phone_number in self.factory.users.keys():
                self.factory.users[phone_number].transport.write(header_pack + send_content)
            else:
                log.msg("Phone_number:%s 不在线." % phone_number.encode('utf-8'))


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return Chat(self)

    def check_users_online(self):
        for key, value in self.users.items():
            if value.last_heartbeat_time != 0 and int(time.time()) - value.last_heartbeat_time > 4:
                log.msg("[%s]没有检测到心跳包,主动切断" % key.encode('utf-8'))
                value.transport.abortConnection()

cf = ChatFactory()

task1 = task.LoopingCall(cf.check_users_online)
task1.start(3, now=False)

reactor.listenTCP(8124, cf)
reactor.run()