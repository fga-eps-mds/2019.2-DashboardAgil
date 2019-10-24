from github import Github

# using username and password
g = Github("user", "password")

# Then play with your Github objects:
repo = g.get_user().get_repo("asdasdasdasd")
commit = repo.get_commit(sha=sha)
print(commit.commit.author.date)


