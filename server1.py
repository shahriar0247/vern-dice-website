import socket
from wsgiref.handlers import format_date_time
import time
from datetime import datetime
from urllib import response
from random import *

def randomizer():

    global list
    global throws
    global sixes
    global fives
    global fours
    global threes
    global twos
    global ones 

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


def render_html(filename):
  file_ = open(filename, "r")
  data = file_.read()
  file_.close()
  return data

def main():
  server = __init_socket()
  while True:
      client, addr = server.accept()
      response = send_response(render_html("index.html"))
      response = f"""
      <div>Amount of throws: {throws}</div>
      <div>Sixes: {sixes}</div>
      <div>Fives: {fives}</div>
      <div>Fours: {fours}</div>
      <div>Threes: {threes}</div>
      <div>Twos: {twos}</div>
      <div>Ones: {ones}</div>
      <input type="button" value="Calculate" onClick="window.location.reload(true)">
      """
      client.send((response).encode())

try:
  main()
except KeyboardInterrupt:
  print("Exiting")