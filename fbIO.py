import chunk
import fbupload
def upload(filedir,username,password):
    chunkSize=100
    path, fname = os.path.split(filedir)
    chunk.zipcrypt(fname, fname + '.zip', password)
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
filename='1.jpg'
username="johaxworthless@gmail.com"
password="sbhacks15"
upload(filename,username,password)
retrive('1',username,password)
