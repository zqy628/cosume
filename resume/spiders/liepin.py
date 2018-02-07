#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import scrapy,time
from selenium import webdriver
from resume.config import get_cookies
from resume.items import ResumeItem
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ResumeSpider(scrapy.Spider):
    name = "liepin"
    allowed_domains = ["liepin.com"]
    start_urls = [
        "https://passport.liepin.com/h/account",
    ]
    print(sys.version_info)
    print(u'\n******请输入搜索关键词，多个关键词空格隔开,回车确认******\n')
    search_words = u'成都 计算机'
    # search_words = input()

    def parse(self, response):
        #模拟登录
        # cookies = get_cookies()
        url = 'https://h.liepin.com/search/getConditionItem/'
        cookies = [{u'domain': u'.liepin.com', u'secure': False, u'value': u'6F0A6B19FFA848194C83BB5FC5162C4A', u'expiry': 3665470056.78636, u'path': u'/', u'httpOnly': False, u'name': u'_uuid'}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'5a5d5a0e8e50e5cddb3c9c6d04a.jpg', u'expiry': 3665470076.779085, u'path': u'/', u'httpOnly': False, u'name': u'user_photo'}, {u'domain': u'.liepin.com', u'name': u'__tlog', u'value': u'1517986409581.77%7C00000000%7C00000000%7C00000000%7C00000000', u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.liepin.com', u'name': u'verifycode', u'value': u'8d799a61fec94a2dba48739c9fd7275e', u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'2', u'expiry': 1518019200, u'path': u'/', u'httpOnly': False, u'name': u'__uv_seq'}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'1517986409580.23', u'expiry': '2148706409L', u'path': u'/', u'httpOnly': False, u'name': u'__uuid'}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'1517986410', u'expiry': 1549522431, u'path': u'/', u'httpOnly': False, u'name': u'Hm_lvt_a2647413544f5a04f00da7eee0d5e200'}, {u'domain': u'.liepin.com', u'name': u'_mscid', u'value': u'00000000', u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'0', u'expiry': 1518072819, u'path': u'/', u'httpOnly': False, u'name': u'_fecdn_'}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'%E5%BC%A0%E4%BD%B3%E5%98%89', u'expiry': 1518029989.295683, u'path': u'/', u'httpOnly': False, u'name': u'user_name'}, {u'domain': u'.liepin.com', u'secure': True, u'value': u'6OsIMyEMywn%2F53GMjmJb56hKj9qgAmTK%2FS8NgRoBhIXqCfy34PrgQwuCq7gHxBEhmxkgcMULNLH5%0D%0APOD4zXFC7UAUwGmkkoC3vOW403YeTuNtHq6ug%2Fqtm5qERcp2kHkBnnVio3gbkkrztRYgYYXqn12g%0D%0Ajojux42n8vLEgw%3D%3D%0D%0A', u'expiry': 1518029989.295697, u'path': u'/', u'httpOnly': True, u'name': u'lt_auth'}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'2', u'expiry': 3665470076.295735, u'path': u'/', u'httpOnly': False, u'name': u'user_kind'}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'90245055b3e2a2961a667e00ad0d9493', u'expiry': 1518029989.295713, u'path': u'/', u'httpOnly': False, u'name': u'UniqueKey'}, {u'domain': u'.liepin.com', u'name': u'socketConnectStore', u'value': u'%7B%22pageId%22%3A%22webim_pageid_1381824022947.2449%22%2C%22connectDomain%22%3A%22liepin.com%22%2C%22socketConnect%22%3A%221%22%7D', u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'd1aa898b78a4ca44', u'expiry': 1518029629.779112, u'path': u'/', u'httpOnly': False, u'name': u'_h_ld_auth_'}, {u'domain': u'h.liepin.com', u'name': u'JSESSIONID', u'value': u'343EA8E594A884311B55365362BD36A0', u'path': u'/', u'httpOnly': True, u'secure': False}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'f2b5127a-3983-4f39-b38b-2eb4a008f23a', u'expiry': 1612594430, u'path': u'/', u'httpOnly': False, u'name': u'gr_user_id'}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'a452b47f-33b8-4411-acf9-c66b7b1da221', u'expiry': 1517988230, u'path': u'/', u'httpOnly': False, u'name': u'gr_session_id_87ae51ccbd70d69e'}, {u'domain': u'.liepin.com', u'secure': False, u'value': u'user_id%3A305c6770076e31805ceefa20e0ffb33d', u'expiry': 1517988230, u'path': u'/', u'httpOnly': False, u'name': u'gr_cs1_a452b47f-33b8-4411-acf9-c66b7b1da221'}, {u'domain': u'.liepin.com', u'name': u'__session_seq', u'value': u'2', u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.liepin.com', u'name': u'Hm_lpvt_a2647413544f5a04f00da7eee0d5e200', u'value': u'1517986431', u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'h.liepin.com', u'name': u'WebIMToken', u'value': u'%7B%22imClientId%22%3A%2218c10cd84a8a06fc5844501a06fd0d45%22%2C%22accessToken%22%3A%2218c10cd84a8a06fc95254e01174bbaa8be344ddbcaee6555997745a4c6488435%22%2C%22imId%22%3A%2218c10cd84a8a06fc6ddb46921ed98068%22%2C%22userId%22%3A%22305c6770076e31805ceefa20e0ffb33d%22%2C%22imUserType%22%3A%222%22%2C%22time%22%3A1517986431667%7D', u'path': u'/', u'httpOnly': False, u'secure': False}]
        print (cookies,url)
        driver = webdriver.Chrome()
        driver.set_window_size(width=1820, height=980)
        driver.get(url)
        for cookie in cookies:
            driver.add_cookie(cookie)
        time.sleep(1)
        driver.refresh()
        time.sleep(1)

        # action = ActionChains(driver)
        # action.send_keys(Keys.ESCAPE).perform()
        # time.sleep(1)
        # action.send_keys(Keys.ESCAPE).perform()
        # time.sleep(1)
        # driver.find_element_by_css_selector('[data-name=resume]').click()
        driver.find_element_by_css_selector('#keywords-suggest .text').send_keys(self.search_words)
        time.sleep(1)
        driver.find_element_by_css_selector('.bt-search input').click()
        # driver.find_element_by_css_selector('#keywords-suggest .text').send_keys(self.search_word)
        # time.sleep(1)
        # driver.find_element_by_css_selector('.bt-search input').click()
        time.sleep(1)
        cosume_cookies = driver.get_cookies()
        cookiestr = {c['name']:c['value'] for c in cosume_cookies}
        # for item in cosume_cookies:
        #     cookiestr[item["name"]] = item["value"]
        print(cookiestr)
        while driver.find_element_by_css_selector('.current+a').get_attribute("class") != 'disabled':
            full_urls = driver.find_elements_by_css_selector('.table-list-peo a')
            for url in full_urls:
                print(url.get_attribute("href"))
                yield scrapy.Request(url.get_attribute("href"),cookies=cookiestr, callback=self.parse_resume)
            driver.find_element_by_css_selector('.current+a').click()
            time.sleep(1)
        driver.quit()

    def parse_resume(self,response):
        item = ResumeItem()
        print(response.css('title::text').extract())
        yield item
