class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        if '{' not in expression:
            return [expression]
        
        right = expression.find('}')
        left = expression.rfind('{', 0, right)
        
        parts = expression[left + 1:right].split(',')
        
        res = set()
        for part in parts:
            new_expr = expression[:left] + part + expression[right + 1:]
            res.update(self.braceExpansionII(new_expr))
            
        return sorted(list(res))