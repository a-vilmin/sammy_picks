import player
from collections import defaultdict


class League():

    def __init__(self, players_csv, expected_hitters, expected_pitchers):
        self.players = defaultdict(list)

        with open(players_csv, 'r') as f:
            for line in f.readlines()[1:]:
                curr = player.Player(line)
                if "/" not in curr.pos:
                    self.players[curr.pos] += [curr]
                else:
                    self.players[curr.pos.split('/')[0]] += [curr]
                    self.players[curr.pos.split('/')[1]] += [curr]

        rates = defaultdict(float)
        with open(expected_hitters) as f:
            for line in f.readlines()[1:]:
                curr = [x.replace("\"", "") for x in line.split(',')]
                rates[curr[0]] = float(curr[-2])

        with open(expected_pitchers) as f:
            for line in f.readlines()[1:]:
                curr = [x.replace("\"", "") for x in line.split(',')]
                rates[curr[0]] = float(curr[-2])

        for _, p in self.players.items():
            for each in p:
                each.avg = rates[each.name]
                if each.avg == 0:
                    p.remove(each)


if __name__ == '__main__':
    import sys

    league = League(sys.argv[1], sys.argv[2])
    print([(x.name, x.avg) for x in league.players['SP']])
