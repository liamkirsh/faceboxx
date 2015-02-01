#break a file into chunks and join them back 

import pyminizip
import sys
from zipfile import ZipFile
import shutil
import os

compression_level = 9
CHUNK_SIZE = 6000

#make an encrypted zip
def zipcrypt(inputFile, output, password):
   pyminizip.compress(inputFile, output, password, compression_level)
   return

def zipdecrypt(inputFile, password):
   zip = ZipFile(inputFile)
   zip.extractall(pwd=password)
   return

#define the function to split the file into smaller chunks
<<<<<<< HEAD
def splitFile(inputFile):
   #read the contents of the file
   #f = open(inputFile, 'rb')
   f = open(inputFile, 'r')
   data = f.read()
   f.close()
   print 'original data len' + str(len(data))
   #os.remove(inputFile[:-4])
   #os.remove(inputFile)

   #create a info.txt file for writing metadata
   i = 0
   j = 0
   os.mkdir(inputFile + 'dir')
   while (CHUNK_SIZE * i < len(data)):
      #print str(len(block)) + '\n'
      #blockfile = open(inputFile + 'dir' + '/' + inputFile + str(i), 'wb')
      blockfile = open(inputFile + 'dir' + '/' + inputFile + str(i), 'w')
      blockfile.write(data[CHUNK_SIZE * i:CHUNK_SIZE * (i + 1)])
      #print 'line 40 blocksize: ' + str(len(''.join(block)))
      i += 1
      #print 'line 42: i is ', str(i)
      blockfile.close()
   #sys.exit(1)
   if (CHUNK_SIZE * i + j < len(data)):
      print 'overflowed!'
      blockfile = open(inputFile + 'dir/' + inputFile + str(i), 'w') 
      print 'i is ' + str(i) + '\n'
      print 'CHUNK_SIZE is ' + str(CHUNK_SIZE)
      print 'j is ' + str(j)
      print 'len of data is ' + str(len(data))
      print 'so what is CHUNK_SIZE * i + j?', str(CHUNK_SIZE*i+j)
      while (((CHUNK_SIZE * i) + j) < len(data)): 
         print 'overflowed a bit\n'
         blockfile.write(data[CHUNK_SIZE * i + j])
         j += 1
      blockfile.close()
   if (j > 0): i += 1
   infofile = open('info.txt', 'w')
   infofile.write(inputFile + ',' + str(i) + ',' + str(CHUNK_SIZE))
   infofile.close()
   return
=======
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
>>>>>>> ed133f0b3d05d8cb6722e8f22b3185cf21c21766

#define the function to join the chunks of files into a single file
def joinFiles(fileName, noOfChunks):
   # this function works
   data = []
   for i in range(noOfChunks):
      chunkName = fileName + '/' + fileName[:-3] + str(i)
      curChunk = open(chunkName, 'rb')
      data.append(curChunk.read())
      curChunk.close()
   shutil.rmtree(fileName) # delete folder of chunks
   joined = open(fileName, 'wb')
   joined.write(''.join(data)) # write joined chunk file
   joined.close()
   return

#splitFile('spim.png')
#joinFiles('spim.png') 

<<<<<<< HEAD
=======
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
>>>>>>> ed133f0b3d05d8cb6722e8f22b3185cf21c21766

# python chunk.py -e file password
if (len(sys.argv) == 4 and sys.argv[1] == "-e"):
   # make encrypted zip
   zipcrypt(sys.argv[2], sys.argv[2] + '.zip', sys.argv[3])

   # call the file splitting function

<<<<<<< HEAD
   splitFile(sys.argv[2] + '.zip')
=======

   splitFile(sys.argv[2] + '.zip', 100)
>>>>>>> ed133f0b3d05d8cb6722e8f22b3185cf21c21766


elif (len(sys.argv) == 4 and sys.argv[1] == "-d"):
   # python chunk.py -d foldername password
   #call the function to join the splitted files
   f = open('info.txt')
   line = f.readline()
<<<<<<< HEAD
   f.close()
   num = line.split(',')[1]
   print 'num', num
   joinFiles(sys.argv[2], int(num))
=======
   num = line.split(',')[2]
   print ('num', num)
   joinFiles(sys.argv[2], int(num), 100)
>>>>>>> ed133f0b3d05d8cb6722e8f22b3185cf21c21766
   zipdecrypt(sys.argv[2],  sys.argv[3])
else:
   print ('python chunk.py -e file password')
   print ('python chunk.py -d foldername password')
