
import NactiXML
import roztridData
import generujHtml

adresaXML = "axi01.oofem.in"
posledniIndexCyklu = 0

dataIn = NactiXML.XML(adresaXML)
poleRadku = dataIn.getPole()

souradniceVsechTrojuhelniku = []
trojuhelnikoveElementy = roztridData.data(poleRadku)
souradniceVsechTrojuhelniku = trojuhelnikoveElementy.getSouradniceVsechTrojuhelniku()

generujHtml.html(souradniceVsechTrojuhelniku)

print("")


