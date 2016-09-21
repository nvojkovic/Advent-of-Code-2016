import itertools

def win(players):
	turn = 0
	while players[0]['hitpoints'] > 0 and players[1]['hitpoints'] > 0:
		damage = max(players[turn]['damage'] - players[1-turn]['armor'], 1)
		players[1-turn]['hitpoints'] -= damage
		turn = 1-turn
	return players[0]['hitpoints'] > 0

weapons = [[8,4],[10,5],[25,6],[40,7],[74,8]]
armors = [[13,1],[31,2],[53,3],[75,4],[102,5],[0,0]]
rings = [[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3],[0,0,0]]
costs = []

for weapon in weapons:
	for armor in armors:
		for ring1, ring2 in itertools.product(rings,rings):
			player = {"hitpoints": 100}
			boss = {"hitpoints": 104, "damage": 8, "armor": 1}

			player['damage'] = weapon[1] + ring1[1] + ring2[1]
			player['armor'] = armor[1] + ring1[2] + ring2[2]
			cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
			
			if(win([player, boss])):
				costs.append(cost)
print(min(costs))
