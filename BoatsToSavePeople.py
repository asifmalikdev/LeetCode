class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i = 0
        j = len(people)-1
        counter = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i+=1
                j-=1
                counter+=1
            elif people[j] == limit:
                counter +=1
                j-=1
            else:
                j-=1
                counter +=1
        return counter

                
people = [3,5,3,4]
limit = 5
obj = Solution()
print(obj.numRescueBoats(people, limit))