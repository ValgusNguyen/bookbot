def count(text):
    words = text.split()
    return len(words)

def into_character(text):
    low_case = text.lower()
    dict = {}
    for i in low_case:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

def sort_on(list):
    return list["num"]    

def sort_dict(dict):
    list = []
    for key, value in dict.items():
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = value
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list
