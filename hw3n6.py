def int_func(word):
    latin_char = 'abcdf'
    return word.title() if not set(word).difference(latin_char)else False


print(int_func('word'), ' ')
