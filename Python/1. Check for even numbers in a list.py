nums = list(map(int,input().split()))
is_even = False
for i in nums:
  if i%2==0:
    is_even = True
    break
if is_even:
  print("Yes")
else:
  print("No")