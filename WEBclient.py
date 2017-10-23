# -*- coding: utf-8 -*-

import socket

arq = open('respServer.txt', 'w')

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

arg = raw_input('navegador ')

try:
	entrada = arg.split(' ')
	serverName = entrada[0]
	serverPort = int(entrada[1])
	
	# Conecta como cliente a um servidor selecionado utilizando a porta especificada 
	s.connect((serverName,serverPort))
	
except Exception as e:
	# Conecta como cliente a um servidor selecionado
	# utilizando a porta especificada 
	s.connect((arg,80))

print '\033[32m'+'\nConexao extabelecida...'+'\033[0;0m'

#arquivo = raw_input('nome do arquivo: ')
#cmd = 'GET ' + arquivo + ' HTTP/1.0\n\n'
#print cmd

# Protocol exchange - sends and receives
#s.send(cmd)
s.send('GET /index.html HTTP/1.0\n\n')

while True:
    resp = s.recv(1024)
    if resp == '': print 'vazio'#break

    #print resp
    print resp[0:12]
    status = resp[9:12]

    if status == '200': 
        print '\033[32m'+'Message: OK - The request is OK (this is the standard response for successful HTTP requests)'+'\033[0;0m'
    elif status == '301': 
        print '\033[31m'+'Message: Moved Permanently - The requested page has moved to a new URL'+'\033[0;0m'
    elif status == '400':
        print '\033[31m'+'Message: Bad Request - The request cannot be fulfilled due to bad syntax'+'\033[0;0m'
    elif status == '403':
        print '\033[31m'+'Message: Forbidden - The request was a legal request, but the server is refusing to respond to it'+'\033[0;0m'
    elif status == '404':
        print '\033[31m'+'Message: Not Found - The requested page could not be found but may be available again in the future'+'\033[0;0m'
    elif status == '500':
        print '\033[31m'+'Message: Internal Server Error - A generic error message, given when no more specific message is suitable'+'\033[0;0m'
    else:
        break

    break


# Close the connection when completed
s.close()
print "\nConexao finalizada."