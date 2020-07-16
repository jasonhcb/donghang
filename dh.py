import sys
import time
from splinter import Browser

def donghang(url,flight):
    browser = Browser('chrome',headless=True) # defaults to firefox
    browser.visit(url)
    # browser.visit('http://www.ceair.com/booking/sha-adnh-200724_CNY.html')
    # browser.find_by_name('search').click()

    # search_results_xpath = '//*[@class="flight"]/a'  # simple, right?
    search_results = browser.find_by_css('.flight')

    for search_result in search_results:
        str = search_result.text
        sp_str = str.split('\n')
        # print(sp_str[0])
        if(sp_str[0].find(flight) != -1):
            price = search_result.find_by_css('.economy').text
            if(price.find('￥') != -1):
                print('有票')
                return False
            else:
                print('无票')
                return True
    browser.quit()
    


url = 'http://www.ceair.com/booking/sha-kmg-200724_CNY.html'
flight = 'MU5818'

isprice = True
while isprice:
    isprice = donghang(url,flight)
    time.sleep(10)
    