#Nod pentru lista dubla inlantuita:
class Nod:
    def __init__(self,val):
        self.val = val
        self.urm = None
        self.prev = None
#Lista Dubla inlantuita:
class ListaDubla:
    def __init__(self):
        self.inceput = None
        self.sfarsit = None
#Inserarea pentru lista dubla - pentru final

    def insert(self, val):
        if Nod is None:
            return Nod(val)

        nodul_nou = Nod(val)

        if self.inceput is None:
            self.inceput = nodul_nou
            self.sfarsit = nodul_nou
        else:
            self.sfarsit.urm = nodul_nou
            nodul_nou.prev = self.sfarsit
            self.sfarsit = nodul_nou

    def stergere(self, val):
        if Nod(val) is None:
            return Nod(val)
        val_curent = self.inceput
        if val_curent == val:
            if val_curent.prev is None:
                self.inceput = val_curent.urm
                if self.inceput:
                    self.inceput.prev = None

    def parcurgere_inainte(self):
        curent_val = self.inceput
        while curent_val:
            print(curent_val.val, end= " <--> "  if curent_val.urm else"")
            curent_val = curent_val.urm
        print()


    def parcurgere_inapoi(self):
        curent_val = self.sfarsit
        while curent_val:
            print(curent_val.val, end= " <--> " if curent_val.prev else"")
            curent_val = curent_val.prev
        print()


lista_dubla = ListaDubla()
lista_dubla.insert(1)
lista_dubla.insert(2)
lista_dubla.insert(3)

rezultat_inainte = lista_dubla.parcurgere_inainte()
rezultat_inapoi = lista_dubla.parcurgere_inapoi()
print(rezultat_inainte)
print(rezultat_inapoi)

lista_dubla.stergere(2)
rezultat_inainte_dupa_stergere = lista_dubla.parcurgere_inainte()
print(rezultat_inainte_dupa_stergere)
