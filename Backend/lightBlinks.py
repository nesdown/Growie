import time

def errorCode():
    print("RED LED BLINKS")
    time.sleep(1)
    print("NO BLINKS")
    time.sleep(1)
    print("RED LED BLINKS")
    time.sleep(1)
    print("NO BLINKS")
    time.sleep(1)
    print("RED LED BLINKS")

def newMilestone(progress):
    for i in range(progress+1):

        print(" * " * i)
        time.sleep(1)
        print("NO BLINKS")

def endProject():
    for i in range(3):
        print("PROJECT COLOR LEDS")
        time.sleep(2)
        print("NO BLINKS")
        time.sleep(0.5)