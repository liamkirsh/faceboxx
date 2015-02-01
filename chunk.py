import os
#break a file into chunks and join them back 


#define the function to split the file into smaller chunks
def splitFile(inputFile,chunkSize):
	#read the contents of the file
	f = open(inputFile, 'rb')
	data = f.read()
	f.close()
	fileDir, ext=os.path.splitext(inputFile)
	path, name = os.path.split(fileDir)
# get the length of data, ie size of the input file in bytes
	bytes = len(data)

#calculate the number of chunks to be created
	noOfChunks= bytes/chunkSize
	if(bytes%chunkSize):
		noOfChunks+=1

#create a info.txt file for writing metadata
	i = 0
	for block in zip(*[iter(data)] * chunkSize):
		fn1 = name+"_%s" % i
		f = open(fn1, 'wb')
		f.write(''.join([str(x) for x in block]))
		
		f.close()
		i += 1

	f = open(name+'_info.txt', 'w')
	f.write(name+ext+','+str(i)+','+str(chunkSize))
	f.close()

#define the function to join the chunks of files into a single file
def joinFiles(fileName,noOfChunks,chunkSize):

	data = []
	name,ext=os.path.splitext(fileName)
	for i in range(noOfChunks):
		chunkNum = i
		
		chunkName = name + '%s' %chunkNum
		f = open(chunkName, 'rb')
		data.append(f.read())
		f.close()
	f2 = open(fileName, 'wb')
	f2.write(''.join(data))
	f2.close()

'''
# call the file splitting function

splitFile('1.jpg',100)

#call the function to join the splitted files
f = open('info.txt')
line = f.readline()
num = line.split(',')[2]
print 'num', num, 'int', int(num)
joinFiles('chunk',int(num),100)
f.close()
'''
