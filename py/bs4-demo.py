# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import os

bodyStr = '''
<a class="orderCard_cardAsLink" href="accountOrder.account?order=78207165">
  <p class="orderCard_orderStatus">Dispatched <span class="orderCard_orderTotal">£34.99</span></p>
  <p class="orderCard_text">Order Number: 78207165</p>
  <p class="orderCard_text">Order Date: 04/10/16</p>
</a>
'''

soup = BeautifulSoup(bodyStr, 'html.parser')

# accountOrder.account?order=78207165
print '------------------'
print soup.a['href']
print soup.a.get('href')
print soup.find('a', 'orderCard_cardAsLink')['href']
print soup('a', 'orderCard_cardAsLink')[0]['href']
print soup.find_all('a', 'orderCard_cardAsLink')[0]['href']
print soup.find(class_='orderCard_cardAsLink')['href']
print soup.find(class_='orderCard_cardAsLink').get('href')
print soup.select('a')[0]['href']
print soup.select('a[href*="order="]')[0]['href']

# Order Number: 78207165
print '------------------'
print soup.find(text=re.compile('Order Number'))
print soup.find(class_='orderCard_text').string
print soup.find(class_='orderCard_orderStatus').find_next('p').string
print soup.find_all(class_='orderCard_text')[0].string
print soup.select('p:nth-of-type(2)')[0].string
print soup.select('.orderCard_cardAsLink p:nth-of-type(2)')[0].string

# Dispatched
print '------------------'
print soup.find('p', 'orderCard_orderStatus').text.strip()

span_ele = soup.find('span')
span_ele.extract()
print soup.find('p', 'orderCard_orderStatus').text.strip()


print soup.prettify()

