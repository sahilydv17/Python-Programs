basicsal = float(input("Enter basic salary: "))

hra = basicsal*30/100
da = basicsal*20/100
ta = basicsal*10/100
pf = 1400
print("Net salary is:", basicsal+hra+da+ta-pf)
