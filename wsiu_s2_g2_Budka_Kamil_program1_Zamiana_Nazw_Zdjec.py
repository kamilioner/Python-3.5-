import os
import datetime

def czas(filename):
        return datetime.datetime.fromtimestamp(os.path.getmtime(filename))
               
for filename in os.listdir("."):
    if filename.endswith(".JPG"):
        print ("zmieniam nazwe pliku", filename)
        dd = str(czas(filename))
        date = dd[:4] + "_" + dd[5:7] + "_" + dd[8:10]
        time = dd[11:13] + "_" + dd[14:16] + "_" + dd[17:19]
        os.rename(filename, 'POL_' + date + "_" + time + '.jpg')
    

