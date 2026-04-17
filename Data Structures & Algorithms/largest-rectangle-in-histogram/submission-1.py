class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea=0
        st=[]

        for i,h in enumerate(heights):
            start=i
            while st and h<st[-1][1]:
                idx,ht=st.pop()
                maxArea=max(maxArea,ht*(i-idx))
                start=idx
            st.append((start,h))
        
        for i,h in st:
            maxArea=max(maxArea,h*(len(heights)-i))
        return maxArea