#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def compare_files(nom_fichier_1: str, nom_fichier_2: str):
    with open('lol', 'r') as a, open('llo', 'r') as b:
        same = True

        while same:
            c = a.read()
            d = b.read()

            same = c == d
    return -1 if same else a.tell 

def triple_space(nom_fichier_1, nom_fichier_2):
    with open(nom_fichier_1, "r") as data, open(nom_fichier_2, 'w') as result:
        text = data.read()
        new_text = text.replace('', '   ')
        result.write(new_text)

        new_text = text.replace(" ", "   ")

    with open(nom_fichier_1, "w") as data:
        data.write(new_text)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    triple_space('lol.txt', 'llo.txt')    