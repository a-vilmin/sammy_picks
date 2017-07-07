from sys import argv
import league


def knapsack(players, max_salary):
    return []


def main():
    players = league.League(argv[1])
    x = [len(l) for _, l in players.players.items()]
    i = x[0]
    for y in x[1:]:
        i *= y
    print(i)


if __name__ == '__main__':
    main()
