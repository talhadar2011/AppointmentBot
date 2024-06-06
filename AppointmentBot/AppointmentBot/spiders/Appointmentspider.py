import scrapy
import playsound


class AppointmentspiderSpider(scrapy.Spider):
    name = "Appointmentspider"
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://localhost:3000']

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