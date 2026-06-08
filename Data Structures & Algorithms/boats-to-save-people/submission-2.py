class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)

        l, r = 0, len(people) - 1
        count = 0

        while l <= r:
            space = limit - people[r]
            r -= 1
            count += 1

            if l <= r and space >= people[l]:
                l += 1

        return count