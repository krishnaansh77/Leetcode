class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        event=[]

        for passenger,first,last in trips:
            event.append([first,passenger])
            event.append([last,-passenger])

        event.sort()
       
        cumsum=0

        for i in range(len(event)):
            cumsum+=event[i][1]
            if cumsum>capacity:
                return False
        return True


        