f=None
try:
    10/0
    f=open("c:\\absent.txt",'rb') # відкриття файлу, котрого немає
    # raise Error
    
except Exception as e:
    if isinstance(e,FileNotFoundError):
        print('no file')
    else:
        print(f"Error: {e}")
    
finally:
    if f is not None:
        f.close()

print('Done')