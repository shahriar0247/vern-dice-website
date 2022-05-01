import socket
from wsgiref.handlers import format_date_time
import time
from datetime import datetime
from urllib import response
from random import *

def randomizer():

    list = []
    throws = 100
    sixes = 0
    fives = 0
    fours = 0
    threes = 0
    twos = 0
    ones = 0

    for i in range(throws):
        list.append(randint(1,6))
 
    for i in list:
        if i == 6:
            sixes += 1

    for i in list:
        if i == 5:
            fives += 1

    for i in list:
        if i == 4:
            fours += 1

    for i in list:
        if i == 3:
            threes += 1

    for i in list:
        if i == 2:
            twos += 1

    for i in list:
        if i == 1:
            ones += 1
    return throws, sixes, fives, fours, threes, twos, ones

def __init_socket():
    port = 8080
    server = socket.socket()
    server.bind(('', port))
    server.listen(5)
    print("Listening: http://localhost:" + str(port))
    return server


def send_response(html):
    now = datetime.now()
    date = str(format_date_time(time.mktime(now.timetuple())))
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nDate: "+date+"\r\nContent-Length: " + str(
        len(html)) + "\r\n\r\n" + html
    return response


def render_html(filename, json: dict):
  file_ = open(filename, "r")
  data = file_.read()
  for a in json.keys():
      data = data.replace("{{" + str(a) + "}}", str(json[a]))
  file_.close()
  return data

def main():
  server = __init_socket()
  while True:
    client, addr = server.accept()
    throws, sixes, fives, fours, threes, twos, ones = randomizer()
    response = send_response(render_html("index.html", {'hello': "hi", "throws": throws,"sixes": sixes, "fives": fives, "fours": fours, "threes": threes, "twos": twos, "ones": ones }))
    
    client.send((response).encode())

try:
  main()
except KeyboardInterrupt:
  print("Exiting")