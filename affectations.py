#! /usr/bin/env python3

import math
import random


def main():

    apprentis = []
    mentors = []

    # Creating two lists, of mentors and apprentis respectively
    with open('members.txt', 'r') as f:
        # lines = f.readlines()
        # for line in lines:
        for line in f:
            line = line.strip()
            if line[-1] == "🐍":
                mentors.append(line)
            else:
                apprentis.append(line)

    # Calculating number of groups
    # (2 mentors by group,
    # except if number of mentors is odd: then a single mentor
    # for one group)
    nombre_mentors = len(mentors)
    nombre_groupes = math.ceil(nombre_mentors / 2)

    # Calculating minimum size of every group as a result
    nombre_apprentis = len(apprentis)
    taille_minimale_groupe = nombre_apprentis // nombre_groupes

    # Assigning each apprenti to a group
    groupes_apprentis = dict()

    groupes_apprentis = répartit_apprentis(
        nombre_groupes,
        taille_minimale_groupe,
        apprentis
    )

    # Assigning each mentor to a group
    groupes_mentors = répartit_mentors(
        nombre_groupes,
        mentors
    )

    # Aliassing groups
    group_aliases = {i+1:chr(i+ord('G')) for i in range(17)}
    
    # Writing results to file
    with open('groupes.txt', 'w') as f:
        f.write("Pour la prochaine période d'exercices, dirigez-vous vers les salons suivants. ")
        f.write("Vous aurez ainsi la chance de travailler avec des mentors en plus petits groupes.\n")
        for groupe, apprentis in groupes_apprentis.items():
            f.write(''.join([
                '#atelier-',
                group_aliases[groupe],
                ': ',
                ', '.join(apprentis + groupes_mentors[groupe]),
                '\n',
                ]))

  
def répartit_apprentis(
        nombre_groupes,
        taille_minimale_groupe,
        personnes
    ):
    '''Randomly allocates people to groups of equal size,
    to the extent possible'''
    
    groupes = dict()

    random.shuffle(personnes)

    for n in range(1, nombre_groupes+1):
        groupes[n] = []
        effectif = 0
        while effectif < taille_minimale_groupe:
            groupes[n].append(personnes.pop())
            effectif += 1

    # In cases where the total number of people
    # is not a multiple of the number of groups,
    # then people are left unassigned
    # and need to be now allocated

    numero_groupe = 1
    while personnes:
        groupes[numero_groupe].append(personnes.pop())
        numero_groupe += 1
    
    return groupes


def répartit_mentors(
        nombre_groupes,
        personnes
    ):
    '''Randomly allocates 2 mentors to each group,
    or 1 to the last group if no more mentor is available'''

    groupes = dict()

    random.shuffle(personnes)

    for n in range(1, nombre_groupes+1):
        groupes[n] = []
        effectif = 0
        while (personnes and effectif < 2):
            groupes[n].append(personnes.pop())
            effectif += 1

    return groupes


if __name__ == '__main__':
    main()