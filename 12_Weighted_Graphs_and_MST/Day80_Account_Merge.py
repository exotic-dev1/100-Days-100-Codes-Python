"""
Day80 :- Accounts Merge
Difficulty :- Medium
Concepts :- union find, hashmap, graphs
"""
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px != py:
            self.parent[py] = px


class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        uf = UnionFind(n)

        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        groups = defaultdict(set)

        for email, acc_idx in email_to_account.items():
            parent = uf.find(acc_idx)
            groups[parent].add(email)

        result = []

        for parent, emails in groups.items():
            name = accounts[parent][0]
            result.append([name] + sorted(emails))

        return result

accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]

sol = Solution()

merged_accounts = sol.accountsMerge(accounts)

print("Merged Accounts:\n")

for account in merged_accounts:
    print(account)