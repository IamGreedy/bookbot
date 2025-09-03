from stats import number_of_words
from stats import number_of_characters
from stats import char_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f: # With open () as permet d'ouvrir le fichier mais aussi de le fermer une fois que le bloc se termine.
        return f.read()# Il faut toujours open le file avant de lire ou écrire un fichier.


def main():
    if len(sys.argv) !=2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    
    #calcul des stats
    num_words = number_of_words(text)
    num_characters = number_of_characters(text)
    letters=char_dict_to_sorted_list(num_characters)
    
    #Impression formatée
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    #Boucle sur la liste triée 
    for item in letters :
        ch=item["char"]
        num=item["num"]
        print(f"{ch}: {num}")

    print("============= END ===============")

main()