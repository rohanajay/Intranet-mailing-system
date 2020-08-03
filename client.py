from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import login
import compose
import rcv 
import rd_wt

data = login.log()

HOST = '127.0.0.1'
PORT = 12000
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

def begin():
	client_socket.send(bytes(data[0].get(),"utf8"))

def receive(client_socket):
    """Handles receiving of messages."""
    while True:
        mess = client_socket.recv(BUFSIZ).decode("utf8")
                
        if(mess != ""):
            mess = mess.split("~")
            From = mess[3]
            Title = mess[1]
            Body = mess[2]
            rcv.r_mail(From,Title,Body)
        else:
            raise RuntimeError("End Of Conversation!!!")

def send(event=None):  # event is passed by binders.
    '''send mail to the server'''
    packet = imail[0]+"~"+imail[1]+"~"+imail[2]+"~"+data[0].get()
    client_socket.send(bytes(packet,"utf8"))

begin()
result = rd_wt.op()
if(result == "write"):
	imail = compose.mail()
	send()

receive_thread = Thread(target=receive,args=(client_socket,))
receive_thread.start()
