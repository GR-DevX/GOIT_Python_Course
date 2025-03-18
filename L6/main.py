import creds
def f(**kwargs):
    pass
def main():
    pass


if __name__=='__main__':
    main()
    #GOOD:
    f(user=creds.user,passwd=creds.passwd,addr=creds.server)
    #BAD:
    f(user='username',passwd='verysecretpassphrase',server='google.com :)')