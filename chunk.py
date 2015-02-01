#break a file into chunks and join them back 

import pyminizip
import sys
from zipfile import ZipFile
import shutil
import os

compression_level = 9

#make an encrypted zip
def zipcrypt(inputFile, output, password):
   pyminizip.compress(inputFile, output, password, compression_level)
   return

def zipdecrypt(inputFile, password):
   zip = ZipFile(inputFile)
   zip.extractall(pwd=password)
   return

#define the function to split the file into smaller chunks
def splitFile(inputFile,chunkSize):
#read the contents of the file
   f = open(inputFile, 'rb')
   data = f.read()
   f.close()
   os.remove(inputFile)


   # get the length of data, ie size of the input file in bytes
   bytes = len(data)

   #calculate the number of chunks to be created
   noOfChunks= bytes/chunkSize
   if(bytes%chunkSize):
      noOfChunks+=1
   i=0

   #create a info.txt file for writing metadata
   os.mkdir(inputFile)
   for block in zip(*[iter(data)] * chunkSize):
      fn1 = (inputFile + "%s") % i
      f = open(inputFile + '/' + fn1, 'wb')
      f.write(''.join(block))
      f.close()
      i += 1

   f = open('info.txt', 'w')
   f.write(inputFile+','+str(i)+','+str(chunkSize))
   f.close()

#define the function to join the chunks of files into a single file
def joinFiles(fileName,noOfChunks,chunkSize):

   data = []

   for i in range(noOfChunks):
      chunkNum = i

      chunkName = fileName + '%d' % chunkNum
      f = open(fileName + '/' + chunkName, 'rb')
      data.append(f.read())
      f.close()
   shutil.rmtree(fileName)
   f2 = open(fileName, 'wb')
   f2.write(''.join(data))
   f2.close()

# python chunk.py -e file password
if (len(sys.argv) == 4 and sys.argv[1] == "-e"):
   # make encrypted zip
   zipcrypt(sys.argv[2], sys.argv[2] + '.zip', sys.argv[3])

   # call the file splitting function


   splitFile(sys.argv[2] + '.zip', 100)


elif (len(sys.argv) == 4 and sys.argv[1] == "-d"):
   # python chunk.py -d foldername password
   #call the function to join the splitted files
   f = open('info.txt')
   line = f.readline()
   num = line.split(',')[2]
   print ('num', num)
   joinFiles(sys.argv[2], int(num), 100)
   zipdecrypt(sys.argv[2],  sys.argv[3])
else:
   print ('python chunk.py -e file password')
   print ('python chunk.py -d foldername password')
