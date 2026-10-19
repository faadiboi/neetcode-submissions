class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm = {}
        for i in nums:
            hashm[i] =hashm.get(i,0)+1
        freq= [[] for i  in range(len(nums)+1)]
        for ky , v in hashm.items():
            freq[v].append(ky)
        
        res = []
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                res.append(n)

                if len(res)==k:
                    return res