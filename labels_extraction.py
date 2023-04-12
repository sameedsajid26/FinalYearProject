import re

file_name = '/Users/sameedsajid/opt/anaconda3/pkgs/lammps-2022.06.23-py310h33d413e_mpich_0/bin/25JAN/testing/log.lammps'
filename = '/Users/sameedsajid/opt/anaconda3/pkgs/lammps-2022.06.23-py310h33d413e_mpich_0/bin/25JAN/testing/labels.txt'
# entering try block
try:

	# opening and reading the file
	file_read = open(file_name, "r")

	# asking the user to enter the string to be
	# searched
	text = 'Stacking-fault energy = '

	# reading file content line by line.
	lines = file_read.readlines()

	new_list = []
	idx = 0

	# looping through each line in the file
	for line in lines:
		
		if text in line:
			new_list.insert(idx, line)
			idx += 1

	file_read.close()

	# if length of new list is 0 that means
	# the input string doesn't
	# found in the text file
	if len(new_list)==0:
		print("\n\"" +text+ "\" is not found in \"" +file_name+ "\"!")
	else:

		# displaying the lines
		# containing given string
		lineLen = len(new_list)
		print("\n**** Lines containing \"" +text+ "\" ****\n")
		for i in range(lineLen):
				print(end=new_list[i])
		print()

# entering except block
# if input file doesn't exist
except :
    print("\nThe file doesn't exist!")


#f = open("myfile.txt", "w")
# f = open("myfile.txt", "x")
with open(filename, 'w') as f:
	for i, line in enumerate(new_list):
		if (i % 2 == 1):
		# for i in line:
		# 	if i.isdigit() == True:	
			f.write(line)

f.close()

sub1 = 'Stacking-fault energy = '
sub2 = ' mJ/m^2'
sfe_list = []
s=str(re.escape(sub1))
e=str(re.escape(sub2))
with open(filename, 'r') as f:
	lines = f.readlines()
	for line in lines:
		res=re.findall(s+"(.*)"+e,line)[0]
		sfe_list.append(res)
		# print("The extracted string : " + res)
f.close()

print(sfe_list)

import numpy as np
sfe_arr = np.array(sfe_list)
sfe_arr = sfe_arr.astype(float)
print (len(sfe_arr))
print ("Mean: ", np.mean(sfe_arr))
print ("Std: ",np.std(sfe_arr))


with open(filename, 'w') as f:
	for line in sfe_list:
			f.write(line)
			f.write('\n')

f.close()


 
