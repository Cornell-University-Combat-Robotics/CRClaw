from switch import Limit

# l = Limit(16)
# try:
#     while(True):
#         print(l.isPressed())
# except: 
#     l.cleanup()
l = Limit(16)
#l.button_callback()
l.add_event()
try:
    while(True):
        l.is_touched()
except:
    l.cleanup()

