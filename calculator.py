print "Do math!"
x = raw_input("enter your first value: ")
y = raw_input("enter your second value:")
z = raw_input("enter the function you are doing:")

if z =="+":
	print x, "plus" 
	print y, "equals"
	print int(x) +int(y)
else:
	if z =="-":
		print x, "minus" 
		print y, "equals"
		print int(x) -int(y)
	else:
		if z =="*":
			print x, "times" 
			print y, "equals"
			print int(x) *int(y)
		else:
			if z =="/":
				print x, "divided by" 
				print y, "equals"
				print int(x) /int(y)
			else:
				print "error, you picked an incorrect function!"

