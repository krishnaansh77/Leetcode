class Solution(object):
    def checkRecord(self, s):
        dict = {'L': 0, 'A': 0}

        for x in s:

            if x != 'L':
                dict['L'] = 0
            else:
                dict['L'] += 1

            if x == 'A':
                dict['A'] += 1

            if dict['A'] >= 2:
                return False

            if dict['L'] == 3:
                return False

        return True

            
        