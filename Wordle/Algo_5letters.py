def extract_five_letter_words(input_file, output_file):
    # Liste pour stocker les mots de 5 lettres
    five_letter_words = []

    # Ouvrir le fichier source en mode lecture
    with open(input_file, 'r') as fin:
        # Parcourir chaque ligne du fichier
        for line in fin:
            # Séparer la ligne en mots
            words = line.split()

            # Vérifier chaque mot
            for word in words:
                # Si le mot a exactement 5 lettres, l'ajouter à la liste
                if len(word) == 5:
                    five_letter_words.append(word)

    # Afficher les mots extraits pour débogage
    print("Mots extraits :", five_letter_words)

    # Ouvrir le fichier de sortie en mode écriture
    with open(output_file, 'w') as fout:
        # Écrire chaque mot extrait dans le fichier de sortie
        for five_letter_word in five_letter_words:
            fout.write(five_letter_word + '\n')

# Appeler la fonction pour extraire les mots de 5 lettres et les écrire dans un fichier
extract_five_letter_words('word.txt', 'output.txt')
