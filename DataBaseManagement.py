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
to promote the sale, use or other dealings in this Software without prior written authorization from Julien Poupeney"""

import psycopg2,logging


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)


def badge_log(date,id_badge,ip):
    logging.info("appel fonction")
    conn = psycopg2.connect("host=192.168.20.105 dbname=rfid_base user=rfid password=rfid ")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS data_log
             (date date, event text, location text)''')

    name_request="SELECT name FROM name WHERE id= (%s)"
    location_request="SELECT location FROM location WHERE ip= (%s)"
    cur.execute(name_request,(id_badge,))
    name=(str(cur.fetchone())[2:-3])
    if name == "":
        name=id_badge

    cur.execute(location_request,(ip,))
    location=(str(cur.fetchone())[2:-3])

    request = "INSERT INTO data_log VALUES (%s,%s,%s)"
    data=[date,name,location]

    logging.info("request sent is "+request)
    cur.execute(request,data)
    conn.commit()
    conn.close()

    logging.info("fini")


def read_data_base(filename):
    conn = psycopg2.connect(filename)
    cur = conn.cursor()
    ip="192.168.20.90"

    cur.execute("SELECT location FROM location WHERE ip=(%s)",(ip,))

    test=(str(cur.fetchone())[2:-3])
    if test=="":
        print"rien"
    else:
        print test

    conn.close()


