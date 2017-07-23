class Player():

    def __init__(self, player_entry):
        parsed = player_entry.strip().split(',')
        self.pos = parsed[0][1:-1]
        self.name = parsed[1].replace("\"", "")
        self.price = int(parsed[2])
        self.matchup = parsed[3]
        self.avg = 0
        self.team = parsed[5]

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name and self.team == other.team

    def __hash__(self):
        return hash(self.name+self.team)

    def get_vals(self):
        return self.avg, self.price
