def f(x):
  return (x**3) - 2 * x - 5 # Root [1.4, 1.5]
  # return (x**6) - (x**4) - (x**3) - 1 # Root [1.4, 1.5]
  # return 2*x**3 + x - 2 # Root [0, 1]

i = 0
def get_roots(last_answer, interval: list[int]) -> float:
  global i
  print("Iteration:", i)
  i += 1
  
  lower_limit = interval[0]
  upper_limit = interval[1]
  
  f_lower_limit = f(lower_limit)
  f_upper_limit = f(upper_limit)
  
  x = lower_limit - ((upper_limit - lower_limit) / (f_upper_limit - f_lower_limit)) * f_lower_limit
  x = round(x, 4)

  if not last_answer == 0 and abs(x - last_answer) < 0.0005:
    return x
  
  print(x)

  if x > 0:
    return get_roots(x, [x, upper_limit])
  if x < 0:
    return get_roots(x, [lower_limit, x])
  

print(get_roots(0, [0, 1]))
