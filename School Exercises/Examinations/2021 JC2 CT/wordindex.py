data = [('afraid', 23), ("bay'd", 28), ('beard', 6), ('beguiled', 4), ('bequeath', 20), ('bored', 18), ('broom', 38), ('changeling', 27), ('comest', 25), ('despise', 21), ('dissension', 8), ('duty', 2), ('gentles', 33), ('hand', 10), ('handicraft', 30), ('iii', 13), ('judgment', 1), ("labour'd", 32), ('liar', 39), ('lover', 5), ('luck', 7), ('neither', 16), ('ounce', 11), ('overbear', 29), ('ox-beef', 17), ('peril', 12), ('pursue', 9), ('ready', 26), ('release', 24), ('shines', 36), ('stones', 34), ('strife', 35), ('strike', 22), ('supposed', 31), ('tire', 15), ('unsay', 3), ('venus', 19), ('warrant', 37), ('yes', 14)]

class WordIndex:
    def __init__(self, inputlist):
        self.root = self.fromlist(inputlist)
    
    def fromlist(self, inputlist):
        '''
        Converts inputlist into a subtree,
        and returns the root node of the subtree
        '''
        if len(inputlist) == 0:
            return None
        mid = len(inputlist) // 2
        key, position = inputlist[mid]
        root = Node(key, position)
        if len(inputlist) > 1:
            root.left = cls.fromlist(inputlist[:mid])
            root.right = cls.fromlist(inputlist[mid+1:])
        return root

class Node:
    def __repr__(self):
        return f'Node("{self.key}": {self.position})'

word_index = WordIndex(data)
