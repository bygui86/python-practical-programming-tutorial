
import time

try:
    print("Waiting for keyboard interrupt...")
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("Interrupt!!")
