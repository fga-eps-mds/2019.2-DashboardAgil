from github import Github

#  username and password
g = Github("KalebeLopes", "Kalebe1230,123")

#   ISSUES ABERTAS 

repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
open_issues = repo.get_issues(state='open')
for issue in open_issues:
    print(issue)


#   ISSUES FECHADAS 

repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
open_issues = repo.get_issues(state='closed')
for issue in open_issues:
    print(issue)


#   ISSUES FECHADAS 

repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
open_issues = repo.get_issues(creator='github.KalebeLopes.KalebeLopes')
for issue in open_issues:
    print(issue)