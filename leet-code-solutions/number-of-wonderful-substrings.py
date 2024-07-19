class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        cnt = defaultdict(int)
        cnt[0] = 1

        ans = 0
        for i in word:
            index = ord(i) - ord("a")
            mask ^= (1<<index)
            ans += cnt[mask]

            for j in range(10):
                premask = mask ^(1 << j)
                ans += cnt[premask]

            cnt[mask] += 1
        return ans