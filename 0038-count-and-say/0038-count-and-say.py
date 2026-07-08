class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: 
            return "1"
        
        current_string = "1"
        
        for _ in range(n - 1):
            next_string = ""
            count = 1
            
            for i in range(1, len(current_string)):
                if current_string[i] == current_string[i - 1]:
                    count += 1
                else:
                    next_string += str(count) + current_string[i - 1]
                    count = 1
            
            next_string += str(count) + current_string[-1]
            
            current_string = next_string
            
        return current_string