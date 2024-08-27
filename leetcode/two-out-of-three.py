class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        x = Counter(nums1)
        y = Counter(nums2)
        z = Counter(nums3)

        ans = []

        ls = nums1 + nums2 + nums3
        print(ls)

        for i in ls:
            count = 0
            if i in x:
                count += 1
            if i in y:
                count += 1
            if i in z:
                count += 1

            if count >=2:
                ans.append(i)


        return list(set(ans))

            