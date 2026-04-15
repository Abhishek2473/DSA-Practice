class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        count1=[0]*26
        count2=[0]*26
        #compare first characters of s2 as s1 length
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')]+=1
            count2[ord(s2[i]) - ord('a')]+=1
        
        if count1==count2:
            return True
        
        #slide the s2 window now

        for i in range(len(s1),len(s2)):
            if count1==count2:
                return True
            count2[ord(s2[i])- ord('a')]+=1 #increasing count
            count2[ord(s2[i-len(s1)] ) - ord('a')]-=1 #removing other elements
        
        return count1==count2


        