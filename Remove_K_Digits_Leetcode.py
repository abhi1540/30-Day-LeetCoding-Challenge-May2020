def removeKdigits(self, num: str, k: int) -> str:

	if len(num) == k:
		return "0"
	
	stack = []
	count = 0
	for i in num:
		while k and stack and stack[-1] > i:
			stack.pop(-1)
			k -= 1
		stack.append(i)
	res = ("".join(stack[0:len(stack)-k])).lstrip("0")
	if len(res):
		return res
	return "0"
        