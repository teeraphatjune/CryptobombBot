from module import *
import schedule
from tkinter import *
from tkinter import ttk
import configparser
import gc
import threading

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

# while True:
#     print("Processing...")
#     login()
#     time.sleep(1)

def start():
    global running 
    running = True
    # chk_status()
    # processing()
    threading.Thread(target=mainfunc).start()
    txt_status.configure(text = 'Processing', foreground="green")
    # threading.Thread(target=chk_status).start()

def stop():
    global running 
    running = False
    txt_status.configure(text = 'Stopped', foreground="red")
    # chk_status()

def mainfunc():
    if running:
        schedule.run_pending()
        login()
        root.after(2000,mainfunc)

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
        root.after(1000, chk_status)
    else:
        txt_status.configure(text = 'Stopped', foreground="red")

# schedule.every(1).seconds.do(chk_status)
root = Tk(className='Bot')
frm = ttk.Frame(root, padding=10)
frm.grid()
root.geometry("230x100")
btn_start = ttk.Button(frm, text="Start", command=start).grid(column=1, row=0)
ttk.Button(frm, text="Stop", command=stop).grid(column=2, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
ttk.Label(frm, text="Status : ").grid(column=1, row=2)
txt_status = ttk.Label(frm, text="Stopped", foreground="red")
txt_status.grid(column=2, row=2)
root.mainloop()