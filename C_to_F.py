unit = input('輸入的單位(C or F): ')
if unit == 'C':
	degree_C = input('攝氏幾度: ')
	degree_C = float(degree_C)
	ans = degree_C*9/5+32
	ans = float(ans)
	print(ans, 'F')
	if ans >= 89:
		print('別出門，會熱死')
if unit == 'F':
	degree_F = input('華氏幾度: ')
	degree_F = float(degree_F)
	ans = (degree_F-32)/9*5
	ans = float(ans)
	print(ans, 'C')
	if ans >= 31:
		print('別出門，會熱死')