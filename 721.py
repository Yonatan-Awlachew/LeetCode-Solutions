class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self,n):
        p = self.parent[n]
        while p!=self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self,a,b):
        p1,p2 = self.find(a),self.find(b)
        if p1==p2: return False
        
        if self.rank[p1]>self.rank[p2]: self.parent[p2]=p1
        elif self.rank[p2]>self.rank[p1]: self.parent[p1]=p2
        else:
            self.parent[p2]=p1
            self.rank[p1]+=1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_id = {}
        email_name = {}
        id = 0

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in email_id:
                    email_id[email]=id
                    email_name[email]=name
                    id+=1

        UF = UnionFind(id)

        for acc in accounts:
            first = acc[1]
            for email in acc[2:]:
                UF.union(email_id[first],email_id[email])

        groups = {}
        for email,index in email_id.items():
            root = UF.find(index)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)
        
        result = []
        for emails in groups.values():
            name = email_name[emails[0]]
            result.append([name] + sorted(emails))
        return result
