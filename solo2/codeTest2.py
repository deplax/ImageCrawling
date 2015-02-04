# -*- coding: utf-8 -*-
__author__ = 'Administrator'

class Service:
    sercet = "kuku?"
    def setname(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s, %s + %s = %s" % (self.name, a, b, result))



pay = Service()
pay.setname("dodo")

pay.sum(1, 1)
pay.setname('kuku')
pay.sum(1, 2)
print pay.name

print type(u'파이썬')