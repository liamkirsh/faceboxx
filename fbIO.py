import re
'''
import chunk
import fbupload
def upload(filedir,username,password):
    chunkSize=100
    chunk.zipcrypt(filedir, filedir + '.zip', password)
    chunk.splitFile(filedir+'.zip',chunkSize)
    #fbupload(filedir,username,password)

def retrive(filename,username,password):
    #get info.txt, files
    f = open('info.txt')
    line = f.readline()
    f.close()
    fileName, noOfChunks, chunkSize = line.split(',')
    chunk.joinFiles(fileName,noOfChunks,chunkSize)
    chunk.zipdecrypt(filename,password)
'''
def link_name_map():
    f=open('links.txt')
    links=f.read()
    
    return [re.findall(r'\.txt\/([^?]+)\?', links),links.split('\n')]
'''
filedir='1.jpg'
username="johaxworthless@gmail.com"
password="sbhacks15"
#x=link_name_map()
#print(x[0])
#print(x[1])

#upload(filedir,username,password)
#retrive(filedir,username,password)
'''