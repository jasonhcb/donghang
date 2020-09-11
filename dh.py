import sys
import time
from splinter import Browser

def donghang(url,flight):
    browser = Browser('chrome') # defaults to firefox
    browser.visit(url)

    # browser.visit('http://www.ceair.com/booking/sha-adnh-200724_CNY.html')
    # browser.find_by_css('.ceair-poptip').click()
    time.sleep(5)
    browser.find_by_css('.ceair-input__inner_homesearch').first().fill('敦煌')
    # search_results_xpath = '//*[@class="flight"]/a'  # simple, right?
    # search_results = browser.find_by_css('.shopping-parent-item-container')

    # for search_result in search_results:
    #     str = search_result.text
    #     print(str)
        # sp_str = str.split('\n')
        # # print(sp_str[0])
        # if(sp_str[0].find(flight) != -1):
        #     price = search_result.find_by_css('.economy').text
        #     if(price.find('￥') != -1):
        #         print('有票')
        #         return False
        #     else:
        #         print('无票')
        #         return True
    # browser.quit()
    


url = 'https://global.ceair.com'
flight = 'MU2216'

donghang(url,flight)
# isprice = True
# while isprice:
#     isprice = donghang(url,flight)
#     time.sleep(10)
    