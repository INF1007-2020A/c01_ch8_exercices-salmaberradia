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

def grade(grades_file, target_file):
    correspondances = {20: 'F', 40: 'D', 50: 'C', 70: 'B', 85: 'A'}

    with open(grades_file, 'r') as note_data, open(target_file,'w') as target:
        for line in note_data.readlines():
            note = float(line)
            for grade in correspondances.keys():
                if grade == 85 and note > grade:
                    target.write('A*')
                if note <= grade:
                    target.write(correspondances[grade])
                    break       

def nombre_croissant(fichier):
    with open(fichier, 'r') as texte:
        return sorted([int(word) for word in texte.read().split() if word.isdigit()])


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(nombre_croissant('exemple.txt')) 