
import re,builtins,math

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_pattern = ['/']

test_phrase = 'This is a string with back slash / and some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'/+', # sequence of digits
                # r'\D+', # sequence of non-digits
                # r'\s+', # sequence of whitespace
                # r'\S+', # sequence of non-whitespace
                # r'\w+', # alphanumeric characters
                # r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)
# print(dir(builtins))
