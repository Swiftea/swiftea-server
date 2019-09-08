import threading


class Semaphore:
    def __init__(self):
        self.counter = 1
        self.mutex = threading.Lock()
        self.condition = threading.Condition(self.mutex)

    def P(self):
        msg = ''
        with self.mutex:
            self.counter -= 1
            if self.counter < 0:
                msg += 'wait\n'
                print('wait')
                self.condition.wait()
            msg += 'go\n'
            print('go')
        return msg

    def V(self):
        msg = ''
        with self.mutex:
            self.counter += 1
            if self.counter <= 0:
                self.condition.notify()
                msg += 'notify\n'
                print('notify')
            msg += 'leave\n'
            print('leave')
        return msg
