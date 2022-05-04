
from http import server
from ipaddress import ip_address
import socket,threading
from unicodedata import name


nick_name = input('choose an nick name >>:')

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servername = '127.0.0.1'
port = 9999
client.connect((servername,port))


# connected client receive messages from server
def client_receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "nick_name?":
                client.send(nick_name.encode('utf-8'))
            else: 
                print(msg)
        except:
            print('***error!***')
            client.close()
            break
# send message from connected successfully client to server
def client_send():
    while True:
        msg = f'{nick_name}:{input("")}'
        client.send(msg.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()     

