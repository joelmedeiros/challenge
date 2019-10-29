def stats(name = '<unknown>', goals = 0):
    print(f'The player {name} has made {goals} goal(s) on the championship.')


name = str(input('Player name: '))
goals = str(input('Number of goals: '))
if (goals.isnumeric()):
    goals = int(goals)
else:
    goals = 0

if name.strip() == '':
    stats(goals=goals)
else:
    stats(name, goals)