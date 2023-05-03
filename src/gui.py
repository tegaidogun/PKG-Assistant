import tkinter as tk
from tkinter import filedialog
from downloader import download_and_extract_packages

def show_gui():
    def browse_tsv_file():
        file_path = filedialog.askopenfilename(filetypes=[("TSV Files", "*.tsv")])
        tsv_file_path.set(file_path)

    def start_downloading():
        ranges = ranges_entry.get().replace(" ","")
        download_and_extract_packages(ranges, tsv_file_path.get(), delete_after_unpack.get(), auto_apply_zrif.get(), store_in_zip.get())

    root = tk.Tk()
    root.title("PKG Downloader and Extractor")

    tsv_file_path = tk.StringVar()
    delete_after_unpack = tk.BooleanVar()
    auto_apply_zrif = tk.BooleanVar()
    store_in_zip = tk.BooleanVar()

    tk.Label(root, text="TSV File Path:").grid(row=0, column=0, sticky="w")
    tk.Entry(root, textvariable=tsv_file_path, width=50).grid(row=0, column=1)
    tk.Button(root, text="Browse", command=browse_tsv_file).grid(row=0, column=2)

    tk.Label(root, text="Line Ranges:").grid(row=1, column=0, sticky="w")
    ranges_entry = tk.Entry(root, width=50)
    ranges_entry.grid(row=1, column=1)

    tk.Checkbutton(root, text="Delete after unpack", variable=delete_after_unpack).grid(row=2, column=0, sticky="w")
    tk.Checkbutton(root, text="Auto apply zRIF", variable=auto_apply_zrif).grid(row=3, column=0, sticky="w")
    tk.Checkbutton(root, text="Store in One ZIP File", variable=store_in_zip).grid(row=4, column=0, sticky="w")

    tk.Button(root, text="Start Downloading", command=start_downloading).grid(row=5, columnspan=3)

    root.mainloop()
