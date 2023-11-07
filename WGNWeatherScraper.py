#!/usr/bin/env python 
# jorune00 - jorune.dev -- 2023-11-06 14:25:44
# Web scraping WGN Weather page for local weather data

import requests
from bs4 import BeautifulSoup

url = 'https://wgntv.com/weather/'

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'lxml')
    temp_element = soup.select_one('div.weather-tabs__panel:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)')
    if temp_element:
        tempurature = temp_element.text.strip()
        print(f"WGN Naperville Temp: {tempurature}")
    else:
        print("Temperature element not found.")
else:
    print(f"Failed to retrieve the webpage, status code: {page.status_code}")