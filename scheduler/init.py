import logging
from time import sleep
from apscheduler.schedulers.background import BlockingScheduler
from helpers.website_crawler import initiateTask

logging.basicConfig()
logging.getLogger("apscheduler").setLevel(logging.DEBUG)

def display():
    print("It has been triggered")


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(initiateTask, "cron", day_of_week="mon-fri", hour="10,17", minute="0-59/10")
    scheduler.start()

if __name__=="__main__": 
    main() 

