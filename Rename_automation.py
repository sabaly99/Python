import os


os.chdir("/home/sabaly/Pictures")

print(os.getcwd())

for f in os.listdir():
    f_name,f_ext = os.path.splitext(f)
    n1,n2,n3,n4,n5,n6,n7,n8= f_name.split('_')
    

    new_name = '{}-{}-{}{}'.format(n1,n7,n8,f_ext)

    os.rename(f,new_name)