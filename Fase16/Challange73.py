league = 'Palmeiras', 'Santos', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Internacional', 'Athletico-PR', 'Botafogo', 'Goiás', 'Corinthians', 'Grêmio', 'Bahia', 'Ceará', 'Fortaleza', 'Vasco', 'Cruzeiro', 'Fluminense', 'Chapecoense', 'CSA', 'Avaí'

print('The first ones are: {}'.format(league[0:5]))
print('The last ones are: {}'.format(league[-4:]))
print('The teams sorted: {}'.format(sorted(league)))
print('The chapecoense team is in {} position'.format(league.index('Chapecoense')+1))