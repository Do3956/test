#coding:utf-8

class Node:
    def __init__(self):
        self.children = None

class Dfa:
    def __init__(self, words):
        self.root = Node()
        self.init(words)

    def init(self, words):
        for w in words:
            node = self.root
            for i in range(len(w)):
                if node.children is None:
                    node.children = {}
                    node.children[w[i]] = Node()
                elif w[i] not in node.children:
                    node.children[w[i]] = Node()

                node = node.children[w[i]]

    def is_contain(self, message):
        msg_len = len(message)
        for i in range(msg_len):
            p = self.root
            j = i
            while (j < msg_len) and p.children != None and message[j] in p.children:
                p = p.children[message[j]]
                j += 1

            if p.children is None:
                return message[i : j]

        return ""

    def print_tree(self):
        
        def pr(n):
            if n.children != None:
                print n.children.keys()
                for k in n.children.keys():
                    pr(n.children[k])

        pr(self.root)

if __name__ == "__main__":
    words = [u"习近平", u"王八糕子"]

    d = Dfa(words)
    print d.print_tree()
    print d.is_contain("王八蛋习近平sssss".decode("utf-8"))