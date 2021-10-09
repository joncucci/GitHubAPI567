import json, requests

base = 'https://api.github.com/'
token = 'TOKEN HERE'

'''
params = {"state": "open",}
headers = {'Authorization': f'token {token}'}
'''

'''
Add to base:
For list of repo names:
users/<ID>/repos

For list of commits:
repos/<ID>/<REPO>/commits
'''

def get_repos(id):

    output = {}

    # If API key is present
    # info = requests.get(base + 'users/{}/repos?page=1&per_page=1000'.format(id), headers=headers, params=params).json()

    # If not
    info = requests.get(base + 'users/{}/repos?page=1&per_page=1000'.format(id))
    if type(info) not in [dict, list, tuple]:
        info = info.json()

    for repo in info:

        # If API key is present
        # commits = requests.get(base + 'repos/{}/{}/commits?page=1&per_page=1000'.format(id, repo['name']), headers=headers, params=params).json()

        # If not
        # print(repo)
        commits = requests.get(base + 'repos/{}/{}/commits?page=1&per_page=1000'.format(id, repo['name']))

        if type(commits) not in [dict, list, tuple]:
                commits = commits.json()
        output[repo['name']] = len(commits)

        print('Repo: {} Number of commits: {}'.format(repo['name'], len(commits)))
    return output

# get_repos('joncucci')
