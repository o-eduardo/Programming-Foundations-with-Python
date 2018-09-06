import time
import webbrowser

    
def breake_time (my_time):
    print "This programa started on "+time.ctime()
    while(my_time >0):
        time.sleep(10)
        webbrowser.open ("https://www.youtube.com/watch?v=U9M65xpI8uk")
        my_time = my_time - 1
    else:
        print "that's all  folks"

