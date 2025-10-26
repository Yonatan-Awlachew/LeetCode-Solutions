class Solution:
    def defangIPaddr(self, address: str) -> str:
        result=list(address)
        for x in range(len(result)):
            if result[x]==".": result[x]="[.]"
        return "".join(result)
