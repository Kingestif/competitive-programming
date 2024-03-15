class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def func(string):
            hashset = set(string)
            if len(string) < 2:
                return ""

            for i in range(len(string)):
                if not(string[i].lower() in hashset and string[i].upper() in hashset):
                    string1 = func(string[:i])
                    string2 = func(string[i+1:])

                    if len(string1) >= len(string2):
                        return string1
                    else:
                        return string2
            return string

        return func(s)
