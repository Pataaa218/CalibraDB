#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import CalTabUpToolui as baseui
import handleTables as table
import math

#declaration
err_report = ["No error detected",
              "Err: unknown formatting of calibration table",
              "Err: file was not chosen or is missing",
              "Err: stopped by user - incorrect data"]
db_path = ""
ct_path = ""
WIDTH, HEIGHT = 300, 300


def draw_graph(canvas, array):
        canvas.delete("all")
        length = len(array)
        Y_MAX = length - 1 if length > 1 else 1
        X_MAX = array[length-1]

        def map_x(x):
            return 5 + (x / X_MAX) * (WIDTH-10)
        def map_y(y):
            return ((-y / Y_MAX) * HEIGHT) + HEIGHT
        
        for i in range(length - 1):
            x1, y1 = array[i], i
            x2, y2 = array[i+1], i+1
            canvas.create_line(map_x(x1), map_y(y1), map_x(x2), map_y(y2), fill="blue", width=1)


class Application(baseui.ApplicationUI):
    def __init__(self, master=None):
        super().__init__(master)

    def on_select_db_button_click(self):
        global db_path
        #path = table.selectFile(table.mdb_title, table.mdb_type)
        #self.selected_db_path.set(path)
        pass

    def on_load_ct_button_click(self):
        global ct_path
        ct_path = table.selectFile(table.ct_title, table.txt_type)
        self.selected_ct_path.set(ct_path)
        log = f'Data to collect:\nTank n.\nTank size: \nProduct: \nInactive zone: \nIndexed: \n\nPress Continue to search file, or\nselect a different file.'
        self.txtbox_feedback_1.set(log)
        log = 'Note: You are using a beta version\nof this program.\n\nCollected data are only\ndumped to new .txt file\nin directory of this program.'
        self.txtbox_feedback_2.set(log)
        self.multibutton_str.set('Continue')
        self.multi_button.configure(state="normal")


    def on_multi_click(self):
        _str = self.multibutton_str.get()
        if _str == 'Continue':
            global ct_path
            self.multi_button.configure(state="disabled")
            table.handleCalibrationTable(ct_path, self.txtbox_feedback_1, root)
            draw_graph(self.grpaher, table.tHeightVolume)
            self.multibutton_str.set('CONFIRM')
            self.multi_button.configure(state="normal")
        else:
            table.tmpFileDump()
            self.multi_button.configure(state="disabled")
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MONTI - MDB calibration tables update tool")
    app = Application(root)
    app.run()

