from urllib3 import PoolManager, exceptions
http = PoolManager()
site = 'www.google.com'
try:
    http.request('GET', site)
except exceptions.HTTPError as e:
    print(f'\033[0;31mThe site `{site}` is not available. \033[m')
else:
    print(f'\033[0;32mThe site `{site}` is accessible. \033[m')