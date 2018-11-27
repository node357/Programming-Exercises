#############################################################################
#
# Imgur URL Parser 
##################
#
# Create a function that takes an imgur link (as a string) and extracts the
# unique id and type. Return an object containing the unique id, and a string
# indicating what type of link it is.

#############################################################################
import re

def imgurUrlParser(url):

    url_regex          =    "^[http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/|www\.]*[imgur|i.imgur]*\.com"
    url = re.match(url_regex, url).string
   
    gallery_regex     =     re.match(url_regex + "(\/gallery\/)(\w+)", url)
    album_regex       =     re.match(url_regex + "(\/a\/)(\w+)", url)
    image_regex       =     re.match(url_regex + "\/(\w+)", url)
    direct_link_regex =     re.match(url_regex + "(\w+)(\.\w+)", url)
    
    if gallery_regex:
        return { "id" : gallery_regex.group(2), "type" : "gallery" } 
    elif album_regex:
        return { "id" : album_regex.group(2), "type" : "album" }
    elif image_regex:
        return { "id" : image_regex.group(1), "type" : "image" } 
    elif direct_link_regex:
        return { "id" : direct_link_regex.group(1), "type" : "image"}





