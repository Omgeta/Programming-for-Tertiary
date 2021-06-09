pity = int(input("Enter the number of pities: ").strip())

class Node:
    def __init__(self, con: int, guarantee: bool, prob: float):
        self.con = con
        self.guarantee = guarantee
        self.prob = prob

    def __repr__(self):
        return f"Node({self.con}, {self.guarantee}, {self.prob})"

    def next(self):
        if self.guarantee:
            return Node(self.con+1, False, self.prob)
        else:
            return Node(self.con, True, self.prob * 0.5), Node(self.con+1, False, self.prob * 0.5)

class PityCalculator:
    @staticmethod
    def _final(pity: int) -> list:
        curr = Node(-1, False, 1.0)
        res = [curr]
        for _ in range(pity):
            a = []
            for x in res:
                a.extend(x.next())
            res = a
        
        return res

    def calculate(self, pity: int):
        x = self._final(pity)
        counts = {}
        for node in x:
            if node.con in counts:
                counts[node.con] += node.prob
            elif node.con > 6:
                counts[6] += node.prob
            else:
                counts[node.con] = node.prob

        for con,prob in counts.items():
            print(f"C{con}: {prob * 100}%")

pc = PityCalculator()
pc.calculate(pity)

while True:
    pass
    

    