'''
Created on 11/09/2017

@author: 
'''
import logging
from collections import Counter
import sys

nivel_log = logging.ERROR
# nivel_log = logging.DEBUG
logger_cagada = None

def aplecaca_core(letras, kk):
    cuenta_caca = Counter(letras)
    cuentas_ord = sorted(cuenta_caca.items(), key=lambda x:(x[1], x[0]), reverse=False)
    logger_cagada.debug("el conteo ord {}".format(cuentas_ord))
    capacidad = kk
    beneflex = 0
    while cuentas_ord and capacidad:
        letra, mierda = cuentas_ord.pop()
        logger_cagada.debug("la letra {} tiene de mierda {}".format(letra, mierda))
#        while cuentas_ord and mierda > capacidad :
#            letra, mierda = cuentas_ord.pop()
#            logger_cagada.debug("la letraa {} tiene de mierda {}".format(letra, mierda))
        ass = (mierda if mierda <= capacidad else capacidad)
        logger_cagada.debug("para capa {} la mierda es {}".format(capacidad, ass))
        beneflex += ass ** 2
        capacidad -= ass
    return beneflex

def aplecaca_main():
    lista = list(sys.stdin)
    _, kk = [int(x) for x in lista[0].strip().split(" ")]
    letras = lista[1].strip()
    logger_cagada.debug("kk {} letras {}".format(kk, letras))
    shit = aplecaca_core(letras, kk)
    print(shit)
    

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        aplecaca_main()
