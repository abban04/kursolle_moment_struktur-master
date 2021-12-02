salary = int(input("What's your salary?"))
mun_tax = salary * 0.2136
county_tax = salary * 0.1148
year_salary = salary*12
state_tax = salary * 0.2
prot_tax = salary * 0.05


print("Output")
print("Monthly salary:    ",(salary),("kr"), 'Yearly salary:' ,(year_salary),("kr"))
print("Municipal tax:     ",(mun_tax),("kr"))
print("County council tax:",(county_tax),("kr"))

if year_salary > 468700 and year_salary < 675700:
    print("State tax: ", (state_tax),("kr"))
    print("Salary after taxes:",(salary) - (mun_tax) - (county_tax) - (state_tax),("kr"))
    print("Total tax: ",(mun_tax) + (county_tax) + (state_tax),("kr"))
    print("Total tax payed: ",((mun_tax + county_tax + state_tax)/salary)*100,("%"))
    
elif year_salary >= 675700:
    print("State tax: ", (state_tax),("kr"))
    print("Protection tax: ", (prot_tax),("kr"))
    print("Salary after taxes:",(salary) - (mun_tax) - (county_tax) - (state_tax) - (prot_tax),("kr"))
    print("Total tax: ",(mun_tax) + (county_tax) + (state_tax) + (prot_tax),("kr"))
    print("Total tax payed: ",((mun_tax + county_tax + state_tax + prot_tax)/salary)*100,("%"))
else:
    print("Salary after taxes:",(salary) - (mun_tax) - (county_tax),("kr"))
    print("Total tax ", (mun_tax) + (county_tax),("kr"))
    print("Total tax payed: ",((mun_tax + county_tax)/salary)*100,("%"))

if year_salary <= 19247:
    print("Since your salary is under the breaking point, you don't have to pay taxes.");

