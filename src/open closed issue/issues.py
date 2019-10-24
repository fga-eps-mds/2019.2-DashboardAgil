from github import Github

#  username and password
g = Github("KalebeLopes", "")

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

    #   TODAS AS ISSUES 

repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
open_issues = repo.get_issues(state='all')
for issue in open_issues:
    print(issue)


#   ISSUES CREATOR 

repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
open_issues = repo.get_issues(creator='Matheus-AM')
for issue in open_issues:
    print(issue)