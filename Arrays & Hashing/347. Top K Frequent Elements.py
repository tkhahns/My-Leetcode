class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        res = []
        for i in range(k):
            max_count = 0
            key = 0
            for j in mydict:
                if mydict[j] > max_count:
                    max_count = mydict[j]
                    key = j
            res.append(key)
            mydict.pop(key, None)
        return res
            