var = [10,20,30,40,50]
varOne = var.copy()# var[:] #shallow copy 
print(f'var: {var}  with address: {id(var)}')
print(f'varOne: {varOne}  with address: {id(varOne)}')
var.append(100)
print(f'var: {var}  with address: {id(var)}')
print(f'varOne: {varOne}  with address: {id(varOne)}')
