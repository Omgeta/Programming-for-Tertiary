for i in range(10):
  a = False
  for k in range(2):
    result = ""
    for j in range(1, i+1):
      if a:
        result += "yes"
      else:
        result += "no"
      if i % 2 != 0:
        a = not a
    if k % 2 == 0:
      a = True
    print(result)
