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
            width=1050)
        self.mainlabel = ttk.Label(self.mainwindow, name="mainlabel")
        self.mainlabel.configure(
            font="{Times New Roman} 20 {bold}",
            padding=5,
            text='Calibration Data Automation Tool')
        self.mainlabel.place(anchor="nw", height=50, width=700, x=0, y=0)
        self.db_select_button = ttk.Button(
            self.mainwindow, name="db_select_button")
        self.db_select_button.configure(padding=5, text='Select Database')
        self.db_select_button.place(
            anchor="w", height=35, width=150, x=10, y=75)
        self.db_select_button.configure(command=self.on_select_db_button_click)
        self.ct_load_button = ttk.Button(
            self.mainwindow, name="ct_load_button")
        self.ct_load_button.configure(padding=5, text='Load calibration table')
        self.ct_load_button.place(
            anchor="w", height=35, width=150, x=10, y=125)
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
        self.path_db.place(anchor="w", height=30, width=500, x=200, y=75)
        self.path_ct = ttk.Entry(self.mainwindow, name="path_ct")
        self.selected_ct_path = tk.StringVar(value='calibration table path')
        self.path_ct.configure(
            font="{Times New Roman} 12 {}",
            justify="left",
            state="readonly",
            textvariable=self.selected_ct_path)
        _text_ = 'calibration table path'
        self.path_ct["state"] = "normal"
        self.path_ct.delete("0", "end")
        self.path_ct.insert("0", _text_)
        self.path_ct["state"] = "readonly"
        self.path_ct.place(anchor="w", height=30, width=500, x=200, y=125)
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
            anchor="nw", height=250, width=340, x=10, y=170)
        self.log_feedback2 = tk.Message(self.mainwindow, name="log_feedback2")
        self.txtbox_feedback_2 = tk.StringVar()
        self.log_feedback2.configure(
            anchor="nw",
            aspect=32000,
            background="#f0f0f0",
            font="{Courier New} 8 {}",
            justify="left",
            relief="sunken",
            textvariable=self.txtbox_feedback_2)
        self.log_feedback2.place(
            anchor="nw",
            height=250,
            width=340,
            x=360,
            y=170)
        separator1 = ttk.Separator(self.mainwindow)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="w", height=1, width=710, x=0, y=160)
        separator2 = ttk.Separator(self.mainwindow)
        separator2.configure(orient="vertical")
        separator2.place(anchor="nw", height=500, width=1, x=710, y=0)
        self.multi_button = ttk.Button(self.mainwindow, name="multi_button")
        self.multibutton_str = tk.StringVar(value='CONFIRM')
        self.multi_button.configure(
            state="disabled",
            text='CONFIRM',
            textvariable=self.multibutton_str)
        self.multi_button.place(anchor="nw", height=50, width=120, x=10, y=430)
        self.multi_button.configure(command=self.on_multi_click)
        self.logo_monti = ttk.Label(self.mainwindow, name="logo_monti")
        self.img_logo_Monti = image_loader("logo_Monti.png")
        self.logo_monti.configure(
            font="{Courier} 20 {}",
            image=self.img_logo_Monti,
            text='logo_Monti.png')
        self.logo_monti.place(anchor="ne", width=225, x=970, y=25)
        self.detail = ttk.Label(self.mainwindow, name="detail")
        self.detail.configure(
            anchor="n",
            foreground="#9f9f9f",
            text='ULTRA database calibration table update tool')
        self.detail.place(anchor="nw", width=240, x=460, y=5)
        self.dev_detail = ttk.Label(self.mainwindow, name="dev_detail")
        self.dev_detail.configure(
            anchor="e",
            foreground="#9f9f9f",
            text='Developed by Poxmin, MONTI systems s.r.o.')
        self.dev_detail.place(anchor="se", width=280, x=700, y=485)
        self.version_detail = ttk.Label(self.mainwindow, name="version_detail")
        self.version_str = tk.StringVar(value='Version 1.0')
        self.version_detail.configure(
            anchor="e",
            compound="top",
            cursor="arrow",
            foreground="#9f9f9f",
            text='Version 1.0',
            textvariable=self.version_str)
        self.version_detail.place(anchor="se", width=150, x=1035, y=485)
        self.grpaher = tk.Canvas(self.mainwindow, name="grpaher")
        self.grpaher.configure(borderwidth=1, relief="sunken")
        self.grpaher.place(anchor="sw", height=300, width=300, x=725, y=450)
        self.mainwindow.pack(side="top")

        # Main widget
        self.mainwindow = self.mainwindow

    def run(self):
        self.mainwindow.mainloop()

    

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationUI(root)
    app.run()
