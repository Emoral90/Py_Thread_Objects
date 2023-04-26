# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# Initializing and running a threaded class
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import threading
import time

# Basic class creating a thread object
class Hello(threading.Thread):
    def __init__(self, num, mes):
        # call parent class constructor
        super().__init__()

        # Create and assign variables
        self.num = num
        self.mes = mes

    # INCLUDE THIS METHOD run(self) ALWAYS
    def run(self):
        time.sleep(self.num)
        print(f"Message: {self.mes}")


# Class creating a thread object that returns a value
class Adder(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        # Create a variable to save the results
        # Since its public by default it can be used in the main function
        self.results = self.number + 3


if __name__ == "__main__":
    hello1 = Hello(1, "Hello from thread 1")
    hello2 = Hello(2, "Hello from thread 2")

    hello1.start()
    hello2.start()

    hello1.join()
    hello2.join()

    print(f"="*20)

    add1 = Adder(100)
    add2 = Adder(200)

    add1.start()
    add2.start()

    add1.join()
    add2.join()

    print(f"Adder(100) returns {add1.results}")
    print(f"Adder(200) returns {add2.results}")