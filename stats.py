def get_num_words(text):
    words = text.split()
    return len(words)
def get_count(list_text):
    count={}
    for letter in list_text:
        check_letter = letter.lower()
        if check_letter in count:
            count[check_letter]+=1
        else:
            count[check_letter]=1
    return count
def sort_dict(dictionary):
    sorting_dict = []
    for key,value in dictionary.items():
        char = key
        num = value
        dict_to_append = { "char": char, "num" : num }
        sorting_dict.append(dict_to_append)
    sorting_dict.sort(reverse=True,key=sort_on)
    return sorting_dict
def sort_on(items):
    return items["num"]



