from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass

    def comparator(a, b):
        checker = Checker()
        return checker.compare(a, b)


class Checker:
    def compare(self, a: Player, b: Player):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            if a.name < b.name:
                return -1
            else:
                return 1

        return 0


with open("./in") as fp:
    while line := fp.readline():
        n = int(line.strip())
        data = []
        for i in range(n):
            line = fp.readline()
            name, score = line.split()
            score = int(score)
            player = Player(name, score)
            data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
