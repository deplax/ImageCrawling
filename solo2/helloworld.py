__author__ = 'Administrator'

hello = "hello World"
print hello


def hap(x, y):
    return x + y


print hap(10, 20)
print (lambda x, y: x + y)(10, 20)

print 'range', range(5)
print 'range', range(0, 100, 10)

print map(lambda x: x ** 2, range(5))
print reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
print reduce(lambda x, y: x + y, range(5))
print reduce(lambda x, y: y + x, 'abcde')
print filter(lambda x: x % 2, range(10))

print type('A')

x = 'banana'
print x[1:]
prime = [2, 3, 7, 11]
prime.append(5)

