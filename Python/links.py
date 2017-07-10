# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:19:39 2017

@author: adrian
"""

def guardar(texto):
    f = open('mi_fichero.txt', 'w')
    f.write(texto)
    f.close()

def leer():
    f = open('teognis.xml', 'r')
    f2 = open('teognis_links.xml', 'w')
    ls = f.readlines()
    for linea in ls:
        mi_pal = ""
        link = False
        for letra in linea:
            if letra == "<":
                link = False
                if mi_pal != "":
                    mi_pal = "<a ref=\"www.perseus.tufts.edu/hopper/morph?l=" + mi_pal + "\">" +  mi_pal + "</a>"
                    f2.write(mi_pal)
                mi_pal = ""
                f2.write(letra)
            elif letra == " " or letra == "," or letra == "\n":
                if mi_pal != "":
                    mi_pal = "<a ref=\"www.perseus.tufts.edu/hopper/morph?l=" + mi_pal + "\">" +  mi_pal + "</a>"
                    f2.write(mi_pal)
                mi_pal = ""
                f2.write(letra)
            elif link:
                mi_pal += letra
            elif letra == ">":
                link = True
                f2.write(letra)
            else:
                f2.write(letra)
    f.close()
    f2.close()