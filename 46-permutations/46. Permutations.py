class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_perm(seq, initial):
            if len(seq) == 1:
                yield initial + seq
            tested = set()
            for i in range(len(seq)):
                if seq[i] not in tested:
                    tested.add(seq[i])
                    tmp = seq[:]
                    tmp[i] = tmp[0]
                    yield from get_perm(tmp[1:], initial + [seq[i]])
        return get_perm(nums, [])