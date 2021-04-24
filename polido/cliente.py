from socket import *;
from threading import *
from _thread import *
import time
import siscomp


def thread_convites(x, y):
    global morte
    global usuario
    global zeta
    global convites
    bserverName = '192.168.0.113';
    bserverPort_1 = 13000;
    clientSocket_1 = socket(AF_INET, SOCK_STREAM);#
    clientSocket_1.connect((bserverName, bserverPort_1));

    while morte == False:
        try:
            if zeta == 1:
                    msg = bytes(usuario, 'utf-8');
                    clientSocket_1.send(msg);

                    recebido = clientSocket_1.recv(2048);
                    convites = recebido.decode('utf-8');
                    
                    time.sleep(0.1);

                    if convites != "[]":
                            print("Você tem convites!\n" + str(convites) + " \nDigite '1' para atualizar a página corretamente\n -->");
                            zeta = 0;
                            

            

        except Exception as e:
            print(e);
            print("Fechando conexão");
            break;
        
    clientSocket_1.close();



####CÓDIGO PRINCIPAL

bserverName = '192.168.0.113';
bserverPort = 12000;

clientSocket = socket(AF_INET, SOCK_STREAM);

clientSocket.connect((bserverName, bserverPort));

start_new_thread(thread_convites, ("1", "1"));

zeta = 0;
zeta1 = 1;
morte = False
separador = "!@#$%&*()-+="
convites = "";

while True:
        try:
                ##inicialização
                print("Olá, bem vindo ao...");
                print(siscomp.art());
                print("===PEDRA===PAPEL===TESOURA===LAGARTO===SPOCK");
                print("Antes de mais nada, precisamos saber, você já está cadastrado?");
                resposta = input("Digite 'S' para sim e 'N' para não:\n");
                resposta = resposta.lower();

                if resposta == "s":
                        #enviando mensagem especificando o que quero fazer
                        msg = bytes("100", 'utf-8');
                        clientSocket.send(msg);
                        recebido = clientSocket.recv(2048);

                        #efetivamente fazer login
                        usuario = input("Insira seu usuário: ");
                        senha = input("Insira sua senha: ");

                        x = usuario + " " + senha;
                        msg = bytes(x, 'utf-8');
                        clientSocket.send(msg);

                        recebido = clientSocket.recv(2048);
                        recebido = recebido.decode('utf-8');

                        if recebido == "600":#
                                print("=====\nSeu usuário ou senha estão errados.\nPorfavor, tente de novo\n=======");

                        elif recebido == "700":#
                                print("=====\nEsse usuário já está online.\n=======");#

                        else:
                                zeta = 1
                                print("=====\nBem vindo, " + usuario + "!\n=======");
                                
                                while True:
                                        #processo de montar a mensagem de boas vindas
                                        msg = bytes("1", 'utf-8');
                                        clientSocket.send(msg);

                                        recebido = clientSocket.recv(2048);
                                        recebido = recebido.decode('utf-8');
                                        usuarios_online = recebido;###

                                        temp = siscomp.organizar(recebido)

                                        temp = "=====Usuários online!====" + temp;
                                        msg = bytes("1", 'utf-8');
                                        clientSocket.send(msg);

                                        recebido = clientSocket.recv(2048);
                                        recebido = recebido.decode('utf-8');
                                        convites = recebido;

                                        temp = temp + "\n=======Você recebeu convites de:\n" + str(recebido) + "\n======";
                                        temp = siscomp.usuarios_online(temp);
                                        print(temp);

                                        ##seleção do usuário
                                        acao = input("--> ");

                                        if acao == "1":
                                                msg = bytes("150", 'utf-8');
                                                clientSocket.send(msg);

                                        elif acao == "2":
                                                if convites == "[]":
                                                        jogador = input("--> ");
                                                        if jogador == usuario:
                                                                print("========\nDesculpe, mas você não pode inicar um jogo consigo mesmo\n=======")
                                                                msg = bytes("150", 'utf-8');
                                                                clientSocket.send(msg);
                                                                zeta = 1;

                                                        elif jogador == "":
                                                                print("========\nDesculpe, mas você digitou algo errado!\n=======")
                                                                msg = bytes("150", 'utf-8');
                                                                clientSocket.send(msg);
                                                                zeta = 1;

                                                        elif convites != "[]":
                                                                print("========\nVocê não pode convidar ninguém, você ainda tem convites pendentes!\n=======");
                                                                msg = bytes("150", 'utf-8');
                                                                clientSocket.send(msg);

                                                        else:
                                                                print("========\nConvite enviado! Esperando resposta\n=======")
                                                                msg = bytes("200", 'utf-8');
                                                                clientSocket.send(msg);

                                                                recebido = clientSocket.recv(2048);

                                                                msg = bytes(jogador, 'utf-8');
                                                                clientSocket.send(msg);

                                                                recebido = clientSocket.recv(2048);
                                                                recebido = recebido.decode('utf-8');

                                                                if recebido == "0":
                                                                        print("========\nDesculpe, mas seu convite foi negado!\n========")
                                                                        msg = bytes("150", 'utf-8');
                                                                        clientSocket.send(msg);

                                                                elif recebido == "450":
                                                                        print("========\nO usuário que você digitou não está online, ou está digitado incorretamente!\n========");
                                                                        msg = bytes("150", 'utf-8');
                                                                        clientSocket.send(msg);
                                                                        
                                                                elif recebido == "850":
                                                                        print("========\nO usuário que você convidou não está mais online, tente outro!\n========");
                                                                        msg = bytes("150", 'utf-8');
                                                                        clientSocket.send(msg);
                                                                        
                                                                else:
                                                                        temp = siscomp.texto_do_jogo();
                                                                        print(temp);
                                                                        jogadas_aceitas = ["1", "2", "3", "4", "5"];
                                                                        x = 0;
                                                                        while x == 0:
                                                                                jogada = input("Digite o número da sua jogada!\n---> ");
                                                                                if jogada in jogadas_aceitas:
                                                                                        jogada = "?" + jogada + "?"
                                                                                        x = 1;
                                                                                        #jogador = input("--> ");
                                                                                        #?2?  ?3? <-- exemplos
                                                                                else:
                                                                                        print("Desculpe, essa jogada é inválida\nTente novamente!\n ");
                                                                        
                                                                        msg = bytes(jogada, 'utf-8');
                                                                        clientSocket.send(msg);

                                                                        recebido = clientSocket.recv(2048);
                                                                        recebido = recebido.decode('utf-8');

                                                                        jogador_1 = recebido.split("?");
                                                                        jogador_1 = jogador_1[1];

                                                                        online_posicao = recebido.find("!")#

                                                                        if online_posicao == -1:#
                                                                            print("=======\n Desculpe, mas parece que seu oponente se desconectou antes de jogar\n=======");
                                                                            msg = bytes("900", 'utf-8');

                                                                        else:#                                                                                
                                                                            jogador_2 = recebido.split("!");
                                                                            jogador_2 = jogador_2[1];

                                                                            result = siscomp.jogo(jogador_1, jogador_2);                                                                                           

                                                                            if result == "0":
                                                                                    print("======\nEmpate!\n======");
                                                                                    msg = bytes("0", 'utf-8');

                                                                            elif result == "1":
                                                                                    print("======\nVocê venceu!\n======");
                                                                                    msg = bytes("1", 'utf-8');

                                                                            else:
                                                                                    print("======\nVocê perdeu!\n======")
                                                                                    msg = bytes("2", 'utf-8');

                                                                        clientSocket.send(msg);
                                                                            
                                                                        recebido = clientSocket.recv(2048);
                                                                        

                                                                msg = bytes("150", 'utf-8');
                                                                clientSocket.send(msg);

                                                                zeta = 1;

                                                else:
                                                        print("========\nVocê não pode convidar ninguém, você ainda tem convites pendentes!\n=======");
                                                        msg = bytes("150", 'utf-8');
                                                        clientSocket.send(msg);

                                        elif acao == "3":
                                                if convites == "[]":
                                                        print("========\nDesculpe, mas houve um erro. Não há convites para você!\n========");
                                                        msg = bytes("150", 'utf-8');
                                                        clientSocket.send(msg);

                                                else:
                                                        jogador = input("--> ");
                                                        msg = bytes("250", 'utf-8');
                                                        clientSocket.send(msg);

                                                        recebido = clientSocket.recv(2048);

                                                        msg = bytes(jogador, 'utf-8');
                                                        clientSocket.send(msg);

                                                        recebido = clientSocket.recv(2048);
                                                        recebido = recebido.decode('utf-8');

                                                        if recebido == "1":
                                                                print("========\nConvite Negado\n========");

                                                        else:
                                                                print("========\nDesculpe, mas eu acho que você digitou o nome errado\n========");

                                                        msg = bytes("150", 'utf-8');
                                                        clientSocket.send(msg);

                                                zeta = 1;
                                                
                                        elif acao == "4":
                                                jogador = input("--> ");
                                                if jogador not in (str(convites)).split("'"):
                                                #if jogador not in usuarios_online_1:
                                                    print("=======\nDesculpe, mas esse nome não aparece na lista de convites!\nVerifique se você  digitou algo errado!\n=====");
                                                    msg = bytes("150", 'utf-8');
                                                    clientSocket.send(msg);

                                                else:
                                                    msg = bytes("300", 'utf-8');
                                                    clientSocket.send(msg);

                                                    recebido = clientSocket.recv(2048);

                                                    msg = bytes(jogador, 'utf-8');
                                                    clientSocket.send(msg);

                                                    recebido = clientSocket.recv(2048);
                                                    recebido = recebido.decode('utf-8');

                                                    temp = siscomp.texto_do_jogo();
                                                    print(temp);
                                                    jogadas_aceitas = ["1", "2", "3", "4", "5"];
                                                    x = 0;
                                                    while x == 0:
                                                            jogada = input("Digite o número da sua jogada!\n---> ");
                                                            if jogada in jogadas_aceitas:
                                                                    jogada = "!" + jogada + "!";
                                                                    x = 1;
                                                                    #jogador = input("--> ");
                                                                    #!2!  !3! <-- exemplos
                                                            else:
                                                                    print("Desculpe, essa jogada é inválida\nTente novamente!\n ");

                                                    msg = bytes(jogada, 'utf-8');
                                                    clientSocket.send(msg);

                                                    recebido = clientSocket.recv(2048);
                                                    recebido = recebido.decode('utf-8');

                                                    jogador_1 = recebido.split("!");
                                                    jogador_1 = jogador_1[1];
                                                    
                                                    online_posicao = recebido.find("?")#

                                                    if online_posicao == -1:#
                                                        print("=======\n Desculpe, mas parece que seu oponente se desconectou antes de jogar\n=======");
                                                        msg = bytes("900", 'utf-8');

                                                    else:
                                                        jogador_2 = recebido.split("?");
                                                        jogador_2 = jogador_2[1];

                                                        result = siscomp.jogo(jogador_1, jogador_2);

                                                        if result == "0":
                                                                print("======\nEmpate!\n======");
                                                                msg = bytes("0", 'utf-8');

                                                        elif result == "1":
                                                                print("======\nVocê venceu!\n======");
                                                                msg = bytes("1", 'utf-8');

                                                        else:
                                                                print("======\nVocê perdeu!\n======")
                                                                msg = bytes("2", 'utf-8');

                                                    clientSocket.send(msg);

                                                    recebido = clientSocket.recv(2048);
                                                    
                                                    msg = bytes("150", 'utf-8');
                                                    clientSocket.send(msg);

                                                    zeta = 1;                                                

                                        else:
                                                print("=========\nOpção inválida\n=========");
                                                msg = bytes("150", 'utf-8');
                                                clientSocket.send(msg);
                                        
                        

                #cadastro de usuário
                elif resposta == "n":
                        #enviando mensagem especificando o que quero fazer
                        msg = bytes("050", 'utf-8');
                        clientSocket.send(msg);
                        recebido = clientSocket.recv(2048);
                        print("=========================\nDeseja se cadastrar?\nSe sim, preencha os campos abaixo!")
                        usuario = input("Digite o seu nome de usuario desejado: ");
                        senha = input("Digite a senha desejada: ");
                        x = usuario + separador + senha;
                        msg = bytes(x, 'utf-8');
                        clientSocket.send(msg);
                        #recebendo resposta do servidor
                        recebido = clientSocket.recv(2048);
                        recebido = recebido.decode('utf-8');
                        print(recebido);

                #usuário digitou algo errado                                
                else:
                        print("================\nDesculpe, você digitou algo errado.\nPor favor, tente novamente\n================");


        except (KeyboardInterrupt):
                print("=============\nFechando conexão! Até logo!\n============")
                clientSocket.close();
                break;
        
        except Exception as e:
                print(e)
                print("Fim de conexão");
                clientSocket.close();
                break;
