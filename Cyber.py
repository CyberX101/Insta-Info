#CyberMax
#https://t.me/CyberSpyWare

import requests
import os
import webbrowser
from bs4 import BeautifulSoup

try:
    os.system('clear')
except:
    os.system('cls')


red = '\033[31m'
green = '\033[32m'

def get_data(user):

    data, last_posts, user_data, = [], [], {}
    user_data_keys = ['posts', 'followers', 'following']
    url = requests.get(f'https://greatfon.com/v/{user}')
    src = url.content
    soup = BeautifulSoup(src, "html.parser")
    get_data = soup.find_all("li", {"class": "user__item"})
    get_posts = soup.find_all('img', {"class": "content__img"})
    for i in range(len(get_data)):
        data.append(get_data[i].text)
    for i in range(len(get_posts)):
        last_posts.append(get_posts[i].attrs['src'])

    c = 0
    for i in data:
        user_data[user_data_keys[c]] = str(i).rsplit(' ',1)[0].replace(' ','')
        c += 1

    return user_data,last_posts

def get_adv_data(user,type):

    data = []
    url = requests.get(f'https://greatfon.com/v/{user}/{type}')
    src = url.content
    soup = BeautifulSoup(src, "html.parser")
    get_followers = soup.find_all('h6')
    for i in range(len(get_followers)):
        data.append(get_followers[i].text)

    return data

print(f'''

    {red}   █ █▄░█ █▀ ▀█▀ ▄▀█ ▄▄ █ █▄░█ █▀▀ █▀█
    {green}   █ █░▀█ ▄█ ░█░ █▀█ ░░ █ █░▀█ █▀░ █▄█

    
    {green}[+] {red}GitHub : {green}CyberX101

    {green}[+] {red}Programmer : {green}@CyberTrojan

    {green}[+] {red}Telegram : {green}@CyberSpyWare


''')
user = input(f'{green}[!] {red}Enter the instagram user : {green}')
try:
    data = get_data(user)[0]     
    adv = get_data(user)[1]      
    followers_list = get_adv_data(user,'followers')     
    following_list = get_adv_data(user,'following')     
    followers, posts, following = data['followers'], data['posts'], data['following']
    print(f'\n\n {red}User: {green}{user}\n {red}Followers: {green}{followers}\n {red}Following: {green}{following}\n {red}Posts: {green}{posts}\n {red}Last Posts: {green}{adv}\n {red}Last Followers: {green}{followers_list}\n {red}Last Following: {green}{following_list}')
except:
    print(f'\n\n {green}The user {user} is not on the Instagram!')

CyberSpyWare = input(f'{green}[+] {red}Do you want to follow our channel on Telegram ? (y/n) {green}')
if CyberSpyWare == "y":
    webbrowser.open("https://t.me/CyberSpyWare")
else:
    exit()
    
