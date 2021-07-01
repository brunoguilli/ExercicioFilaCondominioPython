class Fila:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def filaDeEspera(self):

        no_atual = self.primeiro

        while no_atual is not None:
            print(no_atual.getNumero())
            no_atual = no_atual.proximo

    def insere(self, novo_dado):

        novo_nodo = novo_dado

        # Insere em uma fila vazia.
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def remove(self, vaga):

        assert self.primeiro != None, "Impossível remover elemento de fila vazia."

        self.primeiro.setVaga(vaga);

        self.primeiro = self.primeiro.proximo

        if self.primeiro == None:
            self.ultimo = None

class Torre:
    def __init__(self):
        self.id = 0
        self.nome = None
        self.endereco = None

    def getNome(self):
        return self.nome;

    def getEndereco(self):
        return self.endereco;

    def cadastrar(self,id, nome, endereco):
        self.id = id;
        self.nome = nome;
        self.endereco = endereco;

    def imprimir(self):
        print("Id: ", self.id)
        print("Nome: ", self.nome)
        print("Endereco: ", self.endereco)

class Apartamento:
    def __init__(self):
        self.id = None
        self.numero = None
        self.torre = None
        self.vaga = None
        self.proximo = None

    def getId(self):
        return self.id;

    def getNumero(self):
        return self.numero;

    def getTorre(self):
        return self.torre;

    def getVaga(self):
        return self.vaga;

    def setVaga(self, vaga):
        self.vaga = vaga;

    def getProximo(self):
        return self.proximo;

    def cadastrar(self,id, numero, torre):
        self.id = id;
        self.numero = numero;
        self.torre = torre

    def imprimir(self):
        print("Id: ", self.id)
        print("Numero: ", self.numero)
        print("Vaga: ",self.vaga)
        print("Torre: ", self.torre.getNome())
        print("Proximo: ", self.proximo)


torre1 = Torre()
torre1.cadastrar(1,"Torre A","Av Ipiranga")

torre2 = Torre()
torre2.cadastrar(1,"Torre B","Av Ipiranga")

apto1 = Apartamento();
apto1.cadastrar(1,1208,torre1)

apto2 = Apartamento();
apto2.cadastrar(2,1209,torre1)

apto3 = Apartamento();
apto3.cadastrar(3,1210,torre2)

apto4 = Apartamento();
apto4.cadastrar(4,1220,torre2)

fila = Fila()

fila.insere(apto1)
fila.insere(apto2)
fila.insere(apto3)
fila.insere(apto4)

fila.remove(666)

fila.filaDeEspera()



