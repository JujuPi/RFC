#!/usr/bin/python2.7
# coding=utf-8

"""Copyright © 16/02/2016,Julien Poupeney

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the “Software”), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.

The Software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the
warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or
copyright holders X be liable for any claim, damages or other liability, whether in an action of contract,
tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the Software.
Except as contained in this notice, the name of Julien Poupeney shall not be used in advertising or otherwise
to promote the sale, use or other dealings in this Software without prior written authorization from Julien Poupeney»"""



import socket,datetime,time,logging
from DataBaseManagement import *


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
TCP_IP = '192.168.20.105'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
while True:
    s.listen(2)



    while 1:
        conn, addr = s.accept()
        logging.info('Connection address:'+addr[0])
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        logging.info("received data:"+str((datetime.datetime.now()))+" "+ data)
        badge_log(datetime.datetime.now(),data,addr[0])
        conn.send("hello")  # echo
        conn.close()
        logging.info( "fermeture connexion")



