#!/usr/bin/env python 
# jorune00 - jorune.dev -- 2023-11-07 08:39:42
# Web scraping Weather Underground page for local weather data

import requests
from bs4 import BeautifulSoup

url = 'https://www.wunderground.com/dashboard/pws/KILAUROR99'

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'lxml')
    temp_element = soup.select_one('.main-temp > lib-display-unit:nth-child(1) > '
                                   'span:nth-child(1) > span:nth-child(1)')
    if temp_element:
        tempurature = temp_element.text
        print(f"KILAUROR99 Temp: {tempurature}")
    else:
        print("Temperature element not found.")
else:
    print(f"Failed to retrieve the webpage, status code: {page.status_code}")