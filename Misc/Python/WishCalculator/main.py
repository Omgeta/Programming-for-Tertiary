import random
from functools import cache
from collections import Counter

ITERATIONS = 100000


class Rate:
    BASE_5_STAR = 0.006
    def SOFT_5_STAR(x): return 0.15 - 0.01*(x - 75)

    BASE_4_STAR = 0.051

    HARD_RATE = 1


class Reward:
    NEW_CHAR = 0

    DUPL_5_CHAR = 10
    DUPL_5_CHAR_MAX = 25

    DUPL_4_CHAR = 2
    DUPL_4_CHAR_MAX = 5

    ANY_5_WEP = 10
    ANY_4_WEP = 2
    ANY_3_WEP = 0


class Game:
    FEATURED_5 = ["Kazuha"]
    PERMANENT_5 = ["Jean", "Qiqi", "Keqing", "Mona", "Diluc"]
    FEATURED_4 = ["Rosaria", "Bennet", "Razor"]
    PERMANENT_4 = ["Sucrose", "Diona", "Chongyun", "Fischl", "Beidou", "Noelle",
                   "Ningguang", "Xingqiu", "Barbara", "Xinyan", "Xiangling", "Yanfei"]

    WEAPON_5 = "5* WEAPON"
    WEAPON_4 = "4* WEAPON"
    WEAPON_3 = "3* WEAPON"


def guess(prob):
    return random.random() <= prob


def get_input():
    def intput(x): return int(input(x).strip())

    fate = intput("Intertwined Fate: ")
    primogems = intput("Primogems: ")
    starglitter = intput("Starglitter: ")
    five_pity = intput("5* Pity: ")
    four_pity = intput("4* Pity: ")
    five_guarantee = input("5* Guarantee: ") == "y"
    four_guarantee = input("4* Guarantee: ") == "y"

    return fate, primogems, starglitter, five_pity, four_pity, five_guarantee, four_guarantee


class Inventory:
    def __init__(self):
        self.five_chars = {k: 0 for k in Game.FEATURED_5 + Game.PERMANENT_5}
        self.four_chars = {k: 0 for k in Game.FEATURED_4 + Game.PERMANENT_4}

    def add(self, item):
        if item in self.five_chars:
            self.five_chars[item] += 1
        elif item in self.four_chars:
            self.four_chars[item] += 1

    def get_reward(self, item):
        if item in Game.FEATURED_5 + Game.PERMANENT_5:
            count = self.five_chars[item]
            if count == 0:
                return Reward.NEW_CHAR
            elif 0 < count <= 7:
                return Reward.DUPL_5_CHAR
            elif count > 7:
                return Reward.DUPL_5_CHAR_MAX
        elif item in Game.FEATURED_4 + Game.PERMANENT_4:
            count = self.four_chars[item]
            if count == 0:
                return Reward.NEW_CHAR
            elif 0 < count <= 7:
                return Reward.DUPL_4_CHAR
            elif count > 7:
                return Reward.DUPL_4_CHAR_MAX
        elif item == Game.WEAPON_4:
            return Reward.ANY_4_WEP
        else:
            return Reward.ANY_3_WEP

    def merge(self, other):
        self.five_chars = dict(
            Counter(self.five_chars) + Counter(other.five_chars))
        self.four_chars = dict(
            Counter(self.four_chars) + Counter(other.four_chars))
        return self

    def __truediv__(self, x):
        self.five_chars = {k: v/x for k, v in self.five_chars.items()}
        self.four_chars = {k: v/x for k, v in self.four_chars.items()}
        return self


class WishCalculator:
    def __init__(self, fate=0, primogems=0, starglitter=0, five_pity=0, four_pity=0, five_guarantee=False, four_guarantee=False, debug=False):
        self.rolls = fate + primogems // 160
        self.starglitter = starglitter
        self.five_pity = five_pity
        self.four_pity = four_pity
        self.five_guarantee = five_guarantee
        self.four_guarantee = four_guarantee
        self.debug = debug

    @staticmethod
    def get_five_rate(five_pity):
        if 0 <= five_pity < 75:
            return Rate.BASE_5_STAR
        elif 75 <= five_pity < 90:
            return Rate.SOFT_5_STAR(five_pity)
        else:
            return Rate.HARD_RATE

    @staticmethod
    def get_four_rate(four_pity):
        if 0 <= four_pity < 10:
            return Rate.BASE_4_STAR
        else:
            return Rate.HARD_RATE

    def roll(self):
        inv = Inventory()
        starglitter = self.starglitter
        n = self.rolls
        five_pity = self.five_pity
        four_pity = self.four_pity
        five_guarantee = self.five_guarantee
        four_guarantee = self.four_guarantee

        i = 0
        while i < n:
            five_rate, four_rate = self.get_five_rate(
                five_pity), self.get_four_rate(four_pity)

            if guess(five_rate):  # If 5*
                if guess(0.5) or five_guarantee:  # If featured 5*
                    drop = random.choice(Game.FEATURED_5)
                    five_guarantee = False
                else:  # If standard 5*
                    drop = random.choice(Game.PERMANENT_5)
                    five_guarantee = True
                five_pity = 0
            elif guess(four_rate):  # If 4*
                if guess(0.5) or four_guarantee:  # If featured 4*
                    drop = random.choice(Game.FEATURED_4)
                    four_guarantee = False
                else:
                    if guess(0.5):  # If standard 4* character
                        drop = random.choice(Game.PERMANENT_4)
                    else:  # If 4* wep
                        drop = Game.WEAPON_4
                    four_guarantee = True
                five_pity += 1
                four_pity = 0
            else:
                drop = Game.WEAPON_3
                five_pity += 1
                four_pity += 1

            starglitter += inv.get_reward(drop)
            inv.add(drop)

            # Starglitter recycling
            q, starglitter = divmod(starglitter, 5)
            n += q

            # INCREMENT
            i += 1

        return inv

    def calculate(self):
        total = Inventory()
        featured_copies_spread = {k: 0 for k in range(7 + 1)}
        for i in range(ITERATIONS):
            temp = self.roll()
            total.merge(temp)

            # p.d.f for featured 5*
            featured_copies = temp.five_chars[Game.FEATURED_5[0]
                                              ] if temp.five_chars[Game.FEATURED_5[0]] <= 7 else 7
            featured_copies_spread[featured_copies] += 1

            if self.debug:
                print(f"Progress: {i}/{ITERATIONS}", end="\r")
        avg = total / ITERATIONS
        featured_copies_spread = {
            k: v/ITERATIONS for k, v in featured_copies_spread.items()}

        return avg, featured_copies_spread


# wc = WishCalculator(*get_input(), debug=True)
# avg, featured_copies_spread = wc.calculate()
# print(avg.five_chars, featured_copies_spread)

for x in range(500, 700, 50):
    wc = WishCalculator(x, five_pity=70, five_guarantee=True)
    _, featured_copies_spread = wc.calculate()
    data = map(lambda x: format(x, ".5f"), featured_copies_spread.values())
    with open("./out.csv", "a+") as f:
        f.write(f"{x},{','.join(data)}\n")
