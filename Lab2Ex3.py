import os

for root, dirs, files in os.walk(os.getcwd()):
    for f in files:
        if f.endswith('.py'):
            print(os.path.join(root, f))
