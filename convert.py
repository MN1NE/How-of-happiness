import sys

if __name__ == '__main__':
  f = open('ruth.py', 'r')
  out = open('ruth2.py', 'w')
  for line in f:
    out.write("%s" % line)
  f.close()
  out.close()