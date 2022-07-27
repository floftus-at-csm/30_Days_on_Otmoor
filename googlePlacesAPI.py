# import the library
import googlemaps
import json
import pprint
import xlsxwriter
import time
from pprint import pprint
from PIL import Image
from pathlib import Path

# Define the API Key.

from dotenv import load_dotenv
import os

load_dotenv()
# Define the API Key.
# this should be in a hidden file
API_KEY = os.environ.get("GOOGLE_API_KEY")

# Define the Client
gmaps = googlemaps.Client(key = API_KEY)

# Do a simple nearby search where we specify the location
# in lat/lon format, along with a radius measured in meters
# places_result  = gmaps.places_nearby(location='-33.8670522,151.1957362', radius = 40000, open_now =False , type = 'restaurant')

query_s = 'Spitalfields City Farm'
places_query_result = gmaps.places(query=query_s)
# pprint(places_query_result)
# for place in places_query_result:
#     print(place)
pprint(places_query_result['results'][0]['place_id'])
time.sleep(3)

my_place_id = places_query_result['results'][0]['place_id']

# define the fields you would liked return. Formatted as a list.
my_fields = ['name', 'photo']

# make a request for the details using the Places API.
places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

photos = places_query_result['results'][0]['photos']
print(len(photos))
# place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])
val = 0

name_s = query_s.replace(" ", "_")
path_s = "downloaded/" + name_s + "/"
Path(path_s).mkdir(parents=True, exist_ok=True)

for photo in places_details['result']['photos']:

    photo_id = photo['photo_reference']
    photo_width = 1000                      
    photo_height = 1000

        # request the image, using the Places Photot API.
    raw_image_data = gmaps.places_photo(photo_reference = photo_id, max_width = photo_width, max_height = photo_height)

    download_path_s = path_s + name_s + str(val) + ".png"
    # raw image data is returned so we will save that raw data to a JPG file.

    f = open(download_path_s, 'wb')

    # save the raw image data to the file in chunks.
    for chunk in raw_image_data:
        if chunk:
            f.write(chunk)
    f.close()

    val = val + 1 
    # we will open the newly saved photo, to display the photo.
    # im = Image.open(name_s)
    # im.show()

# # make a request for the details using the Places API.
places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

print(places_details)
# stored_results = []

# # loop through each of the places in the results, and get the place details.      
# for place in places_query_result['results']:

#     # define the place id, needed to get place details. Formatted as a string.
#     my_place_id = place['place_id']

#     # define the fields you would liked return. Formatted as a list.
#     my_fields = ['name','formatted_phone_number','website']

#     # make a request for the details.
#     places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

#     # print the results of the details, returned as a dictionary.
#     pprint.pprint(places_details['result'])

#     # store the results in a list object.
#     stored_results.append(places_details['result'])

# # -------------- DUMPING VALUES IN EXCEL -----------------------

# # define the headers, that is just the key of each result dictionary.
# row_headers = stored_results[0].keys()

# # create a new workbook and a new worksheet.
# workbook = xlsxwriter.Workbook(r'C:\Users\305197\Desktop\data.xlsx')
# worksheet = workbook.add_worksheet()

# # populate the header row
# col = 0
# for header in row_headers:
#     worksheet.write(0, col, header)
#     col += 1

# row = 1
# col = 0
# # populate the other rows

# # get each result from the list.
# for result in stored_results:

#     # get the values from each result.
#     result_values = result.values()

#     # loop through each value in the values component.
#     for value in result_values:
#         worksheet.write(row, col, value)
#         col += 1
    
#     # make sure to go to the next row & reset the column.
#     row += 1
#     col = 0

# # close the workbook
# workbook.close()