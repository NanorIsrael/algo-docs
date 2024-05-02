def is_match(s, p):
	if not p:
		return not s
	first_match = bool(s) and (s[0] == p[0] or p[0] == '.')
	
	if len(p) >= 2 	and p[1] == '*':
		case1 = is_match(s, p[2:])
		case2 = first_match and is_match(s[1:], p)
		return case1 or case2
	return first_match and is_match(s[1:], p[1:])


print(is_match("aa", "a"))      # False
print(is_match("aa", "a*"))     # True
print(is_match("ab", ".*"))     # True
print(is_match("aab", "c*a*b")) # True

print('--------------------------->')
# Example usage:
text = "aab"
pattern = "c*a*b"
result = is_match(text, pattern)
print(result)  # Output: True

# Example usage:
text = "aa"
pattern = "a"
result = is_match(text, pattern)
print(result)  # Output: True

# Example usage:
text = "aa"
pattern = "a*"
result = is_match(text, pattern)
print(result)  # Output: True

# Example usage:
text = "ab"
pattern = ".*"
result = is_match(text, pattern)
print(result)  # Output: True
print("----->", bool("result"))  # Output: True
