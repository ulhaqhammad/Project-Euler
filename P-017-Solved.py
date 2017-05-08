# PROBLEM 017

"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""


def convert(num):
	'''Takes in a number between  1- 1000 and converts it into a words'''
	dic_1 = {1:'one', 2:'two', 3:'three', 4: 'four', 5:'five', 6: 'six', 7:'seven', 8: 'eight', 9:'nine'}
	dic_2 = {0:'ten', 1:'eleven' , 2:'twelve', 3 :'thirteen', 4: 'fourteen', 5:'fifteen', 6: 'sixteen', 7:'seventeen', 8: 'eighteen', 9:'nineteen'}
	dic_3 = {1: 'ten', 2:'twenty', 3:'thirty', 4: 'forty', 5:'fifty', 6: 'sixty', 7:'seventy', 8: 'eighty', 9:'ninety'}

	
	if len(str(num)) == 1:
		return dic_1[int(str(num))]

	# Check if number is in between 21-99
	elif len(str(num)) == 2 and str(num)[0] != '1' and str(num)[1] != '0':
		return dic_3[int(str(num)[0])] + ' '+ dic_1[int(str(num)[1])]
	
	# Check if number ends within 10-99 ends in 0 (e.g 10 , 20 , 30)
	elif len(str(num)) == 2 and str(num)[0] != '1' and str(num)[1] == '0':
		return dic_3[int(str(num)[0])]
	
	# Check if number belongs between 11-19 (e.g 11 , 12 , 13)
	elif len(str(num)) == 2 and str(num)[0] == '1':
		return dic_2[int(str(num)[1])]

	# Check if number belongs in 100s (e.g 100 , 200 , 300)
	elif len(str(num)) == 3 and str(num)[1] == '0' and str(num)[2] == '0':
		return dic_1[int(str(num)[0])] + ' hundred'

	elif len(str(num)) == 3 and str(num)[1] != '1' and str(num)[2] != '0' and str(num)[1] != '0' :
		return dic_1[int(str(num)[0])] + ' hundred and ' + dic_3[int(str(num)[1])] + '-' + dic_1[int(str(num)[2])]

	# Check if number is in the teen's category (e.g 111, 112 , 113)
	elif len(str(num)) == 3 and str(num)[1] == '1' and str(num)[2] != '0':
		return dic_1[int(str(num)[0])] + ' hundred and ' + dic_2[int(str(num)[2])]

	# Check if number is in the category (101 , 102 , 103, 201)
	elif len(str(num)) == 3 and str(num)[1] == '0' and str(num)[2] != '0':
		return dic_1[int(str(num)[0])] + ' hundred and ' + dic_1[int(str(num)[2])]

	elif len(str(num)) == 3 and str(num)[2] == '0':
		return dic_1[int(str(num)[0])] + ' hundred and ' + dic_3[int(str(num)[1])]

	elif len(str(num)) == 4:
		return 'one thousand'

sum_letters = 0
num_in_words =''
for i in range(1,1001):
	num_in_words = convert(i).replace('-','').replace(' ', '')
	sum_letters += len(num_in_words)
print('Total count :', sum_letters) 