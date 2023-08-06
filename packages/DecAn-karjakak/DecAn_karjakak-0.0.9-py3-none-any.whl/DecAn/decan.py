# -*- coding: utf-8 -*-
#Copyright (c) 2020, KarjaKAK
#All rights reserved.

import time
import os
import argparse
import json
import functools
import re
import string
import pickle
import io
from GenPy import Fixstr

"""
Snippet from:
https://docs.python.org/3/library/pickle.html
"""
class RestrictedUnpickler(pickle.Unpickler):
    """Restriction for running modules and functions"""
    
    def find_class(self, module, name):
        if module and name:
            raise pickle.UnpicklingError(f"{module}.{name} not allowed!!!")

def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    
    try:
        return RestrictedUnpickler(io.BytesIO(s)).load()
    except Exception as e:
        raise e

def timer(func):
    """
    Print the runtime of the decorated function
    https://realpython.com/primer-on-python-decorators
    """
    
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"\nFinished {func.__name__!r} in {run_time:.4f} secs\n")
        return(value)    
    return wrapper_timer

def reconst(text: str) -> dict:
    """Deconstruct by reconstruct the text."""
    
    sd = {i: text.count(i) for i in tuple(set(text))}
    try:
        for i in tuple(sd):
            if i in string.punctuation:
                regex = re.compile(rf'\{i}')
            else:
                regex = re.compile(rf'{i}')
            gt = tuple(j.span()[0] for j in regex.finditer(text))
            sd[i] = gt
            text = text.replace(i, '')
            del gt
        return sd
    except Exception as e:
        raise e

def lookwd(alp: str, text: str) -> tuple:
    """Looking for an alphabet or a words positions."""
    
    if alp in text:
        pos = ()
        np = 0
        c = text.count(alp)
        if len(alp) == 1:
            while c:
                np = np + text.find(alp)
                pos = pos + (np,)
                np += 1
                c -= 1
                text = text[text.find(alp)+1:]
            del np, text, c, alp
            return pos
        else:
            while c:
                np = np + text.find(alp)
                pos = pos + ((np, np + len(alp)),)
                np += 1
                c -= 1
                text = text[text.find(alp)+1:]
            del np, text, c, alp
            return pos
        
@timer
def deconstruct(text: str, filename: str, path: str):
    """To deconstruct a text file or sentences to json."""
    
    if os.path.isfile(text):
        if text.rpartition('.')[2] == 'txt':
            with open(text) as rd:
                text = rd.read()
        else:
            raise Exception('Cannot read non-.txt file!!!')
    text = Fixstr(text).fixingfs(False)
    dics = reconst(text)
    if os.path.isdir(path) and filename.rpartition('.')[2] == 'pickle':
        with open(os.path.join(path, filename), 'wb') as dc:
            pickle.dump(dics, dc)
    elif os.path.isdir(path) and filename.rpartition('.')[2] == 'json':
        with open(os.path.join(path, filename), 'w') as dc:
            json.dump(dics, dc)
    else:
        raise Exception('Be specific on file extension, either ".json", or ".pickle"!!!')
    del dics, text, filename, path


@timer
def construct(file: str) -> str:
    """To construct back the deconstruct text that saved in json file."""
    
    rd = None
    if os.path.isfile(file) and file.rpartition('.')[2] == 'pickle':
        with open(file, 'rb') as rjs:
            rd = restricted_loads(rjs.read())
    elif os.path.isfile(file) and file.rpartition('.')[2] == 'json':
        with open(file) as rjs:
            rd = json.load(rjs)        
    else:
        raise Exception('Either file not exist or file is not .pickle/.json!!!')
    if rd:
        try:
            strng = ''
            for i in list(rd)[::-1]:
                for j in rd[i]:
                    strng = f'{strng[:j]}{i}{strng[j:]}'
                del rd[i]
            return strng
        except:
            raise Exception('WARNING-ERROR: Please choose a deconstructed file!!!')

@timer
def textsortchrs(txts: str, alph: list = None):
    """
    Doing analysis of finding each char or words for their position in text.
    * Reference:
    * https://stackoverflow.com/questions/26184100/how-does-v-differ-from-x0b-or-x0c
    * \v == VT [vertical tab (\x0b)]
    * \f == FF [form feed (\x0c)]
    * In string.printable appearing "\x0b" and "\x0c"
    """    
    if os.path.isfile(txts):
        if txts.rpartition('.')[2] == 'txt':
            with open(txts) as rd:
                txts = rd.read()
        else:
            raise Exception('Cannot read non-.txt file!!!')
    txts = Fixstr(txts).fixingfs(False)    
    if isinstance(alph, list):
        dics = {}
        regex = re.compile(r"\S?\w+\S+")
        for i in alph:
            gtp = lookwd(i, txts)
            if gtp:
                dics = dics | {i: {len(gtp): gtp}} 
                del gtp
                if len(i) > 1:
                    print(f'"{i}": {dics[i]}')
                    print(f'"{i}" is {len(dics[i][list(dics[i])[0]])} out of total {len(tuple(regex.finditer(txts)))} words!\n')
                    del dics[i]
                else:
                    print(f'{repr(i)}: {dics[i]}')
                    print(f'{repr(i)} is {len(dics[i][list(dics[i])[0]])} out of total {len(txts)} chars!\n')
                    del dics[i]
            else:
                print(f'No such word {repr(i)} in text!!!')
    else:
        try:
            alph = dict(sorted(reconst(txts).items(), key = lambda k: len(k[1]), reverse = True))
            once = tuple()
            maxi = ('', 0)
            space = 0
            asci = tuple()
            punct = tuple()
            digi = tuple()
            uni = tuple()
            pri = tuple()
            for i, j in alph.items():
                print(f'{repr(i)}: sub-total: {len(j)}')
                if len(j) == 1:
                    once += (i,)
                if len(j) >= maxi[-1] and i not in ['\n','\t','\r','\v','\f', ' ']:
                    if maxi[0] == '':
                        maxi = (i, len(j))
                    else:
                        maxi = maxi[:-1] + (i,) + (maxi[-1],)
                if i in ['\n','\t','\r','\v','\f', ' ']:
                    space += len(j)
                    pri += (i,)
                elif i in string.ascii_letters:
                    asci += (i,)
                elif i in string.digits:
                    digi += (i,)
                elif i in string.punctuation:
                    punct += (i,)            
                else:
                    uni += (i,)
            del alph
            print(f'Total of {len(txts)} chars.')
            print(f'Total of {len(txts)-space} chars, exclude space and printable.')
            print(f'Space and printable occured {space} in the text.')
            print(f'Chars that occur once in text: {", ".join(repr(i) for i in once)}.')
            if len(maxi) > 2:
                print(f'Chars that used most in text: [{", ".join(sorted(repr(i) for i in maxi[:-1]))}], {maxi[-1]} occurences.')
            else:
                print(f'Char that used most in text: {repr(maxi[0])}, {maxi[1]} occurences.')
            print(f"Construction of the text's chars:\n")
            print(f"- ASCII letters: [{', '.join(sorted(repr(i) for i in asci))}].\n")
            print(f"- Unicode letters: [{', '.join(sorted(repr(i) for i in uni))}].\n")
            print(f"- Numerical: [{', '.join(sorted(repr(i) for i in digi))}].\n")
            print(f"- Punctuation: [{', '.join(sorted(repr(i) for i in punct))}].\n")
            print(f"- Printable: [{', '.join(sorted(repr(i) for i in pri))}].")
            del once, maxi, space, asci, punct, uni, digi, pri
        except Exception as e:
            raise e
            
def main():
    parser = argparse.ArgumentParser(prog = 'DecAn',description = 'Analyze and Deconstruct words')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--deconstruct', type = str, nargs = 3, help = 'Save deconstruct as json file')
    group.add_argument('-c', '--construct', type = str, help = 'Construct back the deconstruct in json file')
    parser.add_argument('-a', '--analyze', type = str, help = 'Analyzing chars in a text')
    parser.add_argument('-s', '--search', type = str, action = 'extend', nargs = '+', help = 'Search list [only use after "-a"]')
    args = parser.parse_args()
    if args.analyze:
        if args.search:
            textsortchrs(args.analyze, args.search)
        else:
            textsortchrs(args.analyze)
    elif args.deconstruct:
        deconstruct(args.deconstruct[0], args.deconstruct[1], args.deconstruct[2])
    elif args.construct:
        print(construct(args.construct))

if __name__ == '__main__':
    main()