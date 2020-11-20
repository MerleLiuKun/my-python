"""
    迭代器模式实现
"""

import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)
    
    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
    
    def __iter__(self):
        return SentenceIterable(self.words)

class SentenceIterable:
    def __init__(self, words):
        self.words = words
        self.index = 0
    
    # 无参 next
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        
        self.index += 1
        return word
    
    # 返回本身
    def __iter__(self):
        return self

if __name__ == "__main__":
    s = Sentence("This is sentence v2")
    
    for word in s:
        print(word)
