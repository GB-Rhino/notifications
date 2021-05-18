from pynotifier import Notification
import schedule
import time


def lmao():  ##function for the notification##
    Notification(
        title='test',
        description='test',
        duration=5,  # Duration in seconds
        urgency='normal'
    ).send()


##def job():
##print("I am working")

if __name__ == "__main__":
    schedule.every(10).seconds.do(lmao)
##Requires function to be passed after do##

while True:
    schedule.run_pending()
    time.sleep(1)

##actually runs the script constant, while loop, sleeps program to prevent loop from imploding, schedule.run_pending runs given script##
