import time


class FileWatcher:
    def __init__(self, path_of_file_to_watch):
        self.path = path_of_file_to_watch
        self.subscribers = dict()

    def register(self, subscriber, callback):
        self.subscribers[subscriber] = callback

    def unregister(self, subscriber):
        del self.subscribers[subscriber]

    def notify(self, message):
        for callback in self.subscribers.values():
            callback(message)

class FileObserver:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{} noticed that the file is now {} bytes".format(self.name, message))

john = FileObserver('John')
stacy = FileObserver('Stacy')
bob = FileObserver('Bob')

filewatcher = FileWatcher('/')
filewatcher.register(john, john.update)
filewatcher.register(stacy, stacy.update)
filewatcher.register(bob, bob.update)
for i in range(10):
    time.sleep(5)
    filewatcher.notify("5")



