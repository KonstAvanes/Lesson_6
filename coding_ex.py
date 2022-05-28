sb = b'Ad'

print(sb[0])
print(sb[1])

# 1 variant ascii
s = 'Hello world'

sb = s.encode('ascii')

print(sb)
print(type(sb))

# 2 variant utf-8
s = 'Hello world мир'

sb = s.encode('utf-8')

print(sb)
print(type(sb))

# Decoding
s = sb.decode('utf-8')

print(s)
print(type(s))
