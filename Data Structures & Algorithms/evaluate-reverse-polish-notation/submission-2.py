class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]

        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            else:
                a=st.pop()
                b=st.pop()
                if i=='+':
                    st.append(b+a)
                elif i=='-':
                    st.append(b-a)
                elif i=='*':
                    st.append(b*a)
                elif i=='/':
                    st.append(int(b/a))  # truncate toward 0

        return st[0]
