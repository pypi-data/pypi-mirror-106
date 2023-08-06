import os
import re

def count_words(catalog: str, word: str) -> int:
    answer = 0
    word = word.lower()
    
    for dirpath, dirnames, filenames in os.walk(catalog):
        for filename in filenames:
            if os.path.splitext(filename)[1] != '.txt':
                continue

            with open(os.path.join(dirpath, filename), encoding='utf-8') as file:
                file_gen = (line for line in file)
                
                for line in file_gen:
                    line = (line.lower()).split(' ')
                    for i in line:
                        res = re.sub(r"[.;:,?!()\"'-]", '', i)
                        if '\n' in res:
                            res = res.replace('\n', '')
                        if word == res:
                            answer += 1

    return answer