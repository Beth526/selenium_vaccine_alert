#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:14:25 2021

@author: beth
"""



import time, os
from twython import Twython
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def safeway(url, driver):
    driver.get(url)
    time.sleep(2)
    checkbox = driver.find_element_by_id("attestation_1002")
    checkbox.click()
    time.sleep(2)
    button = driver.find_elements_by_xpath('//button')
    button[-5].click()
    time.sleep(2)
    drop = driver.find_element_by_xpath("//select")
    drop = Select(drop)
    drop.select_by_value('object:60')
    time.sleep(5)
    button = driver.find_elements_by_xpath('//button')
    time.sleep(5)
    button[-1].click()
    time.sleep(5)
    button = driver.find_elements_by_xpath('//button')
    time.sleep(5)
    button[-1].click()
    time.sleep(5)
    button = driver.find_elements_by_xpath('//button')
    for i, b in enumerate(button[-41:-1]):
        try:
            if b.get_attribute('disabled') != 'true':
                button[i].click()
                time.sleep(2)
                test = driver.find_element_by_class_name("empty-event-message.ng-binding")
                if test.text != "There is no availability at this time. Please try a different search or check back later as more availability may open.":
                    print(url)
                    break
        except:
            button = driver.find_elements_by_xpath('//button')
            
def giant(url, driver):
    driver.get(url)
    time.sleep(2)
    bad_q = driver.find_elements_by_xpath('//a')
    try:
        if bad_q[-2].text == 'Get a new place in line ':
            driver.get(bad_q[-2].get_attribute('href'))
            time.sleep(2)
    except:
        pass
    time.sleep(120)
    test = driver.find_element_by_class_name('appointmentTypes')
    if test.text != 'There are currently no COVID-19 vaccine appointments available. Please check back later. We appreciate your patience as we open as many appointments as possible. Thank you.':
        return url
    
    
def adventisthealthcare(driver):
    url = 'https://www.adventisthealthcare.com/coronavirus-covid-19/vaccine/'
    driver.get(url)
    time.sleep(5)
    for i in driver.find_elements_by_xpath('//img')[2:5]:
        if i.get_attribute('src') != 'https://www.adventisthealthcare.com/app/files/public/a9fc4794-7861-4f4b-83fe-9f9924581bd3/icon-checkmark-red.png':
            return url
        
def sixflags_bowie(driver):
    url = 'https://massvax.maryland.gov/appointment-select'
    driver.get(url)
    time.sleep(5)
    button = driver.find_element_by_xpath('//button')
    button.click()
    time.sleep(5)
    box = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/form/span[1]/div/label/input')
    box.click()
    time.sleep(2)
    box = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/form/span[2]/div/label/input')
    box.click()
    box = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/form/span[3]/div/fieldset/div[3]/label[1]/input')
    box.click()
    box = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/form/span[4]/div/fieldset/div[2]/label[4]/input')
    box.click()
    time.sleep(5)
    button = driver.find_elements_by_xpath('//button')
    button[-2].click()
    time.sleep(5)
    #try:
    #    message = driver.find_element_by_class_name("tw-prose.tw-pb-6")
    #    if message.text != "Thank you for contacting the Maryland Department of Health. At this time all appointments for Six Flags America have been reserved through February 15, 2021. Additional appointments will be released in the near future. Please check back periodically by visiting our website to locate additional providers administering vaccines. We ask that you please be patient and understand that the vaccine supply provided to Maryland by the federal government is extremely limited at this time.":
    #        return url
    #except:
    #    return url
    search = driver.find_element_by_xpath('//*[@id="location-search-input"]')
    search.send_keys('Kensington, MD 20895, USA')
    button = driver.find_elements_by_xpath('//button')
    button[-2].click()
    time.sleep(5)
    button = driver.find_elements_by_xpath('//button')
    button[-1].click()
    time.sleep(5)
    button = driver.find_elements_by_xpath('//button')
    button[-1].click()
    time.sleep(5)
    test = driver.find_elements_by_class_name('CalendarDay')
    today = date.today()
    today = today.strftime('%A, %B %-d, %Y')
    for i in range(len(test)):
        if today in test[i].get_attribute('aria-label'):
            continue
        elif 'Not available' in test[i].get_attribute('aria-label'):
            continue
        else:
            return url
        
def CVS(driver):
    url = 'https://www.cvs.com/immunizations/covid-19-vaccine'
    driver.get(url)
    time.sleep(2)
    links = driver.find_elements_by_class_name('link__text')
    for i in range(len(links)):
        if links[i].text == "Maryland":
            MD = links[i]
    MD.click()
    time.sleep(2)
    message = driver.find_element_by_xpath('//*[@id="vaccineinfo-MD"]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[4]/div/p')
    if message.text != 'At this time, all appointments in Maryland are booked. We’ll add more as they become available. Please check back later.':
        return url
    
def Walgreens(driver):
    url='https://www.walgreens.com/findcare/vaccination/covid-19/location-screening'
    driver.get(url)
    search=driver.find_element_by_xpath('//*[@id="inputLocation"]')
    search.clear()
    time.sleep(2)
    search.send_keys('Kensington, MD 20895, USA')
    location='Kensington'
    time.sleep(3)
    button=driver.find_element_by_class_name('btn')
    button.click()
    time.sleep(3)
    message=driver.find_element_by_class_name('fs16')
    if message.text !='Appointments unavailable':
        return (url, location)
    
    search.clear()
    time.sleep(2)
    search.send_keys('Frederick, MD, USA')
    location="Fredrick"
    time.sleep(3)
    button=driver.find_element_by_class_name('btn')
    button.click()  
    time.sleep(2)
    message=driver.find_element_by_class_name('fs16')
    if message.text !='Appointments unavailable':
        return (url, location)
    
    search.clear()
    time.sleep(2)
    search.send_keys('Annapolis, MD, USA')
    location="Annapolis"
    time.sleep(3)
    button=driver.find_element_by_class_name('btn')
    button.click()  
    time.sleep(2)
    message=driver.find_element_by_class_name('fs16')
    if message.text !='Appointments unavailable':
        return (url, location)
    
    search.clear()
    time.sleep(2)
    search.send_keys('Upper Marlboro, MD 20772, USA')
    location="Upper Marlboro"
    time.sleep(3)
    button=driver.find_element_by_class_name('btn')
    button.click()  
    time.sleep(2)
    message=driver.find_element_by_class_name('fs16')
    if message.text !='Appointments unavailable':
        return (url, location)


        
safeway_urls=['https://mhealthcheckin.com/covidvaccine?clientId=1600101762362&region=Maryland&urlId=%2Fvcl%2Fcovid2781', 'https://mhealthcheckin.com/covidvaccine?clientId=1600101367933&region=Maryland&urlId=%2Fvcl%2Fcovid1668', 'https://mhealthcheckin.com/covidvaccine?clientId=1600100832126&region=Maryland&urlId=%2Fvcl%2Fcovid0107', 'https://mhealthcheckin.com/covidvaccine?clientId=1600101507761&region=Maryland&urlId=%2Fvcl%2Fcovid1804','https://mhealthcheckin.com/covidvaccine?clientId=1600101367933&region=Maryland&urlId=%2Fvcl%2Fcovid1668','https://mhealthcheckin.com/covidvaccine?clientId=1600101788886&region=Maryland&urlId=%2Fvcl%2Fcovid2795']
giant_urls=['https://giantfoodsched.rxtouch.com/rbssched/program/covid19/Patient/Advisory','https://reportsonline.queue-it.net/?c=reportsonline&e=giantfoodcovid19&cid=en-US','https://reportsonline.queue-it.net/?c=reportsonline&e=giantfoodcovid19&ver=v3-aspnet-3.6.2&cver=26&man=Giant%20Food','https://reportsonline.queue-it.net/?c=reportsonline&e=giantfoodcovid19&cv=764525675&cid=en-US','https://reportsonline.queue-it.net/?c=reportsonline&e=giantfoodcovid19&ver=v3-aspnet-3.6.2&cver=26&man=Giant%20Food','https://covidinfo.reportsonline.com/covidinfo/GiantFood.html?queueittoken=e_giantfoodcovid19~q_d303ba19-e462-4f79-a176-0c5640aa3a5c~ts_1612817727~ce_true~rt_queue~h_f370e7bfcb5d023463d563f0e62874f552e7d279c61c7bf17df2b1ff83e3fced','https://reportsonline.queue-it.net/?c=reportsonline&e=giantfoodcovid19&ver=v3-aspnet-3.6.2&cver=37&man=Giant%20Food','https://reportsonline.queue-it.net/?c=reportsonline&e=giantfoodcovid19&cv=-1933376203&cid=en-US','https://reportsonline.queue-it.net/?c=reportsonline&e=giantfoodcovid19&cv=-1933376203&cid=en-US','https://reportsonline.queue-it.net/?c=reportsonline&e=giantfoodcovid19&cv=-1933376203&cid=en-US']

safeway_urls=set(safeway_urls)
giant_urls=set(giant_urls)


def check_status(twitter):
    chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    
    result = Walgreens(driver)
    try: 
       if result != None:
           tweet = result[1] + " " + result[0]
           twitter.update_status(status=tweet)
           return None
    except:
        pass
    
    
    result=CVS(driver)
    try: 
       if result != None:
           twitter.update_status(status=result)
           return None
    except:
        pass
    
    
    result = adventisthealthcare(driver)
    try: 
        if result != None:
            twitter.update_status(status=result)
            return None
    except:
        pass
        
    result = sixflags_bowie(driver)
    try:
        if result != None:
            twitter.update_status(status=result)
            return None
    except:
        pass

    for i in giant_urls:
        try:
            result = giant(i, driver)
            if result != None:
                twitter.update_status(status=result)
                return None
        except:
            continue
        
   
    for i in safeway_urls:
        try:
            result = safeway(i, driver)
            if result != None:
                twitter.update_status(status=result)
                return None
        except:
            continue
        
        
    driver.close()
        
            
   
    
    
        


if __name__ == "__main__":
    
    #for tweeting - keys deleted

    APP_KEY = ""
    APP_SECRET = ""
    OAUTH_TOKEN = ""
    OAUTH_TOKEN_SECRET = ""
    

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    
    check_status(twitter)
            
    
            
