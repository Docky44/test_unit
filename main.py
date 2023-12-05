def miroir(texte):
    return texte[::-1]

if __name__ == '__main__':
    mot = input("Entrez un mot : ")
    resultat = miroir(mot)
    print("En mode miroir :", resultat)