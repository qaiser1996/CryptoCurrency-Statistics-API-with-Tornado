import requests
from bs4 import BeautifulSoup
import json

# Defining getCoinData() function to scrape predictions and historical data of crypto currency im JSON format.
def getCoinData(coin="bitcoin"):
    # Retrieve web page with requests library
    page = requests.get("https://walletinvestor.com/forecast/%s-prediction"%coin)

    # Parse web page with BeautifulSoup library
    parser = BeautifulSoup(page.text,"html.parser")

    # Find the table "w0-container" which contains future predictions of upto 7-Days
    table = parser.find(id="w0-container")
    index = 0

    # Define predictions dictionary, which will contain currency's prediction Data
    # { "yyyy-dd-mm" :
    #                   { "Price":"######.##",
    #                     "Min":"######.##",
    #                     "Max":"######.##" }
    # ...
    # }
    dict_pred = {}


    # Scrapping from web page for predictions data and updating dict_pred, predictions data dictionary
    current_key = ""
    for x in table.find_all("td"):
        if index==0:
            dict_pred[x.text] = {}
            index+=1
            current_key = x.text
            continue

        splits_raw = x.text.split(":  ")
        sub_key = splits_raw[0].strip()
        value = splits_raw[1]
        dict_pred[current_key][sub_key] = value
        index+=1
        if index==4:
            index=0


    # Define historical dictionary, which will contain currency's historical Data
    # { "yyyy-dd-mm" :
    #                   { "Open":"######.##",
    #                     "Close":"######.##",
    #                     "High":"######.##",
    #                     "Low":"######.##"}
    # ...
    # }
    dict_hist = {}

    # Scrapping from web page for historical data and updating dict_hist, historical data dictionary
    table = parser.find(id="w2-container")
    index = 0
    current_key = ""
    for x in table.find_all("td"):
        if index==0:
            dict_hist[x.text] = {}
            index+=1
            current_key = x.text
            continue

        splits_raw = x.text.split(":  ")
        sub_key = splits_raw[0].strip()
        value = splits_raw[1]
        dict_hist[current_key][sub_key] = value
        index+=1
        if index==5:
            index=0


    # Creating a final dictionary which contains both historical and predictions dictionary
    data = {"historical":dict_hist,
            "forecast":dict_pred}

    # Converting the final dictionary to json string
    final_json = json.dumps(data)

    # return final JSON
    return final_json
