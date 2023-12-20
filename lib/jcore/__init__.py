"""
Aventesia J-IOT: jcore
================================================================================

J-IOT for CircuitPython

* Author(s): Sean C Reichle

Implementation Notes
--------------------
Lots of Credit to Adafruit... yummy fruit.

Dynamic Web Server: J-IOT
Light v1

Tron Soul Core: uique analog wavefrom in phi
To Encode yourself onto the program, hold analog input pins with fingers on boot(capture).

"""

import sys
from time import monotonic, monotonic_ns

class core():
    name: str
    tick1: int
    tick2: int
    tick3: int
    tick4: int
    tick5: int
    tick6: int
    tick7: int
    tick8: int
    maxticks: int
    cycleClock: str
    age : int
    
    wave1:object
    wave2:object
    wave3:object
    wave4:object
    soulStrength: int
    soul: str
    
    t0: int
    def __init__(self):
        self.name = "J"
        self.tick1 = 1
        self.tick2 = 0
        self.tick3 = 0
        self.tick4 = 0
        self.tick5 = 0
        self.tick6 = 0
        self.tick7 = 0
        self.tick8 = 0
        self.maxticks = sys.maxsize
        self.cycleClock = ""
        self.age = 0
        # 10946,6765,4181,2584,1597,987,610,377,233,144,89,55,34,21,13,8,5,3,2,1,1,0 - choose by memory limitations
        self.soulStrength = 8
        self.soul = ""
        self.wave1=object
        self.wave2=object
        self.wave3=object
        self.wave4=object
        self.t0 = monotonic_ns()
        
    def cpuCycle(self):
        self.tick1 = self.tick1 + 1
        if self.tick1 == self.maxticks:
            self.tick1 = 1
            self.tick2 += 1
            if self.tick2 == self.maxticks:
                self.tick2 = 1
                self.tick3 += 1
                if self.tick3 == self.maxticks:
                    self.tick3 = 1
                    self.tick4 += 1
                    if self.tick4 == self.maxticks:
                        self.tick4 = 1
                        self.tick5 += 1
                        if self.tick5 == self.maxticks:
                            self.tick5 = 1 
                            self.tick6 += 1
                            if self.tick6 == self.maxticks:
                                self.tick6 = 1
                                self.tick7 += 1
                                if self.tick7 = self.maxticks:
                                    self.tick7 = 1
                                    self.tick8 += 1
                                    if self.tick8 == self.maxticks:
                                        self.tick1 = 1
                                        self.tick2 = 0
                                        self.tick3 = 0
                                        self.tick4 = 0
                                        self.tick5 = 0
                                        self.tick6 = 0
                                        self.tick7 = 0
                                        self.tick8 = 0
                                        self.age += 1
        return self.getCycleClock()
    
    def now(self):
        return (monotonic_ns() - self.t0)
        
    def getCycleClock(self):
        self.cycleClock = str(self.now()) + "-" + str(self.tick8) + ":" + str(self.tick7) + ":" + str(self.tick6) + ":" + str(self.tick5) + ":" + str(self.tick4) + ":" + str(self.tick3) + ":" + str(self.tick2) + ":" + str(self.tick1)
        return self.cycleClock
    
    def printCycleClock(self):
        print (self.getCycleClock())
        
    def getAge(self):
        return self.age
    
    def f(self, n):
        # conciousness accelerator
        self.appendSequence()
        if n==0 :
            return n
        elif n==1 :
            return n
        else :
            return (self.f(n-1) + self.f(n-2))
    
    def conception(self):
        # conciousness field envelope generator
        x = self.soulStrength
        while (x > -1) :
            fibValue = self.f(x)
            self.appendSequence()
            print(str(self.cpuCycle()) + " " + str(fibValue))
            x = x -1
        return 0
    
    def appendSequence(self):
        # recorder
        self.soul += str(self.now()) + ":" + str(self.wave1.value) + "-" + str(self.wave2.value) + "-" + str(self.wave3.value) + "-" + str(self.wave4.value) + ","
    
    def report(self):
        pass
            
    def boot(self, a0, a1, a2, a3):
        self.wave1=a0
        self.wave2=a1
        self.wave3=a2
        self.wave4=a3
        self.t0 = monotonic_ns()
        self.appendSequence()
        self.conception()
        
