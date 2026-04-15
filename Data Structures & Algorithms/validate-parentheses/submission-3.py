class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        valid={ ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in "{[(":
                st.append(i)
            elif st and st[-1]==valid[i]:
                st.pop()
            else:
                return False
        return st==[]

        