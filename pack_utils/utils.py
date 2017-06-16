import requests
import fire


def main(user, password):
    r = requests.get('https://api.github.com/user/teams',
                     auth=(str(user), str(password)))
    a = r.json()
    b = [c for c in a if 'conda-forge' in c['organization']['html_url']]
    d = [(z['name'], z['organization']['html_url']) for z in b if z['name'] != 'all-members']
    d.sort()

    template = '|[{name}]({org}/{name}-feedstock) | [![Anaconda-Server Badge]' \
               '(https://anaconda.org/conda-forge' \
               '/{name}/badges/downloads.svg)]' \
               '(https://anaconda.org/conda-forge/{name}) | {linux} | {osx} | {windows} |\n'
    linux = '[![Circle CI](https://circleci.com/gh/conda-forge/{name}-feedstock.svg?style=shield)](https://circleci.com/gh/conda-forge/{name}-feedstock)'
    osx = '[![TravisCI](https://travis-ci.org/conda-forge/{name}-feedstock.svg?branch=master)](https://travis-ci.org/conda-forge/{name}-feedstock)'
    windows = '[![AppVeyor](https://ci.appveyor.com/api/projects/status/github/conda-forge/{name}-feedstock?svg=True)](https://ci.appveyor.com/project/conda-forge/{name}-feedstock/branch/master)'

    with open('../readme.md', 'w') as f:
        f.write('## Packages I help to maintain\n')
        f.write('| Package | Downloads | Linux | OSX | Windows |\n')
        f.write('|:---------:|:--------:|:---------:|:--------:|:---------:|\n')
        l = [template.format(linux=linux, osx=osx, windows=windows, name=i,
                             org=j).format(name=i, org=j) for i, j in d]
        f.writelines(l)
        f.write('\n\n')
        f.write("""Feel free to use this script, you just need to provide your GitHub username, 
and password/token.

`python utils.py USERNAME PASSWORD`""")


if __name__ == '__main__':
    fire.Fire(main)
