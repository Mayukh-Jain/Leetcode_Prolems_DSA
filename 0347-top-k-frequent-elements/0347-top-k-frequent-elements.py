class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        # heap=[]
        # for num,freq in count.items():
        #     heapq.heappush(heap,(freq,num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [num for freq, num in heap]
        return heapq.nlargest(k,count,key=count.get)