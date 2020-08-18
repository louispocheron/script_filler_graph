import os 
from random import randint

# boucle pour les 365 commit pour automatiser 
for i in range(1, 365):


# deuxieme boucle qui fera plusieurs commit par jour pour pas a avoir attendre un an pour avoir un graphique tout vert ! 
# et avoir différentes teintes de vert sinon ce serait trop suspicieux....
    for j in range(0, randint(1, 10)):
        d = str(i) + ' days ago'
# creez un fichier .txt dans lequel le bot ecrira dedans
        with open('file.txt', 'a') as file:
             file.write(d)
# et enfin les différente commandes git ! 
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin main')
