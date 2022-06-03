from email import message
from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification._notify(
        title = "take rest",
        message="rest is the main thing to stay healthy",
        app_icon= "/Users/nirgunsubedi/Desktop/python/python/final/logo.png",
        timeout = 5)
    time.sleep(10)
    