import time

COUNT = 100
test = {
    i: i for i in range(COUNT)
}
s = time.time()
for k in tuple(test.keys()):
    del test[k]
print('tuple del : %s' % (time.time() - s))

test = {
    i: i for i in range(COUNT)
}
s = time.time()
for k in list(test.keys()):
    del test[k]
print('list del  : %s' % (time.time() - s))

test = {
    i: i for i in range(COUNT)
}
s = time.time()
for k in tuple(test.keys()):
    test.pop(k)
print('tuple pop : %s' % (time.time() - s))

test = {
    i: i for i in range(COUNT)
}
s = time.time()
for k in list(test.keys()):
    test.pop(k)
print('list pop  : %s' % (time.time() - s))
