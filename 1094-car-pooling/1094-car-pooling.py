class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        sorted_trips = []
        for i in trips:
            if i[2] < i[1]:
                return False
            sorted_trips.append([i[1], i[2], i[0]])
        sorted_trips.sort()
        
        curr_passengers = 0
        current_drop_offs = [] # append (destination, num_passengers)
        heapq.heapify(current_drop_offs)
        # simulate the trip
        for stop in sorted_trips:
            # drop off existing ppl if possible
            while current_drop_offs:
                if current_drop_offs[0][0] <= stop[0]:
                    curr_passengers -= current_drop_offs[0][1]
                    heapq.heappop(current_drop_offs)
                else:
                    break
            # pick up the ppl at current stop
            curr_passengers += stop[2]
            heapq.heappush(current_drop_offs, (stop[1], stop[2]))
            if curr_passengers > capacity:
                return False
        
        return True
            
        