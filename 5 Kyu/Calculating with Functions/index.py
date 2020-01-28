import math

def zero(operator = None):
  if not operator:
    return 0
  else:
    return operator(0)
def one(operator = None):
  if not operator:
    return 1
  else:
    return operator(1) 
def two(operator = None):
  if not operator:
    return 2
  else:
    return operator(2)
def three(operator = None):
  if not operator:
    return 3
  else:
    return operator(3)
def four(operator = None):
  if not operator:
    return 4
  else:
    return operator(4)
def five(operator = None):
  if not operator:
    return 5
  else:
    return operator(5)
def six(operator = None):
  if not operator:
    return 6
  else:
    return operator(6)
def seven(operator = None):
  if not operator:
    return 7
  else:
    return operator(7)
def eight(operator = None):
  if not operator:
    return 8
  else:
    return operator(8)
def nine(operator = None):
  if not operator:
    return 9
  else:
    return operator(9)

def plus(b):
  def plus(a):
    return a + b
  return plus

def minus(b):
  def minus(a):
    return a - b
  return minus

def times(b):
  def times(a):
    result = a * b
    return result
  return times

def divided_by(b):
  def divided_by(a):
    return math.floor(a / b)
  return divided_by