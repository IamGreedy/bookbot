def number_of_words (text):
    words = text.split()
    count_word = 0
    for word in words:
        count_word+=1
    return count_word

def number_of_characters (text):
    characters = {}
    for character in text:
        character=character.lower()
        if character in characters:
            characters[character] +=1
        else:
            characters[character]=1
    return characters

def sort_on(item):
    return item["num"]

def dict_to_small_dict(characters):
    dicts=[]
    for char, count in characters.items():
        if char.isalpha():
            small_dict ={
                "char":char,
                "num":count
            }
            dicts.append(small_dict)
    return dicts

def char_dict_to_sorted_list (characters):
    letters = dict_to_small_dict(characters)
    letters.sort(key=sort_on, reverse = True)
    return letters




    




