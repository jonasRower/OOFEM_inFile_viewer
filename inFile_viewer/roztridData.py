class data:

    def __init__(self, poleRadku):

        self.poleRadku = poleRadku
        self.polePrvnichSlov = []
        self.poleNode = []
        self.poleTr1supgaxi = []

        self.souradniceX = []
        self.souradniceY = []
        self.souradniceZ = []

        self.uzelElementu1 = []
        self.uzelElementu2 = []
        self.uzelElementu3 = []

        self.souradniceVsechTrojuhelniku = []


        self.vratPolePrvnichSlov()
        self.poleNode = self.vytvorPolePodlePrvnihoSlovaNaRadku("node")
        self.poleTr1supgaxi = self.vytvorPolePodlePrvnihoSlovaNaRadku("tr1supgaxi")

        self.souradniceX = self.vratPoleJednohoSLoupce(self.poleNode, 4)
        self.souradniceY = self.vratPoleJednohoSLoupce(self.poleNode, 5)
        self.souradniceZ = self.vratPoleJednohoSLoupce(self.poleNode, 6)

        self.uzelElementu1 = self.vratPoleJednohoSLoupce(self.poleTr1supgaxi, 4)
        self.uzelElementu2 = self.vratPoleJednohoSLoupce(self.poleTr1supgaxi, 5)
        self.uzelElementu3 = self.vratPoleJednohoSLoupce(self.poleTr1supgaxi, 6)

        self.sestavSouradniceTrojuhelnika()


    # vrati data
    def getSouradniceVsechTrojuhelniku(self):
        return(self.souradniceVsechTrojuhelniku)



    # vrat pole jejich polozky jsou prvnimi slovy z self.poleRadku
    def vratPolePrvnichSlov(self):


        for r in range(0, len(self.poleRadku)):

            radek = self.poleRadku[r]
            wordArr = radek.split()
            if(wordArr == []):
                prvniSlovoNaRadku = ""
            else:
                prvniSlovoNaRadku = wordArr[0]

            self.polePrvnichSlov.append(prvniSlovoNaRadku)



    # podle prvniho slova na radku vybere
    def vytvorPolePodlePrvnihoSlovaNaRadku(self, prvniSlovo):

        poleRadkuPodlePrvnihoSlova = []

        for r in range(0, len(self.polePrvnichSlov)):
            prvniSlovoPole = self.polePrvnichSlov[r]
            if(prvniSlovo == prvniSlovoPole):
                radek = self.poleRadku[r]
                poleRadkuPodlePrvnihoSlova.append(radek)

        return(poleRadkuPodlePrvnihoSlova)



    # vybere sloupec z pole radku - jedna se napr. o souradnici x nebo cokoliv jineho
    # vybira substring z pole radku, ktery je na dany pozici oddeleny mezerami
    def vratPoleJednohoSLoupce(self, poleRadku, pozice):

        sloupecPole = []


        for r in range(0, len(poleRadku)):
            radek = poleRadku[r]
            wordArr = radek.split()
            substring = wordArr[pozice]
            cislo = float(substring)

            sloupecPole.append(cislo)

        return(sloupecPole)


    # vytvori pole XYZ jako pole souradnic
    def vytvorPoleXYZ(self, index):
        x = self.souradniceX[int(index)-1]
        y = self.souradniceY[int(index)-1]
        z = self.souradniceZ[int(index)-1]

        poleXYZ = []
        poleXYZ.append(x)
        poleXYZ.append(y)
        poleXYZ.append(z)

        return(poleXYZ)


    # sestavi souradnice trojuhelnikoveho elementu
    def sestavSouradniceTrojuhelnika(self):

        for r in range(0, len(self.poleTr1supgaxi)):
            index1 = self.uzelElementu1[r]
            index2 = self.uzelElementu2[r]
            index3 = self.uzelElementu3[r]

            poleXYZ1 = self.vytvorPoleXYZ(index1)
            poleXYZ2 = self.vytvorPoleXYZ(index2)
            poleXYZ3 = self.vytvorPoleXYZ(index3)

            souradniceTrojUhelnika = []

            souradniceTrojUhelnika.append(poleXYZ1)
            souradniceTrojUhelnika.append(poleXYZ2)
            souradniceTrojUhelnika.append(poleXYZ3)

            self.souradniceVsechTrojuhelniku.append(souradniceTrojUhelnika)






