import scrapy
import playsound
import random
from fake_useragent import UserAgent


class AppointmentspiderSpider(scrapy.Spider):
    name = "Appointmentspider"
    start_urls = ['http://localhost:3000']
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edge/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"
]
    def start_requests(self):
        print("//////Start_request Running//////")
        # Create a UserAgent object
        ua = UserAgent()

        # Generate a random user agent
        random_user_agent = ua.random
        print(random_user_agent)
        for url in self.start_urls:
            print(self.user_agents[random.randint(0,len(self.user_agents)-1)],
                  "userAgents//////////////////////")
            yield scrapy.Request(url, headers={"useragent":self.user_agents[random.randint(0,len(self.user_agents)-1)]})

    
    
    def parse(self, response):
           # Set headers for a specific request
        Page = response.css('.wrapper')
        NumberOfLinks = len(Page.css('.arrow').extract())
        CompairString = "study visa"
        StringArray = Page.css('div::text').extract()
        alarm_sound = 'C:\\Users\\tdar\\Desktop\\alarm.wav'  
        String_check = False
        for string in StringArray:
            if CompairString in string:
                print(f"Match found in: {string}")
                String_check = True
                
        
        if NumberOfLinks==7 and String_check==True:
            # Play the alarm sound
            playsound.playsound(alarm_sound)
            print("Alarm triggered! Condition met.")
        else:
            print("Number of link not equal to 7 and String test is",String_check)         