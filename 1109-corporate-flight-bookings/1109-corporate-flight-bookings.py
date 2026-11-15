class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff=[0]*(n+2)

        for first,last,seats in bookings:
            diff[first]+=seats
            diff[last+1]-=seats

        total=0
        ans=[]

        for i in range(1,n+1):
            total+=diff[i]
            ans.append(total)

        return ans


        