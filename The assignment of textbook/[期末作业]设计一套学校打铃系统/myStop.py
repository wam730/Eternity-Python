import threading
import time
import inspect
import ctypes
 
 
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
 
 
def print_time(e):
    while 2:
        print(e)
        
        
def in_club():
    t = threading.Thread(target=print_time,args=("2"))
    t.start()
    time.sleep(0.001)
        
def start_():
    stop_thread(t)

        
class AAA(): 
    def in_club(self):
        self.t = threading.Thread(target=print_time,args=("2"))
        self.t.start()
        time.sleep(0.001)
        
    def start_(self):
        stop_thread(self.t)
 
 
if __name__ == "__main__":
    # t = threading.Thread(target=print_time,args=("2"))
    # t.start()
    # time.sleep(0.001)
    # stop_thread(t)
    # print("stoped")
    # time.sleep(2)
    # t1 = threading.Thread(target=print_time,args=("1"))
    # t1.start()
    # time.sleep(0.001)
    # stop_thread(t1)
    # print("stoped")
    
    # start_main = AAA()
    # start_main.in_club()
    # start_main.start_()
    in_club()
    start_()

    while 1:
        pass
