import math

def f(x):
  return x * math.e**x - 5 # Root [1, 2]
  # return math.e**-x - math.sin((math.pi * x) / 2) # Root [1, 2]

def get_root(i, interval: list[int]) -> float:
  lower_limit = interval[0]
  upper_limit = interval[1]
  middle_point = (lower_limit + upper_limit) / 2

  print("Interval: ", [lower_limit, upper_limit])
  print(f"Middle point for iteration {i}: {middle_point}")
  equation = f(middle_point)
  equation = round(equation, 4)

  print(f"Iteration {i}: ", equation)
  if equation == 0:
    return middle_point
  
  i = i + 1
  if equation > 0:
    get_root(i, [lower_limit, middle_point])
  if equation < 0:
    get_root(i, [middle_point, upper_limit])
  
  return middle_point

print(get_root(1, [1, 2]))