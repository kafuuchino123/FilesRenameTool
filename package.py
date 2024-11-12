import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# 定义批量重命名并移动文件的函数
def rename_and_move_files():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    prefix = prefix_entry.get()
    extension = extension_entry.get()

    # 检查输入是否有效
    if not input_folder or not output_folder or not prefix or not extension:
        messagebox.showerror("错误", "请填写所有字段")
        return

    try:
        # 创建输出文件夹（如果不存在）
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # 遍历输入文件夹中的所有文件
        for index, filename in enumerate(os.listdir(input_folder)):
            file_path = os.path.join(input_folder, filename)

            # 如果是符合指定扩展名的文件
            if os.path.isfile(file_path) and filename.endswith(extension):
                new_name = f"{prefix}_{index}{extension}"
                new_file_path = os.path.join(output_folder, new_name)

                # 移动并重命名文件
                shutil.copy(file_path, new_file_path)
                print(f"Renamed and moved: {filename} to {new_name}")

        messagebox.showinfo("完成", "文件已成功重命名并移动！")
    except Exception as e:
        messagebox.showerror("错误", f"发生错误: {str(e)}")

# 定义文件夹选择函数
def choose_input_folder():
    folder_path = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, folder_path)

def choose_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_path)

# 清空输入框
def clear_entries():
    input_folder_entry.delete(0, tk.END)
    output_folder_entry.delete(0, tk.END)
    prefix_entry.delete(0, tk.END)
    extension_entry.set("")  # 清空 Combobox 的内容

# 创建主窗口
root = tk.Tk()
root.title("批量文件重命名和移动工具")

# 输入文件夹路径
tk.Label(root, text="选择输入文件夹:").grid(row=0, column=0, padx=10, pady=5)
input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="选择文件夹", command=choose_input_folder).grid(row=0, column=2, padx=10, pady=5)

# 输出文件夹路径
tk.Label(root, text="选择输出文件夹:").grid(row=1, column=0, padx=10, pady=5)
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="选择文件夹", command=choose_output_folder).grid(row=1, column=2, padx=10, pady=5)

# 文件前缀输入框
tk.Label(root, text="重命名前缀:").grid(row=2, column=0, padx=10, pady=5)
prefix_entry = tk.Entry(root, width=50)
prefix_entry.grid(row=2, column=1, padx=10, pady=5)

# 文件扩展名选择框
tk.Label(root, text="需更改的文件类型:").grid(row=3, column=0, padx=10, pady=5)
extension_entry = ttk.Combobox(root, width=47)
extension_entry['values'] = (".jpg", ".png", ".jpeg", ".txt", ".pdf", ".docx", ".xlsx")  # 常用文件扩展名选项
extension_entry.grid(row=3, column=1, padx=10, pady=5)

# 开始重命名按钮
tk.Button(root, text="开始重命名并移动", command=rename_and_move_files).grid(row=4, column=1, pady=20)

# 清空按钮
tk.Button(root, text="清空输入", command=clear_entries).grid(row=5, column=1, pady=10)

root.mainloop()
