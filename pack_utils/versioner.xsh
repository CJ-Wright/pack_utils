import requests

def main(user, password):
    # get all the packages for the user
    gr = requests.get('https://api.github.com/user/teams',
                      auth=(str(user), str(password)))
    a = gr.json()
    b = [c for c in a if 'conda-forge' in c['organization']['html_url']]
    d = [z['name'] for z in b if z['name'] != 'all-members']
    for s in d:
        feedstockrot @(s)
