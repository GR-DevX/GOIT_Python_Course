a=1
while True:
    inp=input('Enter a comand: ')
    inp=inp.split()
    cmd=inp[0]
    inp=inp[1:]
    match cmd:
        case 'md':
            print(f'Creating dirs: {inp}')
        case 'cd':
            print(f'Changing dir to: {inp[0]}')
        case 'rm':
            print(f"Removing {inp}")
        case 'exit':
            break
        case _:
            print('unknown command')