# s = input("Enter the string: ")
# p = input("Enter the pattern: ")

# idxS = 0
# idxP = 0
# star_idx = -1
# string_temp_idx = -1

# while idxS < len(s):
#     if idxP + 1 < len(p) and p[idxP + 1] == '*':
#         star_idx = idxP
#         s_match_idx = idxS
#         idxP += 2
#     elif idxP < len(p) and (p[idxP] == s[idxS] or p[idxP] == '.'):
#         idxS += 1
#         idxP += 1
#     elif star_idx != -1:
#         if p[star_idx] == s[s_match_idx] or p[star_idx] == '.':
#             s_match_idx += 1
#             idxS = s_match_idx
#             idxP = star_idx + 2
#         else:
#             print("\nMatch: False")
#             exit()
#     else:
#         print("\nMatch: False")
#         exit()
# while idxP + 1 < len(p) and p[idxP + 1] == '*':
#     idxP += 2

# if idxP == len(p):
#     print("\nMatch: True")
# else:
#     print("\nMatch: False")

s = input("Enter the string: ")
p = input("Enter the pattern: ")
dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
print(dp)
dp[0][0] = True
for j in range(1, len(p) + 1):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]
for i in range(1, len(s) + 1):
    for j in range(1, len(p) + 1):
        if p[j - 1] == s[i - 1] or p[j - 1] == '.':
            dp[i][j] = dp[i - 1][j - 1]
        elif p[j - 1] == '*':
            dp[i][j] = dp[i][j - 2]
            if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                dp[i][j] = dp[i][j] or dp[i - 1][j]
        else:
            dp[i][j] = False
match_result = dp[len(s)][len(p)]
print(f"\nString: '{s}'")
print(f"Pattern: '{p}'")
print(f"Match: {match_result}")