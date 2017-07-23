from sys import argv
import league
import evolution


def main():
    players = league.League(argv[1], argv[2], argv[3])
    evolution.run(players)


if __name__ == '__main__':
    main()
