# -*- coding: utf-8 -*-
import Jarvis
import colorama
import sys
import os
import update_window
import threading
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def check_python_version():
    return sys.version_info[0] == 3




def main():
    
    # enable color on windows
    colorama.init()
    # start Jarvis
    
    jarvis = Jarvis.Jarvis()


    command = " ".join(sys.argv[1:]).strip()
    # command = update_window.update()
    
    # print(sys.argv[1:])

    
    jarvis.executor(command)

    
#t1 = threading.Thread(target=main)
# t2 = threading.Thread(target=update_window)



if __name__ == '__main__':
    if check_python_version():
        main()
        
    else:
        print("Sorry! Only Python 3 supported.")
