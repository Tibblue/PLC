import regex as re

metric = {
  "yard":{
    "convertion": 0.91,
    "new_unit": "m"
  },
  "inch":{
    "convertion": 2.54,
    "new_unit": "cm"
  },
  "foot":{
    "convertion": 30.5,
    "new_unit": "cm"
  },
  "mile":{
    "convertion": 1.61,
    "new_unit": "km"
  }
}

texto = "after running 1 mile, they runned 2 yard."


def add_fote(texto):
  # units_str = 's|'.join(metric.keys())+'s'
  units_str = '|'.join(metric.keys())

  matches = re.findall(r'(\d+) ('+units_str+')',texto)
  # print(matches)
  for value,unit in matches:
    new_value = metric[unit]['convertion']
    new_unit = metric[unit]['new_unit']
    print(value,unit,new_value,new_unit)
    texto = re.sub(value+' '+unit,
                  value+' '+unit+r'\\\\footnote{'+str(new_value*float(value))+' '+new_unit+'}',texto)
  return texto


print(add_fote(texto))