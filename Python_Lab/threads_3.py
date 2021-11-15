# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
 
def print_cube(num,count):
    """
    function to print cube of given num
    """
    while count > 0:
        print("Cube: {}".format(num * num * num));
        count = count - 1;

def print_square(num,count):
    """
    function to print square of given num
    """
    while count > 0:
        print("Square: {}".format(num * num));
        count = count - 1;

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,10))
    t2 = threading.Thread(target=print_cube, args=(10,10))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("Done!")

