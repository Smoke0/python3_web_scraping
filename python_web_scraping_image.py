"""
The Basic idea here for retrieving image is basically to perform webscraing on google
and save the first image locally.
"""

import requests
import urllib
from bs4 import BeautifulSoup
import json

def retrieve_image(keyword):
    # Header are required to mimic the browser
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    print('Wait for a while,image is being retrieved......')
    print('It will be saved in same directory as python file\n')
    # google url to request the image from here tbm=isch means we are searching for image where source determines who is making
    # search request browser, application etc. keyword is the query we are performing
    url = "https://www.google.co.in/search?q=" + keyword + "&source=lnms&tbm=isch"

    try:
        # req here is the request object we are creating as a browser would
        # res is the response object we get from the google server.
        req = urllib.request.Request(url, headers=header)
        res = urllib.request.urlopen(req)
        print(res)
        # here we are using beautiful soup library to parse the res document so we can easly find desired elements of html
        # right now google stores the links of images in a div tag of class rg_meta notranslate so we can extract those div tags and retrieve the url of image
        soup = BeautifulSoup(res, 'html.parser')
        one_div_tag = soup.findAll('div', {'class': 'rg_meta notranslate'})[0]  # we are only extracting one image

        # the output by soup.findAll is a string so we need to convert it into JSON so we can extract the url stored in 'ou' arrtibute of div tag and 'ity' attribute stores image type.
        download_url, img_type = json.loads(one_div_tag.text)['ou'], json.loads(one_div_tag.text)['ity']
        # now as we have url of image we can save it using urlopen function from there we read the data of image and write that data on a local file.
        with urllib.request.urlopen(download_url) as res, open(keyword + '.' + img_type, 'wb') as file:
            try:
                data = res.read()
                file.write(data)
            except Exception as e:
                print(e)
        print('Done') # for indicating success.
    except Exception as e:
        print('Could not retrieve data please try again')
        print(e)

# call to retrieve function
retrieve_image(input('Enter Keyword to search\n'))