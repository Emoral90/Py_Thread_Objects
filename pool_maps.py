import os
import time
import multiprocessing as mp

def func(name):
    time.sleep(0.5)
    print(f'{name}, {os.getpid()}') # Method to return the current process id

if __name__ == '__main__':

    names = ['Erick', 'Chase', 'Jordan', 'Camden', 'Korbin']

    # Create a pool of 2 processes
    with mp.Pool(2) as p:
        # map those 2 process to the function func()
        # Python will call the function func() alternating items in the names list.
        # the two processes will run in parallel
        p.map(func, names) 
        # Method to returns an itertor that applies some function (such as func()) to every item in the iterable (such as arrays, lists, dictionaries, etc)
