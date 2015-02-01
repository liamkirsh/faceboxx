import re
import chunk
import fbupload
import os
from selenium import webdriver

def upload(filedir,username,password):
    chunk.zipcrypt(filedir, filedir + '.zip', password)
    chunk.splitFile(filedir + '.zip')
    
    chunks = os.listdir(filedir + '.zipdir')
    paths = [os.path.abspath(os.path.join(filedir + '.zipdir', part))\
		for part in chunks]
    
    driver = fbupload.fbupload(paths, username, password)
    print 'returned from upload'
    urls = fbupload.fbdownload(filedir, username, password, driver)
    print 'returned from download'
    return urls

def retrieve(filename,username,password):
    #get info.txt, files
    f = open('info.txt')
    line = f.readline()
    f.close()
    fileName, noOfChunks, chunkSize = line.split(',')
    chunk.joinFiles(fileName,noOfChunks,chunkSize)
    chunk.zipdecrypt(filename,password)

def link_name_map():
    f=open('links.txt')
    links=f.read()
    
    return [re.findall(r'\.txt\/([^?]+)\?', links),links.split('\n')]
   
'''
filedir='textfile.txt'
username="johaxworthless@gmail.com"
password="sbhacks15"

urls = upload(filedir, username, password)
for url in urls:
	print url + '\n'

#x=link_name_map()
#print(x[0])
#print(x[1])

#upload(filedir,username,password)
#retrive(filedir,username,password)
'''
