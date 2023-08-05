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

def timer(func):
    """
    Print the runtime of the decorated function
    https://realpython.com/primer-on-python-decorators/#timing-functions
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
    # Deconstruct by reconstruct the text.
    
    sd = {i: text.count(i) for i in sorted(tuple(set(text)), key = lambda y: text.find(y))}
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
    # Looking for an alphabet or a words positions.
    
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
    # To deconstruct a text file or sentences to json.
    
    if os.path.isfile(text):
        if text.rpartition('.')[2] == 'txt':
            with open(text) as rd:
                text = rd.read()
        else:
            raise Exception('Cannot read non-.txt file!!!')
    dics = reconst(text)
    if os.path.isdir(path):
        with open(os.path.join(path, fi := f'{filename}.json' if '.json' not in filename else filename), 'w') as dc:
            json.dump(dics, dc)
    del dics, text, filename, path, fi


@timer
def construct(filejson: json) -> str:
    # To construct back the deconstruct text that saved in json file.
    
    if os.path.isfile(filejson):
        with open(filejson) as rjs:
            rd = json.load(rjs)
    strng = ''
    for i in list(rd)[::-1]:
        for j in rd[i]:
            strng = f'{strng[:j]}{i}{strng[j:]}'
        del rd[i]
        print(strng)
    return strng

@timer
def textsortchrs(txts: str, alph: list = None):
    # Doing analysis of finding each char or words for their position in text. 
    
    if os.path.isfile(txts):
        if txts.rpartition('.')[2] == 'txt':
            with open(txts) as rd:
                txts = rd.read()
        else:
            raise Exception('Cannot read non-.txt file!!!')
        
    dics = {}
    if isinstance(alph, list):
        for i in alph:
            gtp = lookwd(i, txts)
            if gtp:
                dics = dics | {i: {len(gtp): gtp}} 
                del gtp
                if len(i) > 1:
                    print(f'"{i}": {dics[i]}')
                    print(f'"{i}" is {len(dics[i][list(dics[i])[0]])} out of total {len(txts.split(" "))} words!\n')
                    del dics[i]
                else:
                    print(f'{repr(i)}: {dics[i]}')
                    print(f'{repr(i)} is {len(dics[i][list(dics[i])[0]])} out of total {len(txts)} chars!\n')
                    del dics[i]
            else:
                print(f'No such word {repr(i)} in text!!!')
    else:
        alph = reconst(txts)
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
            if len(j) > maxi[1] and i != " ":
                maxi = (i, len(j))
            if i in ['\n','\t','\r','\x0b','\x0c', ' ']:
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
        print(f'Char that used most in text: {repr(maxi[0])}, {maxi[1]} occurences.')
        print(f"Construction of the text's chars:\n")
        print(f"- ASCII letters: [{', '.join(sorted(repr(i) for i in asci))}].\n")
        print(f"- Unicode letters: [{', '.join(sorted(repr(i) for i in uni))}].\n")
        print(f"- Digits: [{', '.join(sorted(repr(i) for i in digi))}].\n")
        print(f"- Punctuation: [{', '.join(sorted(repr(i) for i in punct))}].\n")
        print(f"- Printable: [{', '.join(sorted(repr(i) for i in pri))}].")
        del once, maxi, space, asci, punct, uni, digi, pri
        
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