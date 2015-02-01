#Download a file from a given URL

import urllib2
import os

def fbdownload(url,file_name):

 #   file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    f = open("downloads/" + file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()

#fbdownload("https://cdn.fbsbx.com/hphotos-xfp1/v/t59.2708-21/10971559_1377947505849040_1383162146_n.asm/test1.asm?oh=da6c58f5cb8935fd399b0bbecca64ca9&oe=54CF9C97&dl=1")
