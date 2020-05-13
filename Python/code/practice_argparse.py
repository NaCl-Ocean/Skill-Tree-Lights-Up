import argparse
parser = argparse.ArgumentParser(prog='pratice_argparse',description='this is a script for parcitce',epilog='after args help')
parser.add_argument('-f','--foo', help='foo help',metavar='foo',type = int,default=10,dest='f_test')
parser.add_argument('pos_1',help='first pos arg',type = str)
parser.add_argument('pos_2',help='second pos arg')

 
args = parser.parse_args()
print('f:',args.f_test)
print('pos_1:',args.pos_1)
print('pos_1:',args.pos_2)
