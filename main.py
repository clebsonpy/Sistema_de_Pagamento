from empregado import Empregado

if __name__ == "__main__":
    e1 = Empregado("Clebson", "Rua Carvalho", "Horista", 18)
    e1.save()
    e2 = Empregado("Clara", "Rua 2", "Assalariado", 2500)
    e2.save()

    print(Empregado.all())
