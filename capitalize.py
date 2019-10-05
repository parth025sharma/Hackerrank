#!/usr/bin/python3


fname, lname = input().split('')
if fname[0].isnumeric() == True and lname[0].isalpha() == True:
	print(fname +" "+ lname.capitalize())

elif fname[0].isnumeric() == True and lname[0].isnumeric() == True:
	print(fname +" "+ lname)

elif fname[0].isalpha() == True and lname[0].isnumeric() == True:
	print(fname.capitalize() +" "+ lname)

elif fname[0].isalpha() == True and lname[0].isalpha() == True:
	print(fname.capitalize() +" "+ lname.capitalize())
