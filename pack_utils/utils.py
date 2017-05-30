import requests

r = requests.get('https://api.github.com/user/teams', auth=("user", "pass"))
a = r.json()
b = [c for c in a if 'conda-forge' in c['organization']['html_url']]
d = [z['name'] for z in b if z['name'] != 'all-members']

template = '|{} | [![Anaconda-Server Badge](https://anaconda.org/conda-forge' \
           '/{}/badges/downloads.svg)]' \
           '(https://anaconda.org/conda-forge/{}) |\n'

with open('../readme.md', 'w') as f:
    f.write('## Packages I help to maintain\n')
    f.write('| Package | Downloads |\n')
    f.write('|:---------:|:--------:|\n')
    f.writelines([template.format(i, i, i) for i in d])