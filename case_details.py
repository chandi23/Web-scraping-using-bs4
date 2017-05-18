#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from PIL import Image
import urllib
import urllib2
import cStringIO
from cStringIO import StringIO
import re
from bs4 import BeautifulSoup
from datetime import datetime, time, date
import shutil


def get_case_status(case_type, case_number, case_year):
    url = 'http://www.greentribunal.gov.in/search_all_case.aspx'
    session = requests.Session()
    response = session.get(url)
    response = response.text
    soup = BeautifulSoup(response)
    parameters = {}
    parameters['__EVENTARGUMENT'] = ''
    parameters['__EVENTTARGET'] = ''
    parameters['__EVENTVALIDATION'] = ''
    parameters['__LASTFOCUS'] = ''  # parameters
    parameters['__VIEWSTATE'] = ''
    parameters['__VIEWSTATEENCRYPTED'] = ''
    parameters['__VIEWSTATEGENERATOR'] = ''
    parameters['ctl00$content2$btn_submit'] = 'Display'
    parameters['ctl00$content2$csrfval'] = ''
    parameters['ctl00$content2$ddl_case'] = '3'
    parameters['ctl00$content2$ddl_year'] = '2015'
    parameters['ctl00$content2$ddl_year1'] = 'All'
    parameters['ctl00$content2$entercode'] = ''
    parameters['ctl00$content2$hfCustomerId'] = ''
    parameters['ctl00$content2$text_res'] = ''
    parameters['ctl00$content2$txtDairyNo'] = ''
    parameters['ctl00$content2$txt_no'] = '325/2015'
    parameters['ctl00$csrfval'] = ''

    for i in soup.find_all('input'):
        if i['name'] == '__EVENTARGUMENT':
            parameters['__EVENTARGUMENT'] = i['value']
        elif i['name'] == '__EVENTTARGET':
            parameters['__EVENTTARGET'] = i['value']
        elif i['name'] == '__EVENTVALIDATION':
            parameters['__EVENTVALIDATION'] = i['value']
        elif i['name'] == '__LASTFOCUS':

                                                              # dynamic values

            parameters['__LASTFOCUS'] = i['value']
        elif i['name'] == '__VIEWSTATE':
            parameters['__VIEWSTATE'] = i['value']
        elif i['name'] == '__VIEWSTATEENCRYPTED':
            parameters['__VIEWSTATEENCRYPTED'] = i['value']
        elif i['name'] == 'ctl00$content2$btn_submit':
            parameters['ctl00$content2$btn_submit'] = i['value']
        elif i['name'] == 'ctl00$csrfval':
            parameters['ctl00$csrfval'] = i['value']

    response = \
        session.get('http://greentribunal.gov.in/Admin/captcha.ashx',
                    stream=True)
    url = 'http://www.greentribunal.gov.in/search_all_case.aspx'
    with open('captcha_cs.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    im = Image.open('captcha_cs.png')
    im.show()
    captcha = raw_input('')
    parameters['ctl00$content2$entercode'] = captcha
    response = session.post(url, data=parameters)
    response = response.text
    soup = BeautifulSoup(response)

    for i in soup.find_all('input'):
        if i['name'] == '__EVENTARGUMENT':
            parameters['__EVENTARGUMENT'] = i['value']
        elif i['name'] == '__EVENTTARGET':
            parameters['__EVENTTARGET'] = i['value']
        elif i['name'] == '__EVENTVALIDATION':
            parameters['__EVENTVALIDATION'] = i['value']
        elif i['name'] == '__LASTFOCUS':

            # dynamic values

            parameters['__LASTFOCUS'] = i['value']
        elif i['name'] == '__VIEWSTATE':
            parameters['__VIEWSTATE'] = i['value']
        elif i['name'] == '__VIEWSTATEENCRYPTED':
            parameters['__VIEWSTATEENCRYPTED'] = i['value']
        elif i['name'] == 'ctl00$content2$btn_submit':
            parameters['ctl00$content2$btn_submit'] = i['value']
        elif i['name'] == 'ctl00$csrfval':
            parameters['ctl00$csrfval'] = i['value']
    all_order = soup.find(id='content2_grvori_lnkbtnshowoa_0')
    link = all_order.get('href')
    link = re.search(r'javascript:__doPostBack\(\'(.*)\'\,.*\)', link)
    if link:
        link = link.group(1)
        parameters['__EVENTTARGET'] = link

     # do not need this, creating issue

    if 'ctl00$content2$btn_submit' in parameters:
        del parameters['ctl00$content2$btn_submit']
    response = session.post(url, data=parameters)
    response = response.text

    soup = BeautifulSoup(response)
    petitioner = soup.find(id='content2_lblpartyname1').get_text()
    respondent = soup.find(id='content2_lblpartyname3').get_text()
    case_status = soup.find(id='content2_lblstatus').get_text()

    is_disposed = False
    if case_status != 'DisposedOff':
        is_disposed = False
    else:
        is_disposed = True

    values = {'petitioner': petitioner, 'respondent': respondent,
              'is_disposed': is_disposed}
    print values
    return values


if __name__ == '__main__':
    get_case_status('3', '325/2015', '2015')

			
