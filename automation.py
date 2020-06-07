from datetime import datetime
from message import sendMessage
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sendMessage, 'interval', seconds=5)

sched.start()