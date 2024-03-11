class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_collection = collections.defaultdict(int)
        order_set = set(order)
        other_char_stack = []
        for elem in s:
            if elem in order_set:
                order_collection[elem]+=1
            else:
                other_char_stack.append(elem)
        return ''.join([char*order_collection[char] for char in order]) + ''.join(other_char_stack)