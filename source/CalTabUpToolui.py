#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

#
# Begin image loader - Setup image_loader in derived class file
#
def default_image_loader(image_name):
    img = None
    try:
        img = tk.PhotoImage(file=image_name)
    except tk.TclError:
        pass
    return img
image_loader = default_image_loader
# End image loader

def handleLog(_log, s):
    _log += s
    if  _log.count('\n') >= 9:
        i = _log.find('\n')
        _log = _log[i + 1:]
    return _log



class ApplicationUI:
    def __init__(self, master=None, data_pool=None):
        # build ui
        self.mainwindow = ttk.Frame(master, name="mainwindow")
        self.mainwindow.configure(
            borderwidth=5,
            height=500,
            relief="ridge",
            width=1000)
        self.mainlabel = ttk.Label(self.mainwindow, name="mainlabel")
        self.mainlabel.configure(
            font="{Times New Roman} 20 {bold}",
            padding=5,
            text='Database calib-tables update tool')
        self.mainlabel.place(
            anchor="nw",
            relheight=0.1,
            relwidth=0.7,
            relx=0.0,
            rely=0.0,
            x=0,
            y=0)
        self.db_select_button = ttk.Button(
            self.mainwindow, name="db_select_button")
        self.db_select_button.configure(padding=5, text='Select Database')
        self.db_select_button.place(
            anchor="w",
            relheight=0.07,
            relwidth=0.15,
            relx=0.01,
            rely=0.15)
        self.db_select_button.configure(command=self.on_select_db_button_click)
        self.ct_load_button = ttk.Button(
            self.mainwindow, name="ct_load_button")
        self.ct_load_button.configure(padding=5, text='Load calibration table')
        self.ct_load_button.place(
            anchor="w",
            relheight=0.07,
            relwidth=0.15,
            relx=0.01,
            rely=0.25)
        self.ct_load_button.configure(command=self.on_load_ct_button_click)
        self.path_db = ttk.Entry(self.mainwindow, name="path_db")
        self.selected_db_path = tk.StringVar(value='Currently not implemeted!')
        self.path_db.configure(
            font="{Times New Roman} 12 {}",
            justify="left",
            state="readonly",
            textvariable=self.selected_db_path)
        _text_ = 'Currently not implemeted!'
        self.path_db["state"] = "normal"
        self.path_db.delete("0", "end")
        self.path_db.insert("0", _text_)
        self.path_db["state"] = "readonly"
        self.path_db.place(
            anchor="w",
            relheight=0.06,
            relwidth=0.5,
            relx=0.20,
            rely=0.15)
        self.path_ct = ttk.Entry(self.mainwindow, name="path_ct")
        self.selected_ct_path = tk.StringVar(value='calibration table file location')
        self.path_ct.configure(
            font="{Times New Roman} 12 {}",
            justify="left",
            state="readonly",
            textvariable=self.selected_ct_path)
        _text_ = 'calibration table file location'
        self.path_ct["state"] = "normal"
        self.path_ct.delete("0", "end")
        self.path_ct.insert("0", _text_)
        self.path_ct["state"] = "readonly"
        self.path_ct.place(
            anchor="w",
            relheight=0.06,
            relwidth=0.5,
            relx=0.20,
            rely=0.25)
        self.log_feedback1 = tk.Message(self.mainwindow, name="log_feedback1")
        self.txtbox_feedback_1 = tk.StringVar()
        self.log_feedback1.configure(
            anchor="sw",
            aspect=32000,
            background="#f0f0f0",
            font="{Courier New} 11 {}",
            justify="left",
            relief="sunken",
            textvariable=self.txtbox_feedback_1)
        self.log_feedback1.place(
            anchor="nw",
            relheight=0.5,
            relwidth=0.34,
            relx=0.01,
            rely=0.35)
        self.log_feedback2 = tk.Message(self.mainwindow, name="log_feedback2")
        self.txtbox_feedback_2 = tk.StringVar()
        self.log_feedback2.configure(
            anchor="nw",
            aspect=32000,
            background="#f0f0f0",
            font="{Courier New} 11 {}",
            justify="left",
            relief="sunken",
            textvariable=self.txtbox_feedback_2)
        self.log_feedback2.place(
            anchor="nw",
            relheight=0.5,
            relwidth=0.34,
            relx=0.36,
            rely=0.35)
        separator1 = ttk.Separator(self.mainwindow)
        separator1.configure(orient="horizontal")
        separator1.place(
            anchor="w",
            relheight=0.01,
            relwidth=0.71,
            relx=0.0,
            rely=0.32,
            x=0,
            y=0)
        separator2 = ttk.Separator(self.mainwindow)
        separator2.configure(orient="vertical")
        separator2.place(
            anchor="nw",
            relheight=1.0,
            relwidth=0.01,
            relx=0.71,
            rely=0.0,
            x=0,
            y=0)
        self.multi_button = ttk.Button(self.mainwindow, name="multi_button")
        self.multibutton_str = tk.StringVar(value='CONFIRM')
        self.multi_button.configure(
            state="disabled",
            text='CONFIRM',
            textvariable=self.multibutton_str)
        self.multi_button.place(
            anchor="nw",
            relheight=0.10,
            relwidth=0.15,
            relx=0.01,
            rely=0.88,
            x=0,
            y=0)
        self.multi_button.configure(command=self.on_multi_click)
        self.logo_monti = ttk.Label(self.mainwindow, name="logo_monti")
        self.img_logoMonti = image_loader("logoMonti.png")
        self.logo_monti.configure(image=self.img_logoMonti)
        self.logo_monti.place(
            anchor="ne",
            relx=0.97,
            rely=0.07,
            width=225,
            x=0,
            y=0)
        self.detail = ttk.Label(self.mainwindow, name="detail")
        self.detail.configure(
            anchor="n",
            foreground="#9f9f9f",
            text='STAR database calibration table update tool')
        self.detail.place(
            anchor="nw",
            relx=0.46,
            rely=0.01,
            width=240,
            x=0,
            y=0)
        self.dev_detail = ttk.Label(self.mainwindow, name="dev_detail")
        self.dev_detail.configure(
            anchor="e",
            foreground="#9f9f9f",
            text='Developed by Poxmin, MONTI systems s.r.o.')
        self.dev_detail.place(
            anchor="se",
            relx=0.70,
            rely=0.98,
            width=280,
            x=0,
            y=0)
        self.version_detail = ttk.Label(self.mainwindow, name="version_detail")
        self.version_str = tk.StringVar(value='Version 1.0b')
        self.version_detail.configure(
            anchor="e",
            compound="top",
            cursor="arrow",
            foreground="#9f9f9f",
            text='Version 1.0',
            textvariable=self.version_str)
        self.version_detail.place(
            anchor="se",
            relx=0.99,
            rely=0.98,
            width=200,
            x=0,
            y=0)
        self.mainwindow.pack(side="top")

        # Main widget
        self.mainwindow = self.mainwindow

    def run(self):
        self.mainwindow.mainloop()

    

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationUI(root)
    app.run()
