import threading

class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.sleep_event = threading.Event()
        

    def run(self):
        while True:
            self.sleep_event.clear()
            self.sleep_event.wait(60)
            threading.Thread(target=self._run).start()

    def _run(self):
        print('run')

if __name__ == "__main__":
    
    my_thread = MyThread()
    my_thread.start()

