class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        one = sum(students)
        zero = len(students)-one

        passed = 0
        for sand in sandwiches:
            if sand == 0:
                if zero:
                    zero-=1
                    passed+=1
                else:
                    return len(sandwiches) - passed
            if sand == 1:
                if one:
                    one-=1
                    passed+=1
                else:
                    return len(sandwiches) - passed
        return len(sandwiches) - passed