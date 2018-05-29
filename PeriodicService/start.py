import time
from threading import Thread
from periodic_service import trigger_call, configuration

config = configuration()
print("starting the Periodic service that runs every {}secs".format(config['interval']))
# Preferred to use crontab in production
while True:
   Thread(target=trigger_call).start()
   time.sleep(config['interval'])
