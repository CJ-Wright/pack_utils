import requests
import fire

def main(user, password):
    r = requests.get('https://api.github.com/user/teams', auth=(str(user), str(password)))
    a = r.json()
    b = [c for c in a if 'conda-forge' in c['organization']['html_url']]
    d = [z['name'] for z in b if z['name'] != 'all-members']
    d.sort()

    template = '|{} | [![Anaconda-Server Badge](https://anaconda.org/conda-forge' \
               '/{}/badges/downloads.svg)]' \
               '(https://anaconda.org/conda-forge/{}) |\n'

    with open('../readme.md', 'w') as f:
        f.write('## Packages I help to maintain\n')
        f.write('| Package | Downloads |\n')
        f.write('|:---------:|:--------:|\n')
        f.writelines([template.format(i, i, i) for i in d])
        f.write('\n\n')
        f.write("""Feel free to use this script, you just need to provide your GitHub username, 
and password/token.

`python utils.py USERNAME PASSWORD`""")

if __name__ == '__main__':
    fire.Fire(main)