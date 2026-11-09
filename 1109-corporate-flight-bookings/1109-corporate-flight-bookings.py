class Solution(object):
    def corpFlightBookings(self, bookings, n):
        events=[]
        

        for first,last,seats in bookings:
            events.append([first,seats])
            events.append(([last+1,-seats]))

        events.sort()
        ans=[0]*(n+1)
        j=0
        total=0

        for i in range(1,n+1):
            while j<len(events) and i==events[j][0]:
                total+=events[j][1]
                j+=1
            ans[i]=total
        
            

        return ans[1:]

        