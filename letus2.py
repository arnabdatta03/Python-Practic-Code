biya = input("Enter your meterial status :")
sex = input("Enter your sex :")
age = float(input("Enter your age :"))
if (biya=='married')or(biya=='unmarried'and sex=='male'and age>=30) or(biya=='u'and sex=='female'and age>=25):
    print("insure")
else:
    print("Not insure")