import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, arg):
        list.append(self, arg)
        self.log(arg)

a = LoggableList()

a.append('test1')
print(a)
a.append(2)
print(a)
a.append([1, 2, 3])
print(a)
a.append({1: 's'})
print(a)