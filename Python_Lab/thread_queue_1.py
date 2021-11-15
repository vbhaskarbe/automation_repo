from queue import Queue
from threading import Thread
def stringFunction(value, out_queue):
    my_str = "This is string no. " + value
    out_queue.put(my_str)
my_queue = Queue.Queue()
thread1 = threading.Thread(stringFunction("one", my_queue))
thread1.start()
thread1.join()
func_value = my_queue.get()
print(func_value)


