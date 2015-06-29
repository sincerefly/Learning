#/usr/bin/python
# -*- coding : utf-8 -*-
from bs4 import BeautifulSoup
import requests

#https://github.com/yxjxx/v2ex_daily_mission

# settings 
username = 'username'   # your v2ex username
password = 'password'    # your v2ex password
login_url = 'https://v2ex.com/signin'
home_page = 'https://www.v2ex.com'
mission_url = 'https://www.v2ex.com/mission/daily'

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36"

headers = {
        "User-Agent" : UA,
        "Host" : "www.v2ex.com",
        "Referer" : "https://www.v2ex.com/signin",
        "Origin" : "https://www.v2ex.com"
}


def make_soup(url,tag,name, v2ex_session):

    page = v2ex_session.get(url,headers=headers,verify=True).text
    soup = BeautifulSoup(page)
    soup_result = soup.find(attrs = {tag:name})
    # print soup_result
    return soup_result

def build_post(v2ex_session):

    once_vaule = make_soup(login_url,'name','once', v2ex_session)['value']
    print(once_vaule)
    
    post_info = {
        'u' : username,
        'p' : password,
        'once' : once_vaule,
        'next' : '/'
    }
    return post_info

def start_run():

    # Get session
    v2ex_session = requests.Session()

    # Build the post data
    post_data = build_post(v2ex_session)

    # 
    resp = v2ex_session.post(login_url, data=post_data, headers=headers, verify=True)
    
    short_url = make_soup(mission_url, 'class', 'super normal button', v2ex_session)['onclick']
    
    
    first_quote = short_url.find("'")
    last_quote = short_url.find("'", first_quote+1) #str.find(str, beg=0 end=len(string))
    final_url = home_page + short_url[first_quote+1:last_quote]
    
    page = v2ex_session.get(final_url,headers=headers,verify=True).content
    
    flag = make_soup(mission_url, 'class', 'fa fa-ok-sign', v2ex_session)

    return flag


if  __name__ == '__main__':

    flag = start_run()

    if flag:
        print ("Sucessful.")
    else:
        print ("Something wrong.")

















