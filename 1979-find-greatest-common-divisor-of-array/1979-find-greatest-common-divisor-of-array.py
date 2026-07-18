class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums=set(nums)
        return gcd(max(nums),min(nums))
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a