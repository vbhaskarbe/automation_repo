class MyProgram(object):
    def __init__(self):
        pass #you should only set variables,
             #not anything error prone here
    def run(self):
        pass #main program logic
    def cleanup(self):
        pass #your cleanup code here
 
if __name__=="__main__":
    try:
        prog=MyProgram()
        prog.run()
    finally:
        prog.cleanup()


