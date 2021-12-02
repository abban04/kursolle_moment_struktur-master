from time import localtime

t = localtime()
timme = t.tm_hour
print(t, timme)

if timme >= 16:
    print("Skoldagen är slut")
else:
    print("Skoldagen är inte slut")