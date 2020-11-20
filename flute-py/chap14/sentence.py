import re
import reprlib

RE_WROD = re.compile("\w+")

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WROD.findall(text)

    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)

if __name__ == "__main__":
    s = Sentence('"This is a test for sentence')
    for word in s:
        print(word)
