import customtkinter as ctk
from logic.search_logic import search
from data.dictionary import dictionary_data
from data.conjugations import conjugation_data

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
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self._set_appearance_mode('system')
        
        # search bar
        self.search_entry = ctk.CTkEntry(self, placeholder_text='Search in English or Tenandi', width=175)
        self.search_entry.grid(row=1, column=1, pady=(0, 10))

        # search button
        self.search_button = ctk.CTkButton(
            self,
            text='search',
            command=self.handle_search,
            corner_radius=10,
            width=100
            )
        self.search_button.grid(row=1, column=1, pady=(70, 10))

        # enter button configuration
        self.bind('<Return>', lambda event: self.handle_search())

    def handle_search(self):
        term = self.search_entry.get()
        result1 = search(term, dictionary_data)
        result2 = search(term, conjugation_data)
        if term in dictionary_data and term in conjugation_data:
            return result1, result2
        elif term in dictionary_data:
            self.word_result_frame()
            return result1
        
    def word_result_frame(self):
        self.word_frame = ctk.CTkTabview(self, width=400, height=400, fg_color=('#D1E4BB', '#929E84'))
        self.word_frame.grid(row=2, columnspan=3)

        # creating tabs and result object
        self.word_frame.add('Translation')
        self.word_frame.add('Morphology')
        self.word_frame.add('Prounciation')
        result = self.handle_search()

        # translation tab widgets
        self.word = ctk.CTkLabel(self.word_frame.tab('Translation'), text=(result['translation']))
        self.word.pack()

        # morphology tab widgets


        # pronunciation tab widgets

    
