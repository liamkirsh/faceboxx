import chunk
import fbupload
def upload(filedir,username,password):
    chunkSize=100
    chunk.splitFile(filedir,chunkSize)
    #fbupload(filedir,username,password)

def retrive(filename,username,password):
    #get info.txt, files
    f = open(filename+'_info.txt')
    line = f.readline()
    f.close()
    fileName, noOfChunks, chunkSize = line.split(',')
    joinFiles(fileName,noOfChunks,chunkSize)

filename='1.jpg'
username="johaxworthless@gmail.com"
password="sbhacks15"
upload(filename,username,password)
retrive(filename,username,password)
