import player
from collections import defaultdict


class League():

    def __init__(self, players_csv):
        self.players = defaultdict(list)

        with open(players_csv, 'r') as f:
            for line in f.readlines()[1:]:
                curr = player.Player(line)
                if "/" not in curr.pos:
                    self.players[curr.pos] += [curr]
                else:
                    self.players[curr.pos.split('/')[0]] += [curr]
                    self.players[curr.pos.split('/')[1]] += [curr]


if __name__ == '__main__':
    import sys

    league = League(sys.argv[1])
    print([x for x, y in league.players.items()])
