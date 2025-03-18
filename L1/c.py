value='rm'
value2="c:\\delme"
match value, value2:
  case value, "c:\\windows":
    print('c:\\windows is untouchable')
  case 'del'|'rm', value2:
    print(f"remove {value2}")
  case _:
    print('another value')