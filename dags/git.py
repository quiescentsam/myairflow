from git import Repo,remote

rw_dir = '/Users/ssiddiqui/CODE/myairflow'
repo = Repo(rw_dir)

'''Enter code to commit the repository here.
After commit run the following code to push the commit to remote repo.
I am pushing to master branch here'''

origin = repo.remote(name='origin')
origin.push()