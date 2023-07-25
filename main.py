# List of libraries
# BeautifulSoup, time

import requests
from bs4 import BeautifulSoup
from time import sleep
import json


'''User-agent is some info about user who search info on internet
    Without user-agent it is complicated to parse data 
    some sites will return error messages'''
headers = {"User-Agent":
            "Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>"}

# range of list's cards - will return parsing info about 8 lists of cards
for count in range(1, 8):

    sleep(5)
    # url address
    url_address = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    response_from_web_site = requests.get(url_address, headers=headers)

    soup_helper = BeautifulSoup(response_from_web_site.text, "lxml")  # html.parser

    data = soup_helper.find_all("div", class_="col-lg-4 col-md-6 mb-4")

    # getting data as titles, links and links to exact images
    for info in data:
        name_of_product = info.find("h4", class_="card-title").text.replace("\n", "")
        price = info.find("h5").text
        url_card = "https://scrapingclub.com" + info.find("a").get("href")
        url_card_image = "https://scrapingclub.com" + info.find("img", class_="card-img-top img-fluid").get("src")

        # space between info
        data_result = "\n\n" + name_of_product + "\n\n" + price + "\n\n" + url_card + "\n\n" + url_card_image
        print(data_result)

        # format of result - json file
        json_object = json.dumps(data_result)

        with open("scraping_Club.json", "w") as file:
            file.write(json_object)




