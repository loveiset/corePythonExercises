a=raw_input('enter first set(","between numbers): ').split(',')
b=raw_input('enter second set(","between numbers): ').split(',')

setA=set([int(x) for x in a])
setB=set([int(x) for x in b])

op=raw_input('''enter your op: 
in
not in
&
|
^
<
<=
>
>=
==
!=
you choice: ''').strip()

if op in ['in','not in','&','|','^','<','<=','>','>=','==','!=']:
  print eval('setA %s setB' % op)
