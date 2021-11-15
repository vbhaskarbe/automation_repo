import queue
import threading

# creating queue instance
q = queue.Queue()

# creating threading class
class AnyThread():
    def __init__ (self):
        threading.Thread.__init__(self)

    def run(self,i):
        # in this class and function we will put our test target function
        test(i)

t = AnyThread()

# having our test target function
def test(i):
    # do something in this function:
    result = i + 3 + 2
    # and put result to a queue instance
    q.put(result)

for i in range(10): #calling our threading fucntion 3 times (just for example)
    t.run(i)
    output = q.get() # here we get output from queue instance
    print(output)



