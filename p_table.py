with open('Periodic_corpus', 'r') as f:
    corpus = eval(f.read())

class p_table:
    def __init__ (self):
        self.table = corpus
