s="Привіт, світе!"

utf_text=s.encode()
print(f"UTF-8: {utf_text}")

utf16_text=s.encode("utf-16")
print(f"UTF-16: {utf16_text}")

utf32_text=s.encode("utf-32")
print(f"UTF-32: {utf32_text}")

cp1251_text=s.encode("cp1251")
print(f"cp1251: {cp1251_text}")

restored=utf32_text.decode("utf-32")
print (restored)

# with (open("text2.bin","wb")) as f:
#     f.writelines([utf_text,utf16_text,utf32_text,cp1251_text])

# with (open("text2.bin","r")) as f:
#     print(f.read())

