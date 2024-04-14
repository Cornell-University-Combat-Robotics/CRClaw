from switch import Limit

l = Limit(16)
try:
    while(True):
        print(l.isPressed())
except: 
    l.cleanup()