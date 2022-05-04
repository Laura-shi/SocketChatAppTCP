
from ast import Num
from concurrent.futures import thread
from pydoc import cli
import socket
import threading
import string

client_list = []
nick_names = []
servername = '127.0.0.1'
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9999
server.bind((servername,port))
server.listen()

print(' *********the server is ready started********')
# send message from server to all connected clients
def send_msg(msg):
    for client in client_list:
        client.send(msg)

#connect client A to Client B
def connect_client(client):
    while True:
        try:
            msg = client.recv(1024)
            send_msg(msg)
        except:
            index = client_list.index(client)
            client_list.remove(client)
            client.close()
            nick_name =nick_names[index]
            send_msg(f'{nick_name} has left the chatting group!'.encode('utf-8'))
            nick_names.remove(nick_name)
            break

# main function to receive the clients connection
def receive():
    while True:
        print('**********server is running and listenting******')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('nick_name?'.encode('utf-8'))
        nick_name = client.recv(1024)
        nick_names.append(nick_name)
        client_list.append(client)
        print(f'the nick name of this client is {nick_name}'.encode('utf'))
        send_msg(f'{nick_name} has connected to chat!'.encode('utf-8'))
        print('\n-----------------------------------')
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target = connect_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()

