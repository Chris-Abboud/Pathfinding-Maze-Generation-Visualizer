import sys
import threading

class SomeCallable:
    def __call__(self):
        try:
            self.recurse(99900)
        except RecursionError:
            print("Booh!")
        else:
            print("Hurray!")
    def recurse(self, n):
        if n > 0:
            self.recurse(n-1)

SomeCallable()() # recurse in current thread

# recurse in greedy thread
sys.setrecursionlimit(5000000)
threading.stack_size(1154432)
t = threading.Thread(target=SomeCallable())
t.start()
t.join()