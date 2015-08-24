def safe_raw_input(istr):
  try:
    retval=raw_input(istr)
  except EOFError,KeyboardInterrupt:
    retval=None
  return retval
