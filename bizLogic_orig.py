class BizLogic(object):

    """
    Klasse BizLogic (Business Logic):
    Enthält Implementierungen (Methoden) mehrerer Business-Logiken sowie deren 
    Vor- und Nachbedingungen (prerequisites, post-conditions) ...

    Die Vor- und Nachbedingungen werden innerhalb der Klasse BizLogic in Form von 
    Python-Dekoratoren modelliert. Diese Advanced-Methoden werden ausführlicher in 
    https://www.python-kurs.eu/python3_dekorateure.php beschrieben.
    Die Nachbedingung wird in unserem Fall nicht benötigt, da die Vorbedingungen bereits 
    durch 'raise Exceptions' die Weiterverarbeitung der Werte in den Hauptmethoden unterbinden.

    Die Klasse BizLogic enthält folgende Business-Logiken:
    1. ggT: Berechnung des größten gemeinsamen Teilers inkl. der Implementierungs-Varianten:
    1.1. euklid_recursive()
    1.2. euklid()
    """

    # Vorbedingung zur ggT-Berechnung
    def pre_two_natural_numbers(f):
        # Beide Paramterwerte müssen vom Typ ganze Zahlen (int) sein
        def helper(x, y):
            if type(x) == int and type(y) == int:
                return f(x, y)
            else:
                raise Exception("Argument(s) is not an integer")
        return helper


    # 1.1. euklid_recursive()
    @pre_two_natural_numbers
    def euklid_recursive(a, b):
        """Calculate HCF (ggT) using recursive Euklidian algorithm.

        Keyword arguments:
        a -- first integer number (no default)
        b -- second integer number (no default)
        Return value:
        ggt -- ggt as integer number
        Error return value:
        False -- if either of the two params are not integer values
        """

        if b == 0:
            return a
        else:
            return euklid_recursive(b, a % b)

    # 1.2. euklid()
    @pre_two_natural_numbers
    def euklid(a, b):
        """Calculate HCF (ggT) using linear Euklidian algorithm.

        Keyword arguments:
        a -- first integer number (no default)
        b -- second integer number (no default)
        Return value:
        ggt (as integer number)
        Error return value:
        False -- if either of the two params are not integer values
        """

        # main algorithm
        if a == 0:
            return b
        else:
            while b != 0:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return a

if __name__ == '__main__':
    # Dekoratoren sind in unserem Fall nur zusätzlich zu den try ... except Umgebungen um
    # die int(input()) Funktionen zu betrachten. Die eigentliche Fehlerbehandlung muss bereits
    # bei der Eingabe der Werte (App-GUI) erfolgen (s. main.py)!
    a = int(input("Erster Wert: "))
    b = int(input("Zweiter Wert: "))
    try:
        print("Der ggT von {:d} und {:d} ist: {:d}".format(a, b, BizLogic.euklid(a, b)))
    except:
        print("Sorry, wrong input type(s). Use int instead!")