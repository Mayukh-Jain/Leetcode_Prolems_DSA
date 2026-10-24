class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_days(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_month[:month - 1]) + day
        
        alice_start = date_to_days(arriveAlice)
        alice_end = date_to_days(leaveAlice)
        bob_start = date_to_days(arriveBob)
        bob_end = date_to_days(leaveBob)
        
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        
        return 0