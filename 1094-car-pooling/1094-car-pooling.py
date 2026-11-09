class Solution(object):
    def carPooling(self, trips, capacity):
        current=[0]*1001

        for passengers,start,end in trips:
            current[start]+=passengers
            current[end]-=passengers

        maximum=max(trip[2]for trip in trips)
        total_passengers=0

        for i in range(maximum+1):
            total_passengers+=current[i]
            if total_passengers>capacity:
                return False
        return True

        