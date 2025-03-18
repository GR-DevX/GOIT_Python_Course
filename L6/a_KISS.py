def raise_salary(old_salary,raise_value):
    br=old_salary+raise_value
    nt=br*.9 if br<=1000 else br*.8
    return {'brutto':br,
            'netto':nt}

def is_even(n:int)->bool:
    return n%2==1
   
if __name__=='a':
    print("yoou are using cool module 'A'")

if __name__=='__main__':
    print(raise_salary(1000,0))
    print(raise_salary(1000,100))