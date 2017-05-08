#PROBLEM

"""Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit. """

import time
start_time = time.time()


sq_num = 0

limit = 19
max_range = int(1929394959697989990 **.5) # Replace all _ with 9s to get the max value
min_range = int(1020304050607080900 **.5) # Replace all _ with 0s to get the min value
num = min_range
count = 0
while num <= max_range :
	sq_num = num*num
	if len(str(sq_num)) == limit and str(sq_num)[0] == '1' and str(sq_num)[2] == '2' and str(sq_num)[4] == '3' and str(sq_num)[6] == '4' and str(sq_num)[8] == '5' and str(sq_num)[10] == '6' and str(sq_num)[12] == '7' and str(sq_num)[14] == '8' and str(sq_num)[16] == '9' and str(sq_num)[18] == '0' :
		print('Found it {}'.format(num))
		break
	elif len(str(sq_num)) > limit:
		print('Exceeded')
		break
	else:
		num += 10
print("--- %s seconds ---" % (time.time() - start_time))