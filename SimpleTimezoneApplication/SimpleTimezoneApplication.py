import tkinter as tk
import datetime
import pytz



timezones = ["Asia/Ho_Chi_Minh", "US/Alaska", "US/Aleutian", "US/Arizona",
             "US/Central", "US/East-Indiana", "US/Eastern",
             "US/Hawaii", "US/Indiana-Starke", "US/Michigan",
             "US/Mountain", "US/Pacific", "US/Samoa"]

def get_timezone_time(e, args):
    select_timezone_listbox = args[0]
    time_label = args[1]
    selection_index = select_timezone_listbox.curselection()
    select_timezone = select_timezone_listbox.get(selection_index)

    now_time = datetime.datetime.now()
    tz_time = now_time.astimezone(pytz.timezone(select_timezone))

    tz_formetted = tz_time.strftime("%H:%M:%S") #%H:hour %M:min %S: second
    time_label.configure({"text": f"The time in {select_timezone} is {tz_formetted}."})
    time_label.update()

root = tk.Tk()
root.title("Simple Timezone Application") #dat tieu de cho cua so chinh

window_width = 450
window_height = 175
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#cua so se hien thi o vi tri center cua PC width
center_x = int((screen_width - window_width)/2)
#cua so se hien thi o vi tri center cua PC height
center_y = int((screen_height - window_height)/2)
#gan kich thuoc man hinh voi srcW srcH center_x center_y
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.resizable(False, False) #ko cho thay doi kich thuoc

#chi dinh bo cuc luoi
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

#TAO WIDGET CON
select_timezone_label = tk.Label(root, text="Please select a timezone.")
select_timezone_label.grid(column=0, row=0, columnspan=4,
                           sticky=tk.W, padx=10, pady=10)
# Instance of Listbox class for selection of timezone from list.
list_var = tk.Variable(value=timezones)

select_timezone_listbox = tk.Listbox(root,listvariable="" , height=1)
select_timezone_listbox = tk.Listbox(root, listvariable=list_var, height=1)
select_timezone_listbox.grid(column=0, row=1, columnspan=3,
                             sticky=tk.EW, padx=10, pady=10)
#the Label class to display the local time in the selected timezone.
time_label = tk.Label(root, text="")
time_label.grid(column=0,row=4, columnspan=4, sticky=tk.W,
                padx=1, pady=10)

select_timezone_button = tk.Button(root, text="Get Time")
select_timezone_button.grid(column=4, row=1, sticky=tk.E,
                            padx=10, pady=10)



select_timezone_button.bind("<Button>",
    lambda e, args=[select_timezone_listbox, time_label]: get_timezone_time(e, args))


root.mainloop()