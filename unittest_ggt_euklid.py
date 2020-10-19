"""
Unittest_ggt_euklid untersucht das Modul ggt_euklid auf zwei unterschiedliche Arten:
1. Automatische Unittests 
2. Manueller Aufruf der rekursiven oder linearen Implementierungs-Variante des ggT-Algorithmus' inkl. Zeitmessung. 
"""

# Import des zu untersuchenden Moduls (Funktionen)
from bizLogic import BizLogic

# import unittest
import pytest # Alternative zu unittest
import timeit # Zeitmessung
# import time # Alternative zu timeit
import logging # Debugausgaben

# Basis-Einstellungen festlegen:
logging.basicConfig(level=logging.INFO)

# Logger zur aktuellen Sitzung erstellen:
logger = logging.getLogger(__name__)


"""
Pytest (Einfachere Alternative zu Unittest)
Aufruf aus der Kommandozeile/Shell aus Repository-Verzeichnis des aktuellen VS-Projekts, 
   z.B. C:\\Users\\heuser\\source\\repos\\1_ggt_euklid
Parameter -v: verbose
   pytest -v ./unittest_ggt_euklid.py
Contents: https://docs.pytest.org/en/latest/contents.html
Usage: https://docs.pytest.org/en/latest/usage.html
"""

class TestClass:
    # Two test methods, should all be passed ok
    def test_one(self):
        assert BizLogic.euklid(3, 6) == 3

    def test_two(self):
        assert BizLogic.euklid(3, 6) != 2

    """
    # Test method three should yield in an AssertionError failure
    def test_three(self):
        assert BizLogic.euklid(3, 6) != 3
    """

if __name__ == '__main__':
    # Manuelle Aufrufe der beiden Varianten inkl. Zeitmessung
    while True:
        switch = str(input(
"""
Ausführung der ...
  (r)ekursiven Version
  (l)inearen Variante
E(x)it? """))

        if switch in ['R', 'r', 'L', 'l']:
            a = input("Erster Wert: ")
            b = input("Zweiter Wert: ")
        else:
            break

        start_time = timeit.timeit()
        # start_time = time.process_time()

        if switch in ['L', 'l']:
            try:
                logger.info("Der ggT von {} und {} ist (linear): {}".format(a, b, BizLogic.euklid(a, b)))
            except:
                logger.error("Sorry, wrong input value(s). Use int instead!")
        elif switch in ['R', 'r']:
            try:
                logger.info("Der ggT von {} und {} ist (rekursiv): {}".format(a, b, BizLogic.euklid_recursive(a, b)))
            except:
                logger.error("Sorry, wrong input value(s). Use int instead!")
        else:
            break

        end_time = timeit.timeit()
        # end_time = time.process_time()
        logger.info("Elapsed time: {:20.18f} secs".format(end_time - start_time))


