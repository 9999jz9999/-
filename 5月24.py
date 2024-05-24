# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:46:34 2024

@author: kkjj1
"""
#使用 tkinter 創建一個按鈕，點擊該按鈕後允許用戶輸入一段文本並將其寫入到選定目錄中的一個新文件中。
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox

# 主應用窗口
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("文本文件保存器")
        self.geometry("300x150")
        
        self.label = tk.Label(self, text="點擊按鈕輸入文本並保存到文件")
        self.label.pack(pady=20)
        
        self.button = tk.Button(self, text="輸入文本", command=self.input_text)
        self.button.pack(pady=20)
    
    def input_text(self):
        # 彈出對話框讓用戶輸入文本
        user_text = simpledialog.askstring("輸入文本", "請輸入要保存的文本:")
        
        if user_text:
            # 打開文件對話框讓用戶選擇目錄和文件名
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                try:
                    # 將文本寫入選定的文件
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(user_text)
                    messagebox.showinfo("成功", "文本已保存到文件")
                except Exception as e:
                    messagebox.showerror("錯誤", f"保存文件時出錯: {e}")

# 創建應用程序實例並運行
if __name__ == "__main__":
    app = App()
    app.mainloop()



#使用 tkinter 創建一個按鈕，點擊該按鈕後允許用戶選擇一個 CSV 文件並顯示其內容，並允許用戶添加新數據後保存。
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class CSVEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV 文件編輯器")
        self.geometry("600x400")
        
        self.csv_file_path = None
        self.data_frame = None

        self.load_button = tk.Button(self, text="加載 CSV 文件", command=self.load_csv)
        self.load_button.pack(pady=10)

        self.data_text = tk.Text(self, wrap=tk.NONE)
        self.data_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.new_data_label = tk.Label(self, text="添加新數據 (逗號分隔):")
        self.new_data_label.pack(pady=5)
        self.new_data_entry = tk.Entry(self)
        self.new_data_entry.pack(fill=tk.X, padx=10, pady=5)
        
        self.save_button = tk.Button(self, text="保存 CSV 文件", command=self.save_csv)
        self.save_button.pack(pady=10)

    def load_csv(self):
        self.csv_file_path = filedialog.askopenfilename(defaultextension=".csv",
                                                        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if self.csv_file_path:
            try:
                self.data_frame = pd.read_csv(self.csv_file_path)
                self.display_data()
            except Exception as e:
                messagebox.showerror("錯誤", f"加載文件時出錯: {e}")

    def display_data(self):
        self.data_text.delete(1.0, tk.END)
        self.data_text.insert(tk.END, self.data_frame.to_csv(index=False))

    def save_csv(self):
        new_data = self.new_data_entry.get()
        if self.csv_file_path and self.data_frame is not None and new_data:
            try:
                new_row = new_data.split(',')
                self.data_frame.loc[len(self.data_frame)] = new_row
                self.data_frame.to_csv(self.csv_file_path, index=False)
                self.display_data()
                self.new_data_entry.delete(0, tk.END)
                messagebox.showinfo("成功", "新數據已保存到文件")
            except Exception as e:
                messagebox.showerror("錯誤", f"保存文件時出錯: {e}")
        else:
            messagebox.showwarning("警告", "請確保所有欄位均已填寫，並已加載 CSV 文件")

# 創建應用程序實例並運行
if __name__ == "__main__":
    app = CSVEditor()
    app.mainloop()


#使用 tkinter 創建一個按鈕，點擊該按鈕後允許用戶選擇一個目錄，然後使用 os.walk 列出該目錄中的所有 .jpg 和 .png 文件並顯示其路徑。
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class ImageFileLister(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("圖像文件列表")
        self.geometry("600x400")
        
        self.select_dir_button = tk.Button(self, text="選擇目錄", command=self.select_directory)
        self.select_dir_button.pack(pady=10)

        self.file_list_text = tk.Text(self, wrap=tk.NONE)
        self.file_list_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.list_image_files(directory)

    def list_image_files(self, directory):
        self.file_list_text.delete(1.0, tk.END)
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    file_path = os.path.join(root, file)
                    self.file_list_text.insert(tk.END, file_path + '\n')

# 創建應用程序實例並運行
if __name__ == "__main__":
    app = ImageFileLister()
    app.mainloop()
