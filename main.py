from module import *
import schedule
from tkinter import *
from tkinter import ttk
import configparser
import threading
import sys

running = True
counter = 0
# GET CONFIG FROM config.txt
config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))
conf_resetwalk = config.get('Set Time', 'resetwalk')
conf_awake_while_playing = config.get('Set Time', 'awake_while_playing')
# # ------------------------------------------------------------
# Assign Schedule Job Here
schedule.every(int(conf_resetwalk)).minutes.do(resetwalk)
schedule.every(int(conf_awake_while_playing)).minutes.do(awake_while_playing)
schedule.every(10).seconds.do(errorHandle)
schedule.every(11).seconds.do(chk_btn_close)
schedule.every(8).seconds.do(chk_treasure_h)
# # ------------------------------------------------------------

def start():
    global running 
    running = True
    t1 = threading.Thread(target=mainfunc)
    t1.start()
    txt_status.configure(text = 'Processing', foreground="green")
    # threading.Thread(target=chk_status).start()

def stop():
    # testcount()
    global running 
    running = False
    txt_status.configure(text = 'Stopped', foreground="red")

def mainfunc():
    while True:
        if running:
            schedule.run_pending()
            login()
            # time.sleep(2)
        else:
            break
        time.sleep(2)
        # root.after(2000,mainfunc)

# def processing():
#     threading.Thread(target=mainfunc).start()
#     # if running:
#     #     # threading.Thread(target=chk_status).start()
#     #     # chk_btn_close()
#     #     # chk_treasure_h()
#     #     # login()
#     #     gc.collect()
#     #     root.after(2000, processing)


def chk_status():
    global running 
    while True:
        if running:
            global counter
            my_list = [".", "..", "...", ""]
            if counter != 3:
                txt_status.config(text="Processing{}".format(my_list[counter]), foreground="green")
                counter += 1
                # root.after(1000, chk_status)
            else:
                txt_status.config(text="Processing{}".format(my_list[counter]), foreground="green")
                counter = 0
                # root.after(1000, chk_status)
        else:
            txt_status.configure(text = 'Stopped', foreground="red")
            break
def exitprogram():
    root.destroy
    sys.exit()

root = Tk(className='Bot')
frm = ttk.Frame(root, padding=10)
frm.grid()
root.geometry("250x100")
btn_start = ttk.Button(frm, text="Start", command=start).grid(column=1, row=0)
ttk.Button(frm, text="Stop", command=stop).grid(column=2, row=0)
ttk.Button(frm, text="Quit", command=exitprogram).grid(column=1, row=1)
ttk.Label(frm, text="Status : ").grid(column=1, row=2)
txt_status = ttk.Label(frm, text="Stopped", foreground="red")
txt_status.grid(column=2, row=2)
root.mainloop()