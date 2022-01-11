croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
var = raw_input()

for i in croatia:
    var = var.replace(i, '*')

print(len(var))
