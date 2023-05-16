try:
 print("start code")
 print(Error)
 print("end")
except:
 print('NO BROBLEMS')
print("any cod...")
'''
def checker(var_1):
 if type(var_1) != str:
  raise TypeError (f"Sorry , ми не можемо працювати з класом {type(var_1)} будь ласка ведь в str")
 else :
  return var_1
a = 1234
checker(a)
'''
class BuildingError(Exception):
 def __str__(self):
  return "щось багато і дорого"
def check_material(amount , limit):
  if amount > limit:
    return "Достатньо матеріалів!!"
  else:
    raise BuildingError()
print(check_material(1, 300))