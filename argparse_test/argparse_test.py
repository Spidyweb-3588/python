import argparse

parser = argparse.ArgumentParser(description='Arugment 설명')

parser.add_argument('--first', type=int)
parser.add_argument('--second', type=int)
parser.add_argument('--third', type=str)

args = parser.parse_args()

print(args)
print(type(args))

first="na"
second="na"
third="na"

print(first, second, third)

if args.first != None: first=args.first
if args.second != None: second=args.second
if args.third != None and len(args.third) >= 1: third=args.third

#print("first=%d, second=%d, third=%s" % (first, second, third))
#print("first={0}, second={1}, third={2}".format(first, second, third))
print(f"first={first}, second={second}, third={third}")

args_list=[]
args_list.append(args.first)
args_list.append(args.second)
args_list.append(args.third)

for i in range(len(args_list)):
    print(args_list[i])

args_dict=vars(args)
print(args_dict)
for i in args_dict.values():
    print(i)
