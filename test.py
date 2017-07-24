
from pmask.mask import Cleaner

if __name__ == "__main__":
    
    cln = Cleaner()
    original = '\n'.join(cln.bad_words)
    cln.clean(original)
    print  'SAMPLE', '- '* 30
    for og, ct in zip(original.split('\n'), cln.cleaned.split('\n')):
        print '{:15} ==>  {}'. format(og, ct)
    print  'END SAMPLE', '- '* 25
