#Sweep Line Algorithm(pair)
class Solution(object):
    def carPooling(self, trips, capacity):
        arr=[]
        for passenger,first,last in trips:
            arr.append([first,passenger])
            arr.append([last,-passenger])
            #note we used last instead of last+1,because the passengers left at index last

        cumsum=0
        arr.sort()
        for i in range(len(arr)):
            cumsum+=arr[i][1]
            if cumsum>capacity:
                return False
        return True
        

        
        