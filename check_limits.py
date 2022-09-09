def print_to_console(parameter):
  print("{} is out of range!".format(parameter))#not testable
  
def isvalid_temperature(temp,consoleprint):
  if temp > 0 and temp < 45:
    return True
  consoleprint('temperature')
  return False

def isvalid_soc(soc,consoleprint):
  if soc > 20 and soc < 80:
    return True
  consoleprint('soc')
  return False

def isvalid_charge_rate(cr,consoleprint):
  if cr < 0.8:
    return True
  consoleprint('charge rate')
  return False
  
def battery_is_ok(temperature, soc, charge_rate,consoleprint):
  t_cond=isvalid_temperature(temperature,consoleprint)
  s_cond=isvalid_soc(soc,consoleprint)
  cr_cond=isvalid_charge_rate(charge_rate,consoleprint)
  return t_cond & s_cond & cr_cond

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7,print_to_console) is True)
  assert(battery_is_ok(50, 85, 0,print_to_console) is False)
