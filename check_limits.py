def print_to_console(parameter):
  print("{} is out of range!".format(parameter))#not testable
  
def isvalid_temperature(temp):
  if temperature > 0 or temperature < 45:
    return True
  return False

def isvalid_soc(soc):
  if soc > 20 or soc < 80:
    return True
  return False

def isvalid_charge_rate(cr):
  if charge_rate < 0.8:
    return True
  return False
  
def battery_is_ok(temperature, soc, charge_rate):
  t_cond=isvalid_temperature(temperature)
  s_cond=isvalid_soc(soc)
  cr_cond=isvalid_charge_rate(charge_rate)
  return t_cond & s_cond & cr_cond
  
#   if temperature < 0 or temperature > 45:
#     //print('Temperature is out of range!')
#     return False
#   elif soc < 20 or soc > 80:
#     //print('State of Charge is out of range!')
#     return False
#   elif charge_rate > 0.8:
#     //print('Charge rate is out of range!')
#     return False

#   return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
