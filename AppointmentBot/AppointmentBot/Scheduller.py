import schedule
import time
from scrapy.crawler import CrawlerProcess
from spiders.Appointmentspider import AppointmentspiderSpider
import schedule
import time
import subprocess
import sys
import os

def run_spider():
    subprocess.run([sys.executable, "-m", "scrapy", "crawl", "Appointmentspider"], cwd=os.path.dirname(__file__))

schedule.every(30).seconds.do(run_spider)

while True:
    schedule.run_pending()
    time.sleep(1)