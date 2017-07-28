import random

class Empregado():

    seq = 0
    objects = []
    ids = []

    def __init__(self, nome, endereco, tipo, salario, comissao = None):
        self.nome = nome
        self.endereco = endereco
        self.tipo = tipo
        self.salario = salario
        self.comissao = comissao
        self.id = self.gerarId()

    def gerarId(self):
        idx = random.randint(1000, 10000)
        while idx in self.__class__.ids:
            idx = random.randint(100, 1000)

        return idx

    def save(self):
        self.__class__.seq += 1
        self.idc = self.__class__.seq
        self.__class__.objects.append(self)
        self.__class__.ids.append(self.id)

    def remove(self, idx):
        for n in self.__class__.objects
            ido = n.id
            i = self.__class__.objects[n]
            if idx == ido:
                self.__class__.objects.remove(i)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "<ID: {}\n\
        Nome: {}\n\
        Endereço: {}\n\
        Tipo: {}\n\
        Salário: {}\n\
        Comissão: {}>\n".format(self.id, self.nome,
                                self.endereco, self.tipo,
                                self.salario, self.comissao)

    @classmethod
    def all(cls):
        return cls.objects
