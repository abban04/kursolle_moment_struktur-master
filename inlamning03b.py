salary = int(input("What's your salary?"))
mun_tax = salary * 0.2136
county_tax = salary * 0.1148
year_salary = salary*12
print("Output")
print(f"Monthly salary:    ",(salary), 'Yearly salary:' ,(year_salary))
print("Municipal tax:     ",(mun_tax))
print("County council tax:",(county_tax))
print("Salary after taxes:",(salary) - (mun_tax) - (county_tax))

if year_salary <= 19247:
    print("Since your salary is under the breaking point, you don't have to pay taxes.");