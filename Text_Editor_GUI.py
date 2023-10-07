
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("ну вот такой вот...")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    """Открыть файл для редактирования."""
    filepath = askopenfilename(
        filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')]
        )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    try:
        with open(filepath, 'r', encoding='utf-8') as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
    except UnicodeDecodeError:
        # Если не удается декодировать файл как UTF-8, попробуйте другие кодировки, например, cp1251
        with open(filepath, 'r', encoding='cp1251') as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
    window.title(f"Thecleverprogrammer - {filepath}")

def save_file():
    """Сохранить текущий файл как новый файл."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')]
    )
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Thecleverprogrammer - {filepath}")

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)
btn_save = tk.Button(fr_buttons, text="Сохранить как...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()




