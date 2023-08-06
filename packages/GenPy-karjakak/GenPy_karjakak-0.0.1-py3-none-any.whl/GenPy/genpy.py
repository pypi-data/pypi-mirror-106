# -*- coding: utf-8 -*-
#Copyright (c) 2020, KarjaKAK
#All rights reserved.

import re
import os
from pprint import pprint

class Fixstr:
    """
    Fixing String Class.
    """
    def __init__(self, text: str):
        self.text = text

    def fixingfs(self, pr: bool = True) -> str:
        """Fixing text that has ['.', ',', ';', ':'] in the middle, which suppose to be punctuated properly. At best!!!"""
        
        for p in ['.', ',', ';', ':']:
            regs = re.compile(rf'\w+\{p}\w+|\w+\{p}  \w+')
            if p == '.':
                minimize = tuple(sorted((i.group() for i in  tuple(regs.finditer(self.text)) if len(i.group().rpartition(f'{p}')[2]) >= 1 and i.group().rpartition(f'{p}')[2].istitle() and len(i.group().rpartition(f'{p}')[0]) > 1), key = lambda k: k.partition('.')[2]))
            else:
                minimize = tuple(sorted((i.group() for i in  tuple(regs.finditer(self.text)) if len(i.group().rpartition(f'{p}')[2]) >= 1 and any([i.group().rpartition(f'{p}')[2].istitle(), i.group().rpartition(f'{p}')[2].islower()])  and len(i.group().rpartition(f'{p}')[0]) > 1), key = lambda k: k.partition('.')[2]))
            if pr:
                print(f'Fixes needed for "{p}"!')
                pprint(minimize)
                print(f'Total faults: {len(minimize)}\n\nFinished fixes:')
            for w in minimize:
                a = w.replace(f'{p} ', f'{p}') if w.partition(f'{p}')[2][:2].isspace() else w.replace(f'{p}', f'{p} ')
                if pr: print(f'{w} => {a}')
                self.text = f'{self.text[:self.text.find(w)]}{a}{self.text[self.text.find(w) + len(w):]}'
                del a, w
            del minimize
            if pr: print('\n')
        return self.text
    
    def savefix(self, filename: str):
        """Saving Fixed string to a new file."""
        
        if not os.path.isfile(filename):
            fx = self.fixingfs(False)
            with open(filename := filename if filename.rpartition('.')[2] == 'txt' else f'{filename}.txt', 'w') as tx:
                tx.write(fx)
            del fx
        else:
            raise Exception('This file is already exist, please create new one!!!')