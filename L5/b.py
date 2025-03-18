bs=b"some text here"
st="some text here"
bs2=bytes([32,115,111,35,127,32,48])
# print(bs+bs2)
with open('text.bin','wb+')as f2:
    f2.write(bs)
    f2.write(bs2)
    f2.seek(0)
    print(f2.read())

with open('text.bin','r')as f3:
    print(f3.read())
# \x7f 
# 0123456789 
# 0123456789abcdef  - цифри

# 525 = 5*10^2+2*10^1+5*10^0=5*100+2*10+5*1
# 7f = 7*16^1+f*16^0=7*16+15*1=112+15=127

# 1111 1111
# 7654 3210   2^x
# 0000 1010   =10
# 0111 1111   = 1+2+4+8+16+32+64=127