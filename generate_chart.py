import matplotlib.pyplot as plt
import numpy as np
from github import Github
import os

# Get GitHub token from environment
token = os.getenv("GITHUB_TOKEN")
username = "syedmukheeth"

# Authenticate with GitHub API
g = Github(token)
user = g.get_user(username)

# Get contribution data (example: commits, PRs, issues, code reviews)
commits = sum(1 for _ in user.get_repos() for _ in _.get_commits(author=user))
prs = sum(1 for _ in user.get_pulls(state="all"))
issues = sum(1 for _ in user.get_issues(state="all"))
reviews = 0  # GitHub API doesn't give direct count easily

# Calculate percentages
total = commits + prs + issues + reviews
if total == 0:
    total = 1  # avoid division by zero

values = [
    round((commits / total) * 100, 1),
    round((prs / total) * 100, 1),
    round((issues / total) * 100, 1),
    round((reviews / total) * 100, 1),
]

labels = ["Commits", "Pull Requests", "Issues", "Code Reviews"]

# Radar chart setup
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles, values, color="lime", linewidth=2)
ax.fill(angles, values, color="lime", alpha=0.3)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.savefig("github-stats.svg", format="svg")
