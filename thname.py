import threading

def test():
    print("test")
    print(threading.current_thread().name) # Here
                                                              
t = threading.Thread(target=test, name="test_thread")
t.start() 
