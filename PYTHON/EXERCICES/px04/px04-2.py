feu = 'vert'
def vert(x) : return feu is 'vert'
print vert(feu)				# True

feu = 'rouge'
def rouge(x) : return feu is 'vert'
print rouge(feu)				# False

feu = 'orange'
def orange(x) : return feu is 'vert'
print orange(feu)				# False
