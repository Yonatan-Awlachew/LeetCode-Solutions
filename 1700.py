class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        count = {}

        for x in students:
            if x not in count:
                count[x]=0
            count[x]+=1
        
        for s in sandwiches:
            if count.get(s,0)>0:
                result-=1
                count[s]-=1
            else:
                return result
        return result
