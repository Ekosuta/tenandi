import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Chirago')
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w = 500
        h = 450
        x = int(sw/2 + w)
        y = int(sh/2)
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self._set_appearance_mode('system')
        

        # search bar
        self.search_entry = ctk.CTkEntry(self, placeholder_text='Search in English or Tenandi')
        self.search_entry.grid(row=0, column=1, sticky='ew', pady=(20, 10))

        # search button
        self.search_button = ctk.CTkButton(self, text='search', command=self.search)
        self.search_button.grid(row=1, column=1, pady=(0, 10))

    def search(self):
        pass

    