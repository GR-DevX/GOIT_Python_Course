import sys
def connect(serv):
    pass

args=tuple(sys.argv)
user=None
passwd=None
server='localhost'
for i in range(len(args)):
    if args[i]=='--user':
        user=args[i+1]
    if args[i]=='--password':
        passwd=args[i+1]
    if args[i]=='--server':
        server=args[i+1]
connect(server)
print(f'User {user} with password {passwd} logged to {server}')