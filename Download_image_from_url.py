# ###########################################################################################################
#Method 1: #Simple downloading image from a URL using wget module
# ###########################################################################################################
# import wget
# #
# # image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Namma_Metro_Phase_1_line_map.png"
# image_url="http://jvcorp-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/linkedin.png" # This gets 403 Error
# Namma_metro=wget.download(image_url)
# print(Namma_metro)

# ###########################################################################################################
#Method 2: #Simple downloading image from a URL using Requests module
# ###########################################################################################################
import requests
# image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Namma_Metro_Phase_1_line_map.png"
image_url="https://jvcorp-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/linkedin.png"
r = requests.get(image_url, stream=True) #
#Note that you need to open the destination file in binary mode to ensure python doesn't try and translate newlines for you.
#We also set stream=True so that requests doesn't download the whole image into memory first.

path = 'E:/Test/Our_Metro.png'
with open(path,'wb') as f:
    for chunk in r.iter_content(): #r.iter_content() returns a generator and chunk gives a part downloaded and that is written into a file.
        f.write(chunk)
        f.flush() #The flush() method cleans out the internal buffer.


# ###########################################################################################################
#Method 3: Downloading image from a URL using Requests and Shutil modules
# ###########################################################################################################
# import requests
# import shutil  # Shell Utilities module (manipulate the filesystem, make archives, etc.)
#
# image_url="http://jvcorp-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/linkedin.png"
# resp = requests.get(image_url, stream=True)
# # Open a local file with wb ( write binary ) permission.
# local_file = open('LinkedIn.png', 'wb')
# # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
# resp.raw.decode_content = True
# # Copy the response stream raw data to local image file.
# shutil.copyfileobj(resp.raw, local_file)
# # Remove the image url response object.
# del resp


# ###########################################################################################################
#Method 4: #Downloading image from a URL and showing progress of the download, run this program in Terminal
# ###########################################################################################################
# from clint.textui import progress
# import requests
#
# image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Namma_Metro_Phase_1_line_map.png"
# r = requests.get(image_url, stream=True)
# #print(r.headers)
# #print(r.headers.get('content-length'))
# path = 'E:/Test/Namma_metro5.png'
# with open(path, 'wb') as f:
#     total_length = int(r.headers.get('content-length'))
#     for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):  #O/p: [###############] 76441/76441 - 00:00:09
#     #for chunk in progress.mill(r.iter_content(chunk_size=10), expected_size=(total_length / 10) + 1): #O/P : Spinner  /
#         if chunk:
#             f.write(chunk)
#             f.flush()

# ###########################################################################################################