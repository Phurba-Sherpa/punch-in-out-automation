from crontab import CronTab


def main():
    jobScheduler = CronTab(user='phurba')
    # creating a new cron job with the scheduler
    job = jobScheduler.new(command='python  /Users/phurb/OneDrive/Desktop/punch-in-out-automation/scheduler/index.py')
    # schedule the job
    job.minute.every(1)
    jobScheduler.write()    

if __name__=="__main__": 
    main() 