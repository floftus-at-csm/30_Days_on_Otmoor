# 30_Days_on_Otmoor

This is the repository for my environmental media lab piece
it will be a low-tech web artwork inspired by the rebellion to enclosure on otmoor in the mid-1800s
The piece will comprise of a set of scenes that will refresh every cycle of the moon

scene 1:    
    names of places of commons (with a central point at otmoor*) in the shape of tools (trowels, spaces, gloves, hoes, etc.). The names will be gathered from shared assets website, users can add names of locations via an input box
scene 2:    
    images from the locations wrapped around knots
scene3:     
    somehow deals with abolition and the relationship between enclosure and commons
    ideas: programmatically scrubbing out military and police sites from map/images

links will be available to all locations

Ideally, this website is as low power as possible and could run of solar power

setup idea: 
    hardware
        raspberry pi - preferably a pizero
        e-ink screen
        18650 battery
        solar panel
        wifi connection

    software
        3D software - 3JS or GLSLViewer (this would be lower power I reckon)
        image-processing software - python PIL/wand or Javascript Sharp
        website - nodejs + HTML + CSS + Js
        fetching images from api
        storing locations (this could be a really simple server like a )
        30 day timer running on the server

    1. nodejs server handling fetching images from Place API, could handle glslviewer?
    2. website displaying three scene


*ie. I'll start at otmoor and work out
don't follow national lines


How to use Google Place Photo API
1. make a places search request
return a place id
2. make a places details request
this requires some parameter
get back a photoreference id



Creating a 2D texture from 2D Images
explore the file structure when you do photogrammetry
could I then programmatically adjust this file?
would there be enough detail? they're around 4k x 4k
so I think so
could always have multiple objects




Project Structure:
2 parallel processes
One web app, one local script

1. Image Gathering, Fermenting
Python script get images from API from a list of Commons 
(list of commons is a file on the )
Saving Images 
then composites images into batches of 2D Textures for 3D Models
(this could just start as compositing into 2D Images)
screenshots taken of 3D models being rotated - then dithered (e.g. 30 images going round the whole model)
images saved into folders
make gif from images
this is done at every full moon


2. Web Application 
a web application that shows the rotated 3D models as gifs
served as a simple website for now
information about project also available
time until next full moon also available
functions
    input to add to the commons list
    
    