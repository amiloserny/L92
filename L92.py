#Amanda Miloserny
string = "SPAM!HelloSPAM! worldSPAM!"
def remove_substring(string, word):
    list = []
    index = 0
    while index < len(string):
        if string[index:index + len(word)]==word:
            index += len(word)
        else:
            list.append(string[index])
            index += 1
    print("".join(list))

remove_substring(string, "SPAM!")
