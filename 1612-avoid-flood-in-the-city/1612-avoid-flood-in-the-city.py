from sortedcontainers import SortedList

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(rains)
        sunny_days = SortedList()
        full_lakes = {}

        for i in range(len(rains)):
            rain = rains[i]
            if rain == 0:
                sunny_days.add(i)
            else:
                if rain in full_lakes:
                    last_rain_day = full_lakes[rain]
                    idx = sunny_days.bisect_right(last_rain_day)

                    if idx == len(sunny_days):
                        return []
                    
                    dry_day = sunny_days[idx]
                    ans[dry_day] = rain
                    sunny_days.remove(dry_day)
                
                ans[i] = -1
                full_lakes[rain] = i
        return ans
            


        