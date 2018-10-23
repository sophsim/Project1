import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import csv

def getData(file):
	with open(file, "r") as infile:
		lines = infile.readlines()[1:]
		infile.close()
		list_of_dict = []
		for line in lines:
			dictdata= {}
			values = line.split(",")
			first = values[0]
			last = values[1]
			email = values[2]
			class_data = values[3]
			dob = values[4]
			dictdata["First"] = first
			dictdata["Last"] = last
			dictdata["Email"] = email
			dictdata["Class"] = class_data
			dictdata["DOB"] = dob.strip('\n')
			list_of_dict.append(dictdata)

	infile.close()
	return list_of_dict


def mySort(data,col):
	
	sort_data = sorted(data, key = lambda l: l[col])
	
	name_data = sort_data[0]['First'] + " " + sort_data[0]['Last']
	
	return name_data



def classSizes(data):
	
	d = {}
	
	for s in  data:
		if s['Class'] not in d:
			d[s['Class']] = 0
		d[s['Class']] = d[s['Class']] + 1
	
	return sorted(d.items(), key = lambda l: l[1], reverse = True)


def findMonth(a):
	b_dict = {}
	for d in a:
	    b_month = d["DOB"].split('/')[0]
	    if b_month in b_dict:
	        b_dict[b_month] += 1
	    else:
	        b_dict[b_month] = 1
	return int(sorted(b_dict, key = lambda l: b_dict[l], reverse = True)[0])


def mySortPrint(a,col,fileName):
	outfile = open(fileName, "w")
	sort_data = sorted(a, key=lambda l: l[col])
	
	for stud in sort_data:
		output = stud['First'] + "," + stud['Last'] + "," + stud["Email"]
		outfile.write(output + '\n')
	
	pass


def findAge(a):

	list_of_ages = []
	t = date.today()
	
	for person in a:
		dob = person['DOB'].split('/')
		born = date(int(dob[2]), int(dob[0]), int(dob[1]))
		list_of_ages += [t.year-born.year-((t.month,t.day)<(born.month,born.day))]
	
	return round(sum(list_of_ages)/len(list_of_ages))


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
