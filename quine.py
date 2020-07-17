def q():
  s = "'def q():\\n  s = ' + repr(s) + '\\n  return str(' + s + ')'"
  return str('def q():\n  s = ' + repr(s) + '\n  return str(' + s + ')')
