sides = list(map(int,input().split()))
if sum(sides) != 180:
  print("Invalid")
elif any(x==90 for x in sides):
  print("Right")
elif any(x>90 for x in sides):
  print("Obtuse")
else:
  print("Acute")