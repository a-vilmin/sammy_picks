from random import choice, sample, random, randint
import tqdm


LINEUP_SIZE = 10


def choose_cand(players, pos):
    if pos == 'OF':
        cand = sample(players, 3)
    elif pos == "SP":
        cand = sample(players, 2)
    else:
        cand = [choice(players)]
    return cand


def create_single_lineup(league):
    lineup = []
    positions = []

    for pos, players in league.players.items():
        if pos == 'RP':
            continue
        else:
            cand = choose_cand(players, pos)

            while True:
                if len([x for x in cand if x in lineup]) == 0:
                    lineup += cand
                    positions += [pos] * len(cand)
                    break
                cand = choose_cand(players, pos)
    return lineup, positions


def population(league, size):
    lineups = []
    positions = []
    while(size):
        l, p = create_single_lineup(league)
        lineups += [l]
        positions = p
        size -= 1
    return lineups, positions


def fitness(lineup, salary_cap):
    total = sum([x.price for x in lineup])
    if total > salary_cap:
        return 0
    else:
        return sum([x.avg for x in lineup])


def evolve(lineups, salary_cap, retain=0.2, random_sel=0.05, mutate=0.01):
    graded = [(fitness(x, salary_cap), x) for x in lineups]
    graded = [x[1] for x in sorted(graded)][::-1]

    ret_len = int(len(graded)*retain)
    parents = graded[:ret_len]
    parents += [x for x in graded[ret_len:] if random_sel > random()]

    for lineup in parents:
        if mutate > random():
            lineup_choice = randint(0, len(lineups) - 1)
            lineup_pos = randint(0, LINEUP_SIZE-1)
            if lineups[lineup_choice][lineup_pos] not in lineup:
                lineup[lineup_pos] = lineups[lineup_choice][lineup_pos]

    parents_len = len(parents)
    children = []
    while len(children) < len(lineups) - parents_len:
        male, female = sample(range(0, parents_len), 2)
        male_genes = parents[male]
        female_genes = parents[female]

        half = int(LINEUP_SIZE/2)
        child = male_genes[:half] + female_genes[half:]
        children += [child]

    return parents + children


def run(league):
    lineups, positions = population(league, 10000)

    for _ in tqdm.trange(1000):
        lineups = evolve(lineups, 50000)

    graded = [(fitness(x, 50000), x) for x in lineups]
    graded = [x[1] for x in sorted(graded)][::-1][0]

    for i in range(LINEUP_SIZE):
        curr = graded[i]
        print(curr.name+" at "+positions[i]+" with "+str(curr.avg))

    print("Total Points = "+str(fitness(graded, 50000)))
    print("Total Cost = "+str(sum([x.price for x in graded])))
