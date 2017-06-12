import requests
from base64 import standard_b64decode


def get_licence(package_names):
    if not isinstance(package_names, (list, tuple)):
        package_names = (package_names, )
    licences = []
    for p in package_names:
        r = requests.get(
            'https://api.github.com/repos/conda-forge/{}-feedstock/readme'.format(p))
        print(r)
        c = standard_b64decode(r.json()['content']).decode("utf-8")
        d = c.split('\n')
        l = [z for z in d if 'Package license' in z][0]
        l = l.split(': ')[-1].split(', ')
        licences.extend(l)
    return licences
if __name__ == '__main__':
    import yaml
    with open('/home/christopher/dev/staged-recipes/recipes/billingegroup-meta/meta.yaml', 'r') as f:
        for i in range(7):
            _ = f.readline()

        a = yaml.load(f)

    print(a)
    b = a['requirements']['run']
    print(b)
    print(set(get_licence(b)))