class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        master_str = "123456789"
        result = []
        
        low_len = len(str(low))
        high_len = len(str(high))
        
        for length in range(low_len, high_len + 1):
            for start_idx in range(10 - length):
                num = int(master_str[start_idx:start_idx + length])
                
                if low <= num <= high:
                    result.append(num)
                    
        return result