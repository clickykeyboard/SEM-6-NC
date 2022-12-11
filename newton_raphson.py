import sympy

x = sympy.Symbol('x')

def f():
  return "x * e**x - 5" # Initial value is 1

def get_roots(iteration, initial_value) -> float:
  global x

  f_x: sympy.Expr = sympy.sympify(f())
  f_prime_x: sympy.Expr = sympy.diff(f(), x)

  # Putting initial value
  f_x_substitute = f_x.subs(x, initial_value)
  f_prime_x_substitute = f_prime_x.subs(x, initial_value)

  # Check if 'e' is in the expression
  if 'e' in f():
    f_x_substitute = f_x_substitute.subs(sympy.Symbol('e'), 2.71828)
    f_prime_x_substitute = f_prime_x_substitute.subs(sympy.Symbol('e'), 2.71828)

  # Newton Raphson Formula
  next_value = initial_value - (f_x_substitute / f_prime_x_substitute)

  if abs(next_value - initial_value) < 0.0005:
    return next_value
  
  return get_roots(iteration + 1, next_value)
  
print(get_roots(0, 1))
import sympy
