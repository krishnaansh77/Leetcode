class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        n=len(people)
        left=0
        right=n-1
        count=0
        while left<=right:
            w=people[left]+people[right]
            if w<=limit:
                count+=1
                left+=1
                right-=1
            else:
                count+=1
                right-=1
        return count


        
        