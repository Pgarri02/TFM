# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:19:39 2017

"""

def generar_links_plano():
    f = open('texto.txt', 'r')
    f2 = open('texto_links.txt', 'w')
    ls = f.readlines()
    texto = ""
    for linea in ls:
        palabras = linea.split()
        for pal in palabras:
            if pal[-1] == ",":
                pal = pal[:-1]
                texto = texto + "<a ref=\"http://logeion.uchicago.edu/index.html#" + pal + "\">" +  pal + "</a>" + ", "
            else:
                texto = texto + "<a ref=\"http://logeion.uchicago.edu/index.html#" + pal + "\">" +  pal + "</a>" + " "
        texto = texto + "\n"
    f2.write(texto)
    f.close()
    f2.close()

def generar_links_htmlv2():
    f = open('teognisgriego.html', 'r')
    f2 = open('teognisgriego_links.html', 'w')   
    ls = f.readlines()
    for linea in ls:
        if linea.find("<p>") != -1:
            mi_pal = ""
            link = False
            for letra in linea:
                if letra == "<":
                    link = False
                    if mi_pal != "":
                        
                        mi_pal = "<a ref=\"http://logeion.uchicago.edu/index.html#" + mi_pal + "\">" +  mi_pal + "</a>"
                        f2.write(mi_pal)
                    mi_pal = ""
                    f2.write(letra)
                elif letra == " " or letra == "," or letra == "." or letra == "\n":
                    if mi_pal != "":
                        mi_pal = "<a ref=\"http://logeion.uchicago.edu/index.html#" + mi_pal + "\">" +  mi_pal + "</a>"
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
        else:
            f2.write(linea)
    f.close()
    f2.close()         

def generar_links_html():
    f = open('teognisgriego.html', 'r')
    f2 = open('texto_links.txt', 'w')
    ls = f.readlines()
    for linea in ls:
        mi_pal = ""
        link = False
        for letra in linea:
            if letra == "<":
                link = False
                if mi_pal != "":
                    
                    mi_pal = "<a ref=\"http://logeion.uchicago.edu/index.html#" + mi_pal + "\">" +  mi_pal + "</a>"
                    f2.write(mi_pal)
                mi_pal = ""
                f2.write(letra)
            elif letra == " " or letra == "," or letra == "." or letra == "\n":
                if mi_pal != "":
                    mi_pal = "<a ref=\"http://logeion.uchicago.edu/index.html#" + mi_pal + "\">" +  mi_pal + "</a>"
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