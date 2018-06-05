#! \sr\bin\env python
feu = 'vert'
print 'Start: ' + feu

def change(x):
  if x is 'rouge' : return 'vert'
  if x is 'vert' : return 'orange'
  return 'rouge' 

feu = change(feu) ; 
print feu ;
feu = change(feu) ; 
print feu ;
feu = change(feu) ; 
print feu ;
feu = change(feu) ; 
print feu ;

