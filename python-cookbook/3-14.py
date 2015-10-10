import decimal,re,operator
parse_input=re.compile(r'''(?x)
  (\d+\.?\d*)
  \s*
  ([-+/*])
  $''')
oper={'+':operator.add,'-':operator.sub,
  '*':operator.mul,'/':operator.truediv,}
total=decimal.Decimal('0')
def print_total():
  print '== == =\n',total

print """welcom to adding machine:
enter a number and operator,
an empty line to see the current subtotal,
or q to quit: """
while True:
  try:
    tape_line=raw_input().strip()
  except EOFError:
    tape_line='q'
  if not tape_line:
    print_total()
    continue
  elif tape_line=='q':
    print_total()
    break
  try:
    num_text,op=parse_input.match(tape_line).groups()
  except AttributeError:
    print 'invalid entry: %r'%tape_line
    print 'enter number and operator...'
    continue
  total=oper[op](total,decimal.Decimal(num_text))
