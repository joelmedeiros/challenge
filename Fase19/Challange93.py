data = {}
data['name'] = str(input('Player name: '))
matches = int(input('Matches played: '))
goals = []
for m in range(0, matches):
    goal = int(input(f'How many goals in the match {m}?'))
    goals.append(goal)

data['goals'] = goals
data['total'] = sum(goals)

print('~=' * 30)
print(data)
print('~=' * 30)
for k, v in data.items():
    print(f'The field {k} has the value {v}')
print('~=' * 30)

print(f'The {data["name"]} has played {matches}:')
for k, v in enumerate(data['goals']):
    print(f'On the match {k}, made {v} goals.')
print(f'In a total of {data["total"]} goals')