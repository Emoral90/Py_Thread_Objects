'''
Multiprocessing offers both local and remote concurrency to avoid the GIL by using subprocesses instead of threads. Thus, taking advantage of multiple processors now available on machines

This module also introduces the Pool object in order to parallelize the execution of a function across multiple input values
'''

import multiprocessing as mp
import threading as th

# 1) Adding processes to the program is the same as creating, starting, and joining threads

# 2) declare a global variable outside the function with one value and inside with another
global_var = 0

def func(name):
    global global_var
    global_var = 123
    print(f"Hello {name}: {global_var}")

if __name__ == "__main__":
    # 2) verify how the value of global_var has changed before and after Process
    print(f"Before process global_var = {global_var}")
    # 1) Same procedure as starting and joining as threads
    p = mp.Process(target=func, args=("Erick",))
    p.start()
    p.join()
    print(f"After process global_var = {global_var}\n\n")

    print(f"Before thread global_var = {global_var}")
    t = th.Thread(target=func, args=("Chase",))
    t.start()
    t.join()
    print(f"Before thread global_var = {global_var}")

# 2) To change the value of a global variable, you can call a function that uses that variable declared as global. Called first from a process then a thread