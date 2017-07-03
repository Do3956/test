# -*- coding: utf-8 -*-
"""
__author__ = 'admin'
__mtime__ = '2017/7/3'
__content__ = ''
"""

def poetry_main():
    addresses = parse_args()

    xform_addr = addresses.pop(0)

    proxy = TransformProxy(*xform_addr)

    from twisted.internet import reactor

    results = []

    @defer.inlineCallbacks
    def get_transformed_poem(host, port):
        try:
            poem = yield get_poetry(host, port)
        except Exception, e:
            print >>sys.stderr, 'The poem download failed:', e
            raise

        try:
            poem = yield proxy.xform('cummingsify', poem)
        except Exception:
            print >>sys.stderr, 'Cummingsify failed!'

        defer.returnValue(poem)

    def got_poem(poem):
        print poem

    def poem_done(_):
        results.append(_)
        if len(results) == len(addresses):
            reactor.stop()

    for address in addresses:
        host, port = address
        d = get_transformed_poem(host, port)
        d.addCallbacks(got_poem)
        d.addBoth(poem_done)

    reactor.run()
