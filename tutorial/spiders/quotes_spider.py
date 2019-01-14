import scrapy
import csv
import re
import struct
from selenium import webdriver

#Pour choisir la langues 
def download_page(url):
        browser = webdriver.Firefox()
        browser.get(url)
        return browser

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    with open('Resultat.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, quotechar=' ', quoting=csv.QUOTE_ALL)
            spamwriter.writerow(['Title','Note', 'Avis', 'langues'])

    def start_requests(self):
        global url
        url = 'https://www.tripadvisor.com/Hotel_Review-g187791-d13417243-Reviews-Vatican_Suite_383-Rome_Lazio.html'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        driver = download_page(url)

        title = response.css('title::text')[0].extract()
        noteM = response.css('.overallRating::text')[0].extract()
        langues = "fr" #en it fr
        script_lang = "document.getElementById('filters_detail_language_filterLang_"+ langues +"').setAttribute('checked', 'checked')"
        
        # Il faut que je rajoute dans HTML l'attribut ('checked'="checked") 
        # pour s'est faire j'ai rajoute de un code javaScripte pour que ca soit selectionner
       
        driver.execute_script(script_lang)
        driver.find_element_by_css_selector(".taLnk.ulBlueLinks").click()
        
        avis = driver.find_elements_by_class_name('listContainer.hide-more-mobile')
        avv = avis[0].find_elements_by_tag_name("p")

        avis_Brut = ""
        for av in avv:
            avis_Brut += av.text.encode('utf-8') + '\n\n'


        n = driver.find_elements_by_class_name("ui_bubble_rating")
        not_avis = ""
        not_SSavis = ""

        classes = response.css('.ui_bubble_rating').xpath("@class").extract()

        for cls in classes:
            match = re.search(r'bubble_\d+\b', cls)
            if match:
                not_avis = str(format(match.group(0)))
                i = int(re.findall("\d+", not_avis) [0])
                not_SSavis += str(i) + "\n\n" 

        driver.quit()

        with open('Resultat.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([title, not_SSavis, avis_Brut, langues])
