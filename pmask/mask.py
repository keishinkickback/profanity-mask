import os
import re

class Cleaner(object):
    '''
    check and clean profanity in strings.
    '''
    def __init__(self, skip=4):
        '''

        '''
        # read file
        path_dir = os.path.dirname(os.path.abspath(__file__))
        path_f = os.path.join(path_dir, 'bad_words.txt')
        self.bad_words = set(line.strip('\n').lower() for line in open(path_f))
        # create mapping
        self.mapping = self.crate_mapping(self.bad_words, skip=skip)
        sorted_keys = sorted(list(self.mapping.keys()), reverse=True)
        # create re expression
        self.pattern = re.compile(r'\b(' + '|'.join(sorted_keys) + r')\b',
                                                            re.IGNORECASE)

    def crate_mapping(self, lst_words,skip=4):
        '''
        creats mapping {target:cleaned, ...} from given lst_words
        hide characters in between first and last characters.
        skip: fucking ==> f***i*g with skip=4.
        '''
        mapping = {}
        for og_w in lst_words:
            new_w = ['*' for _ in og_w]
            new_w[0] = og_w[0]
            if skip + 1 < len(og_w):
                new_w[-1] = og_w[-1]
            for i in range(skip, len(og_w), skip):
                new_w[i] = og_w[i]
            mapping[og_w] = ''.join(new_w)
        return mapping

    def create_own_mapping(self,lst_words):
        '''
        creatae your own and call it in __init__ instead of create_mapping
        return dict {word: masked word, ... }
        '''
        pass

    def clean(self, original_string):
        '''
        clean string
        '''
        self.original_string = original_string

        def f_map(x):
            if x.group().lower() in self.mapping:
                return self.mapping[x.group().lower()]
            else:
                return x.group()

        self.cleaned = self.pattern.sub(f_map,original_string)
        lst_chs = []
        for i, ch in enumerate(self.original_string):
            if ch.isupper() and self.cleaned[i].islower():
                lst_chs.append(ch)
            else:
                lst_chs.append(self.cleaned[i])

        self.cleaned = ''.join(lst_chs)
        return self.cleaned

def test():
    # Show all mappings
    cln = Cleaner(skip=4)
    original = '\n'.join(cln.bad_words)
    cln.clean(original)
    print  'MAPPING', '- '* 30
    for og, ct in zip(original.split('\n'), cln.cleaned.split('\n')):
        print '{:15} ==>  {}'. format(og, ct)
    print  'END MAPPING', '- '* 25
    print
    input = "Fuck bullshit apple."
    cln.clean(input)
    print cln.original_string
    print cln.cleaned


if __name__ == "__main__":
    test()
