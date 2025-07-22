temp, unit = input().split() 
temp = float(temp)
if unit=='C':
  print((9/5)*temp + 32," F")
elif unit=='F':
  print((5/9)*(temp -32)," C")