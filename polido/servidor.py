from socket import *
from threading import *
from _thread import *
import time
#from datetime import datetime
import siscomp

def thread_convites(connection_1, i):
    #global usuarios_online
    global convites

    while True:
        try:
            recebido = connection_1.recv(2048);
            recebido = recebido.decode('utf-8');
            usuario = recebido;

            temp = str(convites[usuario]);
            connection_1.send(str.encode(temp));

        except Exception as e:
            print(e);
            print("Fechando conexão");
            break;
        
    connection_1.close();
    


def threaded_client(connection, i):
    global usuarios_online
    global convites
    global partidas
    separador = "!@#$%&*()-+="
    zeta = 0;
    usuario = "";

    while True:
        try:
            recebido = connection.recv(2048);
            if not recebido:
                raise Exception("Socket fechado");
            
            recebido = recebido.decode('utf-8');

            #cadastrando usuário novo
            if recebido == "050":
                connection.send(str.encode("Ok"));

                #recebe usuario e senha
                recebido = connection.recv(2048);
                recebido = recebido.decode('utf-8');

                obj.acquire() #<----semáforo
                result = siscomp.cadastro_de_usuario(recebido);
                obj.release()#<----semáforo

                if result == "1":
                    connection.sendall(str.encode("========\nVocê foi cadastrado!\n========"));
                    
                else:
                    connection.sendall(str.encode("========\nEsse nome já está em uso! Tente outro\n========"));

            elif recebido == "100":
                #inicalização
                connection.send(str.encode("Ok"));
                recebido = connection.recv(2048);
                recebido = recebido.decode('utf-8');

                temp = recebido.split(" ")

                #teste para ver se tem login
                if temp[0] in usuarios_online:
                    result = "online"

                else:
                    result = siscomp.login_de_usuario(recebido);

                #enviando resposta de login
                if result == "0":
                    connection.send(str.encode("600"));#

                elif result == "online":#
                    connection.send(str.encode("700"));#

                else:
                    #processo de montar a mensagem de boas vindas                  
                    connection.send(str.encode("1"));
                    usuario = recebido.split(" ");
                    usuario = usuario[0];
                    usuarios_online.append(usuario);
                    convites[usuario] = [];                    

                    recebido = connection.recv(2048);
                    ###MONTANDO MENSAGEM DE RESPOSTA PARA O CLIENTE
                    temp = "\n"
                    for i in usuarios_online:
                        score = siscomp.pontuacao(i)
                        temp = temp + str(i) + " - " + str(score) + "\n"

                    connection.send(str.encode(temp));

                    recebido = connection.recv(2048);

                    temp = str(convites[usuario]);
                    connection.send(str.encode(temp));
                    

            elif recebido == "150":
                recebido = connection.recv(2048);
                temp = "\n"
                for i in usuarios_online:
                    score = siscomp.pontuacao(i)
                    temp = temp + str(i) + " - " + str(score) + "\n"

                connection.send(str.encode(temp));
                recebido = connection.recv(2048);

                temp = str(convites[usuario]);
                connection.send(str.encode(temp));

            elif recebido == "200":
                #SISTEMA DE CONVITES
                connection.send(str.encode("1"));
                
                recebido = connection.recv(2048);
                recebido = recebido.decode('utf-8');

                if recebido not in usuarios_online:#
                    connection.send(str.encode("450"));
                    
                else:#
                    convites[recebido].append(usuario);
                    ##SISTEMA DE CONVITES

                    anfitriao = usuario; #
                    convidado = recebido

                    partidas[anfitriao + " " + convidado] = 0;

                    while partidas[anfitriao + " " + convidado] == 0:
                        time.sleep(0.1);
                        if recebido not in usuarios_online:#
                            partidas[anfitriao + " " + convidado] = 120;#

                    if partidas[anfitriao + " " + convidado] == 1:
                        connection.send(str.encode("0"));

                    elif partidas[anfitriao + " " + convidado] == 120:
                        connection.send(str.encode("850"));

                    else:
                        connection.send(str.encode("1"));

                        recebido = connection.recv(2048);
                        recebido = recebido.decode('utf-8');

                        partidas[anfitriao + " " + convidado] = str(partidas[anfitriao + " " + convidado]) + " " + recebido;

                        timer = time.time();
                        while len(partidas[anfitriao + " " + convidado].split(" ")) == 2:
                            if time.time() < timer + 30:
                                time.sleep(0.1);
                            else:
                                timer = "0";
                                partidas[anfitriao + " " + convidado] = str(partidas[anfitriao + " " + convidado]) + " !600!";#
                                break

                        
                        connection.send(str.encode(partidas[anfitriao + " " + convidado]));

                        recebido = connection.recv(2048);
                        recebido = recebido.decode('utf-8');

                        if recebido == "900":#
                            batatas_existem = True;#

                        else:#
                            obj_placar.acquire()
                            if recebido == "1":
                                siscomp.placar(usuario, 1)
                                
                            elif recebido == "2":
                                siscomp.placar(usuario, 2)

                            else:
                                batatas_existem = True;

                            obj_placar.release()

                        connection.send(str.encode("0"));
                
                
            elif recebido == "250":
                #SISTEMA DE CONVITES
                connection.send(str.encode("ok"));

                recebido = connection.recv(2048);
                recebido = recebido.decode('utf-8');

                anfitriao = recebido;
                convidado = usuario;

                if recebido in convites[usuario]:
                    convites[usuario].remove(recebido);
                    partidas[anfitriao + " " + convidado] = 1;
                    time.sleep(0.3);
                    partidas.pop(anfitriao + " " + convidado);
                    connection.send(str.encode("1"));
                    
                else:
                    connection.send(str.encode("0"));

            elif recebido == "300":
                connection.send(str.encode("ok"));

                recebido = connection.recv(2048);
                recebido = recebido.decode('utf-8');

                connection.send(str.encode("ok"));

                anfitriao = recebido;
                convidado = usuario;

                convites[convidado].remove(anfitriao);####<---

                partidas[anfitriao + " " + convidado] = 2;

                recebido = connection.recv(2048);
                recebido = recebido.decode('utf-8');

                partidas[anfitriao + " " + convidado] = str(partidas[anfitriao + " " + convidado]) + " " + recebido

                timer = time.time();
                while len(partidas[anfitriao + " " + convidado].split(" ")) == 2:
                    if time.time() < timer + 30:
                        time.sleep(0.1);

                    else:
                        partidas[anfitriao + " " + convidado] = str(partidas[anfitriao + " " + convidado]) + " ?600?";#
                        timer = "0";
                        break

                connection.send(str.encode(partidas[anfitriao + " " + convidado]));

                recebido = connection.recv(2048);
                recebido = recebido.decode('utf-8');

                if recebido == "900":#
                    batatas_existem = True;#

                else:
                    obj_placar.acquire()
                    if recebido == "1":
                        siscomp.placar(usuario, 1)

                    elif recebido == "2":
                        siscomp.placar(usuario, 2)

                    else:
                        batatas_existem = True;

                    obj_placar.release()

                connection.send(str.encode("0"));              
                
            
            else:
                batatas_existem = True;
                


        except Exception as e:
            obj_tela.acquire()
            print(e);
            print("Fechando conexão");
            obj_tela.release()
            break;

    if usuario  != "":
        usuarios_online.remove(usuario);
        convites.pop(usuario);
        for item in convites:
            if usuario in convites[item]:
                convites[item].remove(usuario)
        
    connection.close();


############
ServerSocket = socket(AF_INET, SOCK_STREAM);
ServerSocket_1 = socket(AF_INET, SOCK_STREAM);
host = ''
port = 12000
port_1 = 13000#
ThreadCount = 0
ThreadCount_1 = 0
obj = Semaphore(1)
obj_tela = Semaphore(1)
obj_placar = Semaphore(1)
usuarios_online = []
partidas = {}
convites = {}

try:
    ServerSocket.bind((host, port))
    ServerSocket_1.bind((host, port_1))#
    
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(1)
ServerSocket_1.listen(1)

while True:
    Client, address = ServerSocket.accept()
    Client_1, address_1 = ServerSocket_1.accept()#
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    ThreadCount += 1;
    ThreadCount_1 += 1;
    start_new_thread(threaded_client, (Client, ThreadCount))
    start_new_thread(thread_convites, (Client_1, ThreadCount_1))
    print('Thread Number: ' + str(ThreadCount))
    
ServerSocket.close()
        

