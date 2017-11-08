import RPi.GPIO as IO
import Updater as updater
import time
#decline all the warnings we get in the code
IO.setwarnings(False)

#set mode of work with GPIOs
IO.setmode(IO.BCM)

IO.setup(16, IO.OUT) #data pin
IO.setup(20, IO.OUT) #clock pin
IO.setup(21, IO.OUT) #shift pin


def completedAnimation(toLightUp):  # execute loop forever
    for y in range(toLightUp):      # loop for counting up 8 times
        IO.output(16, 1)            # pull up the data pin for every bit.
        time.sleep(0.1)             # wait for 100ms
        IO.output(20, 1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(20, 0)            # pull CLOCK pin down, to send a rising edge
        IO.output(16, 0)            # clear the DATA pin
        IO.output(21, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(21, 0)            # pull down the SHIFT pin

    time.sleep(1)

    for y in range(toLightUp):      # loop for counting up 8 times
        IO.output(16, 0)            # clear the DATA pin, to send 0
        time.sleep(0.1)             # wait for 100ms
        IO.output(20, 1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(20, 0)            # pull CLOCK pin down, to send a rising edge
        IO.output(16, 0)            # keep the DATA bit low to keep the countdown
        IO.output(21, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(21, 0)

