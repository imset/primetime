import sys
import math
import random

def primeTime(arg1):
	cnt = 2
	primeChk = "is PRIME"
	if int(arg1) < 0:
		print("NOTE: Negatives are not traditionally considered able to be prime.")
	print(arg1)
	while cnt <= math.sqrt(abs(int(arg1))) and arg1 != '1':
		if (cnt % 3 == 0 and cnt != 3) or (cnt % 5 == 0 and cnt != 5) or (cnt % 7 == 0 and cnt != 7):
			cnt += 2
		elif int(arg1) % cnt != 0:
			primeChk = "is PRIME"
			if cnt == 2:
				cnt += 1
			else:
				cnt += 2
		elif primeChk == "is PRIME" and cnt == arg1:
			break
		else:
			primeChk = "is NOT PRIME due to ", cnt
			break
	if arg1 == '1' or arg1 == '0':
		primeChk = "is neither PRIME nor COMPOSITE"
	return ''.join(map(str,primeChk))

if __name__ == '__main__':
	try:
		print(primeTime(sys.argv[1]))
	except IndexError:
		print(primeTime(random.randint(3,300000)))
