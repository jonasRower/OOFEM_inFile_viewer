
class html:

    def __init__(self, souradniceVsechTrojuhelniku):

        self.souradniceVsechTrojuhelniku = souradniceVsechTrojuhelniku

        # zde se nastavuji meritka
        self.Mx = 50
        self.My = 50

        self.poleHtml = []
        self.poleScript = []
        self.poleScriptCary = []
        self.poleScriptCaryVsechTrojuhelniku = []
        self.nazevSouboru = "schemaStruct.html"

        #zapise vsechny data vsech trojuhelniku do scriptu
        self.poleScriptCaryVsechTrojuhelniku = self.vratSriptProVykresleniVsechTrojuhelniku()

        #prida ke skriptu se souradnicemi i ostatni radky script
        self.poleScript = self.vytvorPoleScript(self.poleScriptCaryVsechTrojuhelniku)
        self.poleHtml = self.vytvorHtmlPole(self.poleScript)
        self.zapisHtml(self.poleHtml)


        print("")


    def vratSriptProVykresleniVsechTrojuhelniku(self):

        poleScriptCaryVsechTrojuhelniku = []

        for r in range(0, len(self.souradniceVsechTrojuhelniku)):
            skriptPoleCary = []
            skriptPoleCary = self.vratScriptProVykresleniJednohoTrojuhelnika(r)

            #prida  data do celkoveho pole
            for p in range(0, len(skriptPoleCary)):
                skriptRadek = skriptPoleCary[p]
                poleScriptCaryVsechTrojuhelniku.append(skriptRadek)

        return(poleScriptCaryVsechTrojuhelniku)


    def vratScriptProVykresleniJednohoTrojuhelnika(self, index):
        trojuhelnik = self.souradniceVsechTrojuhelniku[index]
        skriptPoleCary = []

        uzel1 = trojuhelnik[0]
        uzel2 = trojuhelnik[1]
        uzel3 = trojuhelnik[2]

        skriptPoleCary = self.pridejCaruDoPole(uzel1, uzel2, skriptPoleCary)
        skriptPoleCary = self.pridejCaruDoPole(uzel2, uzel3, skriptPoleCary)
        skriptPoleCary = self.pridejCaruDoPole(uzel1, uzel3, skriptPoleCary)

        return(skriptPoleCary)


    def pridejCaruDoPole(self, uzelA, uzelB, skriptPoleCary):
        pridatCaru = []

        Ax = uzelA[0]
        Ay = uzelA[1]

        Bx = uzelB[0]
        By = uzelB[1]

        # aplikuje meritka
        Ax = self.My * Ax
        Bx = self.My * Bx
        Ay = self.My * Ay
        By = self.My * By


        pridatCaru = self.pridejCaru(Ax, Ay, Bx, By)
        skriptPoleCary.append(pridatCaru[0])
        skriptPoleCary.append(pridatCaru[1])

        return(skriptPoleCary)


    def pridejCaru(self, Ax, Ay, Bx, By):

        pridatCaru = []
        pridatCaruStr = 'ctx.moveTo(' + str(Ax) + ', ' + str(Ay) + ');'
        pridatCaru.append(pridatCaruStr)
        pridatCaruStr = 'ctx.lineTo(' + str(Bx) + ', ' + str(By) + ');'
        pridatCaru.append(pridatCaruStr)

        return (pridatCaru)


    def vytvorPoleScript(self, poleScriptCaryVsechTrojuhelniku):
        poleScript = []
        poleScript.append('<script>')
        poleScript.append('var c = document.getElementById("myCanvas");')
        poleScript.append('var ctx = c.getContext("2d");')
        poleScript.append('ctx.beginPath();')

        for r in range(0, len(poleScriptCaryVsechTrojuhelniku)):
            radek = poleScriptCaryVsechTrojuhelniku[r]
            poleScript.append(radek)

        poleScript.append('ctx.stroke();')
        poleScript.append('</script>')

        return(poleScript)


    def vytvorHtmlPole(selfm, poleScript):
        poleHtml = []
        poleHtml.append("<!DOCTYPE html>")
        poleHtml.append("<html>")
        poleHtml.append("<head>")
        poleHtml.append("<title>Schema konstrukce</title>")
        poleHtml.append("</head>")

        poleHtml.append('<canvas id="myCanvas" width="300" height="150" style="border:1px solid #d3d3d3;">')
        poleHtml.append('Your browser does not support the HTML5 canvas tag.</canvas>')

        for r in range(0, len(poleScript)):
            radek = poleScript[r]
            poleHtml.append(radek)

        poleHtml.append("<body>")
        poleHtml.append("<body>")


        poleHtml.append("</body>")
        poleHtml.append("</html>")

        return(poleHtml)



    def zapisHtml(self, poleHtml):

        dataWrite = ""
        f = open(self.nazevSouboru, 'w')

        for i in range(0, len(poleHtml)):
            radek = poleHtml[i]
            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()
