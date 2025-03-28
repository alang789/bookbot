def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    text = text.lower()
    character_dict = {}
    for char in text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_on(dictionary):
    return dictionary["num"]

def create_sorted_list(dictionary):
    sorted_list = []
    for char in dictionary:
        sorted_list.append({"char" : char, "num" : dictionary[char]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

