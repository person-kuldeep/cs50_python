
# sys module 

import sys
print("Script name: ", sys.argv[0])
print("Python executable path: ", sys.executable)
print("Python version: ", sys.version)
print("Platform: ", sys.platform)
if len(sys.argv) < 2:
    sys.exit("too few args")
print("hello, ", sys.argv[1])