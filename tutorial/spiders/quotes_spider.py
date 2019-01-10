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

    with open('Resul.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, quotechar=' ', quoting=csv.QUOTE_ALL)
            spamwriter.writerow(['Title','Note', 'Avis', 'langues'])



    def start_requests(self):
        global url
        url = 'https://www.tripadvisor.com/Hotel_Review-g187791-d13417243-Reviews-Vatican_Suite_383-Rome_Lazio.html'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        driver = download_page(url)

        title = response.css('title::text')[0].extract()
        note = response.css('.overallRating::text')[0].extract()
        langues = "fr" #en it fr
        script_lang = "document.getElementById('filters_detail_language_filterLang_"+ langues +"').setAttribute('checked', 'checked')"
        
        # Pour selectionner un langues c'est m'as pris un peu de temps parce que 
        # il fallut que je rajoute dans HTML l'attribut ('checked'="checked") 
        # pour s'est faire j'ai rajoute de un code javaScripte pour que ca soit selectionner
       
        driver.execute_script(script_lang)

        avis = driver.find_elements_by_class_name('listContainer.hide-more-mobile')
        supreavis = ""
        for av in avis:
            supreavis += av.text.encode('utf-8') + '\n'

        # driver.quit()

        with open('Resul.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([title, note,supreavis, langues])
        

        # print("___________________ ", dir(langues))
        # filename = 'file_Scgraper_%s.html' % page
        # with open(filename, 'wb') as f:
        #     # print("___________________",response.css('title::text')[0].extract())#extraire que de text
        #     # print("___________________",response.css('title::text').extract_first())#extraire que de text sans les balises
        #     # test = response.css('div.name.ui_header.h2')
        #     print("___________________", response.css('div.ui_radio.item')[0].extract())
        #     print("___________________",test[1].css("span.text::text").extract_first())#extraire div
            
        #     f.write(response.body)

        # self.log('Saved file %s' % filename)