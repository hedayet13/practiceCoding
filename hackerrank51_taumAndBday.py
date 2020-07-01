t = int(input().strip())

for iter in range(t):
    first_input = input().rstrip().split()
    b= int(first_input[0])
    w= int(first_input[1])
    second_input = input().rstrip().split()
    bc= int(second_input[0])
    wc= int(second_input[1])
    z= int(second_input[2])

    if bc==0 or wc==0:
        print(0)
    elif z==0:
        print(b*bc+w*wc)
    elif bc==wc==z:
        print(b*bc+w*wc)
    elif z>wc and z>bc:
        print(b*bc+w*wc)
    elif bc>>wc+z:
        print((b+w)*z+b*wc)
    elif z<wc or z<bc:
        if bc>wc:
            print(b*(wc+z)+w*wc)
        elif wc>bc:
            print((b*bc)+w*(bc+z))

#  all can solve by the single line of code below


def taumBday(b, w, bc, wc, z):
    return b*min(bc, wc+z) + w*min(wc,bc+z)