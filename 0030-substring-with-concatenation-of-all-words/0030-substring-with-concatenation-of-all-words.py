class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []

        wc = {}
        for word in words:
            wc[word] = wc.get(word, 0) + 1

        result=[]

        for i in range(word_len):
            left = i
            right = i
            seen = {}
            count = 0
            
            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len
                
                if word in wc:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    
                    while seen[word] > wc[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == num_words:
                        result.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right
                    
        return result