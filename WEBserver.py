# -*- coding: utf-8 -*-

# -- exemplo WebServer --
import socket

def conectado(con, cliente):
        print 'Conectado com', cliente[0], 'na porta', cliente[1], '...'

        while True:
                # Recebe até 1024 bytes
                resp = (con.recv(1024)).strip()

                # Interrompe caso um usuário envie "SHUTDOWN"
                if not resp: break

                arq.write(resp)
                arq.close()
                
                # Envia uma resposta
                #connect.send("You said '" + resp + "' to me\n")
                con.send(arq)

                # Fecha o socket quando termina uma conexão
                #con.close()

                # Permanece no loop aguardando outro cliente
            
        print 'Finalizando conexao do cliente', cliente
        con.close()
        thread.exit()

# Estabelece um socket TCP/IP --> AF_NET == IP, SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print '\033[32m'+'\nServidor ativo. Aguardando conexão...'+'\033[0;0m'

# Vincula à porta TCP No. 17642 ...
s.bind(('',17642))

# ... e realiza a escuta para que alguém entre em contato usando
# uma fila com até 5 conexões
#s.listen(5)
s.listen(1)

while True:
    # Espera por uma conexão
    con, cliente = s.accept()
    print 'con', con
    print 'cliente', cliente
    thread.start_new_thread(conectado, tuple([con, cliente]))