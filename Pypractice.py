#!/usr/bin/pyhton3
print("Hello, World!")
a,b = 0,1
if a < b:
  print('a ({}) is less than b({})'.format(a,b))
else:
  print('a({}) is not less than b({})'.format(a,b))
  
print("foo" if a<b else "bar");


def fibonacci():
  a,b = 0,1
  while b<50:
    print(b);
    a,b=b,a+b
  print("done");	

fh = open("Pypractice.py")
for line in fh.readlines():
  print(line,end='');
  
fibonacci()
try:
  f = open("xfile.yxy") 
except IOError as e:
  print("Error: ({})".format(e))
  

def main():
  
if __name__ = "__main__" :main()