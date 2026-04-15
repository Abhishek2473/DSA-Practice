class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)

        st=[] #(temp,idx) pair
        
        #basically, pop out if stack has less temp than the current temp

        for i,t in enumerate(temp):
            while st and t>st[-1][0]:
                tem,idx=st.pop()
                res[idx]=i-idx
            st.append((t,i))
        
        return res
