NAME = input("")
SALARY  = float(input(""))
SELLS = float(input(""))

TOTAL = SALARY + (SELLS * 0.15)

print("TOTAL = R$ {:.2f}".format(TOTAL))