def jogo(jogador_1, jogador_2):
        
        if jogador_1 == jogador_2:
                return "0"
        elif jogador_1 == "3" and jogador_2 == "2":
                return "1"

        elif jogador_1 == "2" and jogador_2 == "1":
                return "1"

        elif jogador_1 == "1" and jogador_2 == "4":
                return "1"

        elif jogador_1 == "1" and jogador_2 == "5":
                return "1"

        elif jogador_1 == "5" and jogador_2 == "3":
                return "1"

        elif jogador_1 == "3" and jogador_2 == "4":
                return "1"

        elif jogador_1 == "3" and jogador_2 == "4":
                return "1"

        elif jogador_1 == "4" and jogador_2 == "2":
                return "1"

        elif jogador_1 == "2" and jogador_2 == "5":
                return "1"

        elif jogador_1 == "5" and jogador_2 == "1":
                return "1"

        elif jogador_1 == "1" and jogador_2 == "3":
                return "1"

        elif jogador_2 == "600":
                return "1"

        elif jogador_1 == "600":
                return "2"

        else:
                return "2"


def login_de_usuario(login):
    separador = "!@#$%&*()-+="
    arquivo = open("base_de_dados.txt", "r");
    base_de_dados = arquivo.read();
    arquivo.close();
    x = 0
    base_de_dados = base_de_dados.split("\n");
    for item in base_de_dados:
        if login == item:
            x = 1;
            break;
        
            
    if x == 1:
        return "1";
    else:
        return "0";
             
def cadastro_de_usuario(login):
    separador = "!@#$%&*()-+="
    arquivo = open("base_de_dados.txt", "r");
    base_de_dados = arquivo.read();
    arquivo.close();
    x = 0;
    login = login.split(separador);
    base_de_dados_temp = base_de_dados.split("\n");
    for item in base_de_dados_temp:
        temp = item.split(" ");
        if login[0] == temp[0]:
            x = 1;
            break;   
            
    if x == 0:
        base_de_dados = base_de_dados + "\n" + str(login[0]) + " " + str(login[1]);
        arquivo = open("base_de_dados.txt", "w");
        arquivo.write(base_de_dados);
        arquivo.close();
        ####################
        arquivo = open("pontuacoes.txt", "r");
        pontuacoes = arquivo.read();
        arquivo.close();
        pontuacoes = pontuacoes + "\n" + str(login[0]) + " 0";
        arquivo = open("pontuacoes.txt", "w");
        arquivo.write(pontuacoes);
        arquivo.close();
        return "1";
    else:
        return "0";

def computador():
        import random
        return str(random.randint(1,5))

def aleatorio():
        import random
        return str(random.randint(100,999))

def art():
        x = '''
 _____________________________   
/        _____________        \  
| == .  |             |     o |  
|   _   |  SISCOMP    |    B  |  
|  / \  |             | A   O |  
| | O | |  TRABALHO   |  O    |  
|  \_/  |   FINAL     |       |  
|       |             | . . . |  
|  :::  |             | . . . |  
|  :::  |_____________| . . . |  
|           S N K             |  
\_____________________________/
''';
        y = '''
      _____
     |.---.|
     ||___||
     |+  .'|
     | _ _ |
     |_____/''';

        return x

def usuarios_online(usuarios):
        string1 = '''
''';

        string2 = '''
INSTRUÇÕES:
                   Sair -> Digite 'Ctrl' + 'c' a qualquer momento desde que esteja fora de um jogo
              Atualizar -> Digite '1'
       Convidar jogador -> Digite '2' e aperte: "ENTER"
                           Depois, digite (exatamente) o nome do jogador que deseja convidar
         Negar convites -> Digite '3' aperte "ENTER"
                           e depois digite o nome do jogador a ser negado
       Aceitar convites -> Digite '4' aperte "ENTER"
                          e depois digite o nome do jogador desejado.
                          O jogo vai começar em seguida.
========================

''';
        #usuarios_online = organizar(usuarios);
        retorno = string1 + usuarios + string2;
        return retorno
        
def placar(vencedor, flag):
        arquivo = open("pontuacoes.txt", "r");
        pontuacoes = arquivo.read();
        arquivo.close();

        pontuacoes = pontuacoes.split("\n")

        i = 0;
        while i < len(pontuacoes):
                jogador = pontuacoes[i].split(" ")
                if jogador[0] == vencedor:
                        temp = int(jogador[1])

                        if flag == 1:
                                temp = temp + 1
                        else:
                                temp = temp - 1

                        temp = vencedor + " " + str(temp)
                        #print(temp)
                        pontuacoes[i] = str(temp)
                        break
                        #print(pontuacoes[i])

                i = i + 1

        #print(pontuacoes)
        pontuacoes = "\n".join(pontuacoes)
        arquivo = open("pontuacoes.txt", "w");
        pontuacoes = arquivo.write(pontuacoes);
        arquivo.close();

        if flag == 1:
                return str(temp);
        else:
                x = 1;

def pontuacao(usuario):
        arquivo = open("pontuacoes.txt", "r");
        pontuacoes = arquivo.read();
        arquivo.close();

        pontuacoes = pontuacoes.split("\n")

        i = 0;
        while i < len(pontuacoes):
                jogador = pontuacoes[i].split(" ")
                if jogador[0] == usuario:
                        temp = int(jogador[1])
                        break;

                i = i + 1

        return temp


#def organizar(dicionario):
#        import operator
#        ordenada = sorted(dicionario.items(), key=operator.itemgetter(1))
#        temp = ""
#        i = 0
#        while i < len(dicionario):
#                temp = temp + str(ordenada[i][0]) + " - " + str(ordenada[i][1]) + "\n"
#                i = i + 1

#        return temp

def ler_convites():
        arquivo = open("convites.txt", "r");
        convites = arquivo.read();
        arquivo.close();
        return convites;


def texto_do_jogo():
        texto = '''
        ==========Digite sua jogada================

                        PEDRA - 1
                        PAPEL - 2
                        TESOURA - 3
                        LIZARD - 4
                        SPOCK - 5

        ===========================================
        ''';

        return texto

def organizar(usuarios):
        #print(usuarios);
        users = [];
        score = [];
        temporario = usuarios.split("\n");
        #print("oi")

        for item in temporario:
                #print(item);
                if item == "":
                        batatas_existem = True;

                else:
                        temp = item.split(" - ");
                        users.append(temp[0]);
                        score.append(temp[1]);
                        #print(i)

        i = 0;

        while i < len(score):
                score[i] = int(score[i]);
                i = i + 1;

        usuarios_online = "\n"

        while len(score) != 0:
                i = 0;
                maior = 0;
                posicao = 0;
                while i < len(score):
                        if maior < score[i]:
                                maior = score[i];
                                posicao = i;
                        i = i + 1;

                #print(maior, posicao)
                usuarios_online = usuarios_online + str(users[posicao]) + " - " + str(maior) + "\n";
                #print(usuarios_online);

                del score[posicao];
                del users[posicao];

        return usuarios_online
                #print(users)
                #print("-------")
        
        #users = [];
        #score = [];
        #temporario = usuarios.split("\n");
        #for item in temporario:
        #        if item == []:
        #                batatas_existem = True;

        #        else:
        #                temp = item.split(" - ");
        #                users.append(temp[0]);
        #                score.append(temp[1]);
        #                #print(i)
        #i = 0;
        #while i < len(score):
        #        score[i] = int(score[i]);
        #        i = i + 1;

        


