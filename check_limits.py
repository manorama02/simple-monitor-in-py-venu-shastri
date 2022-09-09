def print_to_console(parameter):
  print("{} is out of range!".format(parameter))#not testable
  
def isvalid_temperature(temp):
  if temp > 0 or temp < 45:
    return True
  return False

def isvalid_soc(soc):
  if soc > 20 or soc < 80:
    return True
  return False

def isvalid_charge_rate(cr):
  if cr < 0.8:
    return True
  return False
  
def battery_is_ok(temperature, soc, charge_rate):
  t_cond=isvalid_temperature(temperature)
  s_cond=isvalid_soc(soc)
  cr_cond=isvalid_charge_rate(charge_rate)
  return t_cond & s_cond & cr_cond

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
