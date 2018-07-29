class Solution:
    def twoSum(self, target, num):
        dict={}
        for i in xrange(len(num)):
            x=num[i]
            if target-x in dict:
                    return(dict[target-x]+1,i+1)
            dict[x]=i

aa=Solution()
print aa.twoSum(2,[1,1,2,3,5])

