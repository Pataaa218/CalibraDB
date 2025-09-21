#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import CalTabUpToolui as baseui
import handleTables as table

#declaration
err_report = ["No error detected",
              "Err: unknown formatting of calibration table",
              "Err: file was not chosen or is missing",
              "Err: stopped by user - incorrect data"]
db_path = ""
ct_path = ""

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
        log = f'Collected data:\nTank n.\nTank size: \nProduct: \nInactive: \nIndexed: \nPress Continue to search file, or\nselect a different file.'
        self.txtbox_feedback_1.set(log)
        log = 'Note: You are using beta version\nof this program.\nCollected data are only\ndumped to new .txt file\nin directory of program.'
        self.txtbox_feedback_2.set(log)
        self.multibutton_str.set('Continue')
        self.multi_button.configure(state="normal")


    def on_multi_click(self):
        _str = self.multibutton_str.get()
        if _str == 'Continue':
            global ct_path
            self.multi_button.configure(state="disabled")
            table.handleCalibrationTable(ct_path)
            log = f'Collected data:\nTank n.{table.tNumber}\nTank size: {table.tSize}\nProduct: {table.tProduct}\nInactive: {table.tHeightVolume[0]:.3f}\nIndexed: {len(table.tHeightVolume)}\nPress CONFIRM to write, or\nselect a new file.'
            self.txtbox_feedback_1.set(log)
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

