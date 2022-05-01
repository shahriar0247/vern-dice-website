import socket
from wsgiref.handlers import format_date_time
import main
import time
from datetime import datetime


sixes = str(main.sixes)
fives = str(main.fives)
fours = str(main.fours)
threes = str(main.threes)
twos = str(main.twos)
ones = str(main.ones)

server = socket.socket()        
print ("Socket successfully created")

port = 8080
host_ip = 'localhost'

server.bind(('', port))        
print ("socket binded to %s" %(port))

server.listen(500)    
print ("socket is listening")           

print ("Connected to the socket successfully ")

def send_response(html):
  now = datetime.now()
  date = str(format_date_time(time.mktime(now.timetuple())))
  response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nDate: "+date+"\r\nContent-Length: " + str(
                    len(html)) + "\r\n\r\n" + html
  return response

while True:

  c, addr = server.accept()    
  print ('Got connection from', addr )
  response = f"""
  <div>Sixes: {sixes}</div>
  <div>Fives: {fives}</div>
  <div>Fours: {fours}</div>
  <div>Threes: {threes}</div>
  <div>Twos: {twos}</div>
  <div>Ones: {ones}</div>

  <input type="button" value="Reload Page" onClick="window.location.reload(true)">
  """

  c.send(send_response(response).encode())