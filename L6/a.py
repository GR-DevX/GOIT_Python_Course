def raise_salary(old_salary,raise_value):
    return {'brutto':old_salary+raise_value,
            'netto':(old_salary+raise_value)*0.9 if old_salary+raise_value <=1000 else (old_salary+raise_value)*0.8}


if __name__=='a':
    print("yoou are using cool module 'A'")

if __name__=='__main__':
    print(raise_salary(1000,0))
    print(raise_salary(1000,100))