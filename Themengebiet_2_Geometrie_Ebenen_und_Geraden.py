#Themengebiet 2: Projekt I
#In diesem Projekt sollen einfache geometrische Objekte, wie Geraden und Ebenen im 3-dimensionalen Raum
#betrachtet werden. Hierzu schreibe man zuerst die zwei Klassen Gerade und Ebene mit den nicht-öffentlichen
#Attributen x_0,vec_1,vec_2 im Falle von Ebenen. x_0,vec_1 im Falle von Geraden.
#Hierbei sollen die Ebenen bzw. Geraden in Parameterform dargestellt sein. Man schreibe Konstruktoren
#um die Objekte aus vorgegebenen x_0,vec_1,vec_2 bzw. x_0,vec_1 zu erzeugen.
# Die Parameter sollen hier Listen sein. Zusätzlich soll für beide Klassen eine Methode move(vec)
# geschrieben werden, die die Gerade/Ebene um vec verschiebt und eine Methode ison(x), die ausgibt,
#ob der Punkt x(Liste/Tupel) auf der Gerade/Ebene liegt. Für alle in diesem Themengebiet geschriebenen
#Klassen stelle man vernünftige (passende) Konstruktoren, und set, get-Methoden und geeignete Ausgaben,
#__str__ und __repr__, zur Verfügung.
# Man überprüfe stets die Funkltionalität der implementierten Methoden.

#Projekt I: Man schreibe eine Methode getnormal(), die einen Vektor(Liste) zurückliefert, der senkrecht
#auf der Ebene steht. Anschließend schreibe man eine weitere Klasse EbeneHess, die die nichtöffentlichen
#Attribute d,normal_0 enthält und die Ebene in der Hesseschen Normalenform (Wikipedia) darstellt.
#Jetzt schreibe man für die Klassen EbeneHess und Ebene Methoden, die die Darstellung in das jeweils
#andere Format überführen, also die gleiche Ebene im jeweils anderen Format zurück liefern.



class Ebene:
    def __init__(self, x0, vector1, vector2):
        self._x0 = x0
        self._vector1 = vector1
        self._vector2 = vector2

class Gerade:
    def __init__(self, x0, vector1):
        self._x0 = x0
        self._vector1 = vector1
