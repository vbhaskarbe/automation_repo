import sys
import pprint
getframe_expr = 'sys._getframe({}).f_code.co_name'

def foo():
    print( "I am foo, calling bar:")
    bar()

def bar():
    print( "I am bar, calling baz:")
    baz()

def baz():
    print( "I am baz:")
    #pprint.pprint(dir(getframe_expr))
    pprint.pprint(dir(sys))    #._getframe({})))
    caller = eval(getframe_expr.format(2))
    callers_caller = eval(getframe_expr.format(3))
    print( "I was called from", caller)
    print( caller, "was called from", callers_caller)

foo()



