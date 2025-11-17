class Solution:
    def decodeString(self, s: str) -> str:
        numstack,strstack = [],[]
        curr_string,curr_num = "",0
        
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num*10 + int(ch)
            elif ch=="[":
                strstack.append(curr_string)
                numstack.append(curr_num)
                curr_string = ""
                curr_num = 0
            elif ch=="]":
                num = numstack.pop()
                prev = strstack.pop()
                curr_string = prev + curr_string*num
            else:
                curr_string += ch
        return curr_string
