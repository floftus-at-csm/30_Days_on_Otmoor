# 1. for each name in the community gardens list get images from google images, save into folder named by the list
# check for errors - log these errors so I can check them over
# if folder already exists do what?
# 2. compile into gif
# 3. use gif to form a set of composite images
# 4. save composite images in a folder
# 5. compile composite images into a gif
# 6. save gifs into folder

import googlemaps
import json
import time
from pprint import pprint
from PIL import Image
from pathlib import Path
from dotenv import load_dotenv
import os

def load_from_txt_file(txt_file_path):
    with open(txt_file_path) as file:
        array_from_txt_file = file.readlines()
        array_from_txt_file = [line.rstrip() for line in array_from_txt_file]
    return array_from_txt_file

load_dotenv()
# Define the API Key.
# this should be in a hidden file
API_KEY = os.environ.get("GOOGLE_API_KEY")

# Define the Client
gmaps = googlemaps.Client(key = API_KEY)

# load the list of names
common_sites = load_from_txt_file("community_gardens.txt")


# define the fields you would liked return. Formatted as a list.
my_fields = ['name', 'photo'] 
photo_width = 5000                      
photo_height = 5000

dictionary_of_sites = {}
# for land in common_sites:

# get images
for land in common_sites[0:2]:
    # the colon
    # do initial query to get the id for each location
    whats_been_left = gmaps.places(query=land)
    pprint(whats_been_left['results'][0]['place_id'])
    
    digital_id = whats_been_left['results'][0]['place_id']

    # add digital id to dictionary next to the site name (land)
    dictionary_of_sites[land] = digital_id
    # print("the dictionary is: ", dictionary_of_sites)

    # do second query, the details query, which allows you access to the photo urls
    places_details  = gmaps.place(place_id= digital_id , fields= my_fields)
    print("the places details are: ", places_details['result'])
    val = 0

    land_file_name = land.replace(" ", "_")
    path_s = "static/downloaded/" + land_file_name + "/"
    Path(path_s).mkdir(parents=True, exist_ok=True)

    # for photo in places_details['result']['photos']:
    try:
        # for index, photo in places_details['result']['photos'].enumerate():
        for photo in places_details['result']['photos']:
            # print("the index is: ", index)
            print("inside the try!")

            photo_id = photo['photo_reference']

            # request the image, using the Places Photot API.
            raw_image_data = gmaps.places_photo(photo_reference = photo_id, max_width = photo_width, max_height = photo_height)
            print("the raw image date is", type(raw_image_data))
            download_path_s = path_s + land_file_name + str(val) + ".png"
            # raw image data is returned so we will save that raw data to a JPG file.

            f = open(download_path_s, 'wb')

            # save the raw image data to the file in chunks.
            for chunk in raw_image_data:
                if chunk:
                    print(chunk)
                    print(type(chunk))
                    # potentially resize here 
                    f.write(chunk)
            f.close()

            val = val + 1 
    except:
        print("********************************")
        print("no photos in: ", land)
        print("********************************")

# process images