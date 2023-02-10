class Solution:
    import collections
    def dividePlayers(self, skill: List[int]) -> int:
        ans = sum(skill)//(len(skill)//2)
        cnt = collections.Counter(skill)
        result = 0
        for k, v in cnt.items():
            if ans-k not in cnt or cnt[ans-k] != cnt[k]:
                return -1
            result += k*(ans-k)*v
        return result//2
        
