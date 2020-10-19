class BizLogic(object):

    """
    Klasse BizLogic (Business Logic):
    Enthält Implementierungen (Methoden) mehrerer Business-Logiken sowie deren 
    Vor- und Nachbedingungen (prerequisites, post-conditions) ...

    Die Vor- und Nachbedingungen werden innerhalb der Klasse BizLogic in Form von 
    Python-Dekoratoren modelliert. Diese Advanced-Methoden werden ausführlicher in 
    https://www.python-kurs.eu/python3_dekorateure.php beschrieben.
    s.a. K. Reitz, T. Schlusser: Hitchhiker's Guide für Python, O'Reilly

    Die Klasse BizLogic enthält folgende Business-Logiken:
    1. ggT: Berechnung des größten gemeinsamen Teilers inkl. der Implementierungs-Varianten:
    1.1. euklid_recursive()
    1.2. euklid()
    """

    fist_entry = True

    """ 
    Vor- und Nachbedingung zur ggT-Berechnung
    Die Methoden euklid(a, b) und euklid_recursive(a, b) erhalten als Eingaben Werte des Typs
    String. Diese müssen zunächst in den Typ Int umgewandelt werden (Vorbedingung). 
    Das Ergebnis der Berechnung liegt wiederum als Typ Int vor. Zur Ausgabe dieses Wertes
    muss als Nachbedingung der Wert in den Typ String umgewandelt werden.
    Die Vor- und Nachbedingungen werden im Folgenden durch den Ausdruck
    str(f(int(x), int(y))) modelliert. 
    Er umfasst mit int() die beiden Vorbedingungen und mit str() die Nachbedingung zur 
    betrachteten Methode f (euklid bzw. euklid_recursive).
    """
    def pre_two_natural_numbers(f):
        # Beide Paramterwerte müssen vom Typ ganze Zahlen (int) sein
        # Lassen sich die String-Argumente nicht in Int umwandeln, so wird eine Ausnahmebehandlung
        # angestoßen (raise Exception). Diese kann in folgenden Methoden verwendet werden.
        def helper(x, y):
            try:
                return str(f(int(x), int(y)))
            except:
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
    # tbd: Implementierung der Dekoratoren um die rekursice Variante euklid_recursive
    a = int(input("Erster Wert: "))
    b = int(input("Zweiter Wert: "))
    try:
        print("Der ggT von {:d} und {:d} ist: {:d}".format(a, b, BizLogic.euklid(a, b)))
    except:
        print("Sorry, wrong input type(s). Use int instead!")