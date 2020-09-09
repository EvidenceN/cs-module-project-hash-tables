def word_count(s):
    split = s.lower().split()
    dict_list = []
    empty = {}
    for i in split:
        key = i
        value = len(i)
        dict_list.append((key, value))
        #empty.update(dict_list)
    return dict(dict_list)



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))