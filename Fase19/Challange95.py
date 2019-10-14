data = {}
players = []
goon = True
while goon:
    data['name'] = str(input('Player name: '))
    matches = int(input('Matches played: '))
    goals = []
    for m in range(0, matches):
        goal = int(input(f'How many goals in the match {m}?'))
        goals.append(goal)

    data['goals'] = goals
    data['total'] = sum(goals)

    players.append(data.copy())
    goon = str(input('Do you want to continue? [y/n]')) in 'yY'

print('-=' * 23)
print(f'id{"name":>10}{"goals":>15}{"total":>15}')
print('-'*46)
for key, player in enumerate(players):
    print(f'{key} {player["name"]:^20} {player["goals"]} {player["total"]:>15}')
print('-'*46)

while True:
    playerKey = int(input('What player do you want do see the details?'))
    if (playerKey == 999):
        break

    for k, player in enumerate(players):
        if (k == playerKey):
            print(f'Showing details of {player["name"]} player: ')
            for k, goal in enumerate(player['goals']):
                print(f'On the match {k}, made {goal} goals.')
            print('-'*46)

    # print('ERROR: Player not found! Try again')

print('Done')