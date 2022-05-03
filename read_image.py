import streamlit as st
from PIL import Image
from pexels_api import API
import urllib.request
import os


from pexels_api import API
# Type your Pexels API
PEXELS_API_KEY = '563492ad6f917000010000018b9a138999c246199723bec3093de702'
# Create API object
api = API(PEXELS_API_KEY)
# Search five 'kitten' photos
api.search('Puerto Sherry Puerto de Santa Maria Z9012', page=1, results_per_page=5)
# Get photo entries
photos = api.get_entries()
# Loop the five photos
st.write("## Image from URL example:- ")
st.image("https://cdn.britannica.com/q:60/49/161649-050-3F458ECF/Bernese-mountain-dog-grass.jpg")

for photo in photos:
  # Print photographer
  print('Photographer: ', photo.photographer)
  # Print url
  print('Photo url: ', photo.url)
  # Print original size url
  photo_org = photo.original
  photo_name = photo.description
  print('Photo original size: ', photo_org)
  
  #urllib.request.urlretrieve(f"{photo_org}", "image.jpg")
  #img = Image.open("image.jpg")
  #img_url = photo.original

  #image = Image.open(img_url)
  st.write(photo_name)
  st.image(photo_org)
  #st.image(image, caption=photo.photographer)
  st.write(photo.photographer)


api.curated(results_per_page=10, page=5)
while True:
    # Get all photos in the page
    photos = api.get_entries()
    # For each photo print its properties
    for photo in photos:
        st.write("-----------------------------------------------")
        st.write("Photo id: ", photo.id)
        st.write("Photo width: ", photo.width)
        st.write("Photo height: ", photo.height)
        st.write("Photo url: ", photo.url)
        st.write("Photographer: ", photo.photographer)
        st.write("Photo description: ", photo.description)
        st.write("Photo extension: ", photo.extension)
        st.write("Photo sizes:")
        st.write("\toriginal: ", photo.original)
        st.write("\tcompressed: ", photo.compressed)
        st.write("\tlarge2x: ", photo.large2x)
        st.write("\tlarge: ", photo.large)
        st.write("\tmedium: ", photo.medium)
        st.write("\tsmall: ", photo.small)
        st.write("\ttiny: ", photo.tiny)
        st.write("\tportrait: ", photo.portrait)
        st.write("\tlandscape: ", photo.landscape)
    # If there is no previous page st.write the first page and end the loop
    if not api.has_previous_page:
        st.write("First page: ", api.page)
        break
    # Search previous page
    api.search_previous_page()

