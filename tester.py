def measure_string(myStr):
    count = 0
    if myStr == myStr[-1]:
        return count + 1

    else:
        return 1 + measure_string(myStr[1:])

    # count = 0
    # if myStr == myStr[-1]:
    # 	return count
    # else:
    #     return measure_string(myStr[1:])


#The line below will test your function. As written, this
#should print 13. You may modify this to test your code.
print(measure_string("13 characters"))
print("--------------")
print(measure_string("1"))




