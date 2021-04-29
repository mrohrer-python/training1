class Player ():
    def __init__(self, first_name, last_name, height_cm, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight = weight

    def weight_to_lbs(self):
        pounds = self.weight * 2.29487534
        return pounds

class GolfPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight, points, handicap, tournaments):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight=weight)
        self.points = points
        self.handicap = handicap
        self.tournaments = tournaments

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight, goals, red_cards, yellow_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight=weight)
        self.goals = goals
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards

markus_golfobj = GolfPlayer(first_name="Markus", last_name="Angermann", height_cm=191, weight=89, points=50, handicap=32, tournaments=2)
petra_golfobj = GolfPlayer(first_name="Petra", last_name="Muster", height_cm=165, weight=65, points=44, handicap=3, tournaments=40)
print(markus_golfobj.handicap)
print(petra_golfobj.last_name)
golf_player =[markus_golfobj, petra_golfobj]
for player in golf_player:
    print(player.last_name + " " + str(player.handicap))

print(petra_golfobj.weight_to_lbs())

ronaldo = FootballPlayer(first_name="Christiano", last_name="Ronaldo", height_cm=178, weight=80, goals=400, red_cards=20, yellow_cards=50)
print(ronaldo.yellow_cards)