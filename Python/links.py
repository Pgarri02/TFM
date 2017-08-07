# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:19:39 2017

"""



def generar_links_final():
    f = open('teognisgriego.html', 'r', encoding='utf-8')
    f2 = open('teognisgriego_links.html', 'w', encoding='utf-8')   
    ls = f.readlines()
    for linea in ls:
        if linea.find("<p>") != -1:
            mi_pal = ""
            link = False
            for letra in linea:
                if letra == "<":
                    link = False
                    if mi_pal != "":
                        
                        mi_pal = "<a href=\"http://logeion.uchicago.edu/index.html#" + mi_pal + "\">" +  mi_pal + "</a>"
                        f2.write(mi_pal)
                    mi_pal = ""
                    f2.write(letra)
                elif letra == " " or letra == "," or letra == "." or letra == "\n":
                    if mi_pal != "":
                        mi_pal = "<a href=\"http://logeion.uchicago.edu/index.html#" + mi_pal + "\">" +  mi_pal + "</a>"
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

d