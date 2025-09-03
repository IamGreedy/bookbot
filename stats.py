def number_of_words (text):              # Compte le nombre de mots dans le livre
    words = text.split()
    count_word = 0
    for word in words:
        count_word+=1
    return count_word

def number_of_characters (text):         # Compte le nombre d’occurrences de chaque caractère et renvoie un dictionnaire où chaque clé est une lettre et chaque valeur est son nombre d’apparitions
    characters = {}                      # On crée un dictionnaire vide
    for character in text:               # On parcourt chaque caractère du texte (l'argument texte étant un str)
        character=character.lower()      # On met en minuscule pour fusionner ‘A’ et ‘a’ 
        if character in characters:      # Si on a déjà vu ce caractère, on fait +1 sinon on l'initialise à 1
            characters[character] +=1
        else:
            characters[character]=1
    return characters

def sort_on(item):                       # Prend un dictionnaire en entrée et renvoie la valeur associée à la clé "num" pour permettre de trier une liste selon ce nombre.
    return item["num"]                   # On appelle la fonction avec "letters.sort(key=sort_on, reverse=True)"

def dict_to_small_dict(characters):
    dicts=[]                                     # On crée une liste vide
    for char, count in characters.items():       # On parcourt le dictionnaire characters (chaque char = clé, chaque count = valeur). .items() sert à récupérer à la fois les clés et les valeurs d’un dictionnaire sous forme de paires (clé, valeur) pour pouvoir les parcourir facilement dans une boucle.
        if char.isalpha():                       # On vérifie que c'est une lettre de l'alphabet
            small_dict ={                        # On construit un petit dictionnaire avec la lettre et son nombre d'occurences
                "char":char,
                "num":count
            }
            dicts.append(small_dict)             # On ajoute les petits dictionnaires à la liste dicts pour faire une grande de liste de pleins de petits dictionnaires
    return dicts
def char_dict_to_sorted_list (characters):        # On prend characters de number_of_characters en entrée
    letters = dict_to_small_dict(characters)      # On fait une liste de petits dictionnaires 
    letters.sort(key=sort_on, reverse = True)     # On trie les lettres en fonction de leur nombre d'occurences et Reverse = True permet de les trier de manière décroissante
    return letters




    




