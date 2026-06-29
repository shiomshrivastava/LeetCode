# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0

#         # Build LPS array
#         lps = [0] * len(needle)
#         prev = 0
#         i = 1

#         while i < len(needle):
#             if needle[i] == needle[prev]:
#                 prev += 1
#                 lps[i] = prev
#                 i += 1
#             else:
#                 if prev != 0:
#                     prev = lps[prev - 1]
#                 else:
#                     lps[i] = 0
#                     i += 1

#         # Search using KMP
#         i = j = 0

#         while i < len(haystack):
#             if haystack[i] == needle[j]:
#                 i += 1
#                 j += 1

#                 if j == len(needle):
#                     return i - j
#             else:
#                 if j != 0:
#                     j = lps[j - 1]
#                 else:
#                     i += 1

#         return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)