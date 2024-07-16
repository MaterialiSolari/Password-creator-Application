import customtkinter
from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkFont, CTkFrame
import random
import string

class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('900x900')
        self.configure(fg_color='white')  # Set the background color of the main window to white

        self.my_font_title = customtkinter.CTkFont('Arial Black', 35)
        self.my_font_description = customtkinter.CTkFont('Arial', 20)
        self.my_font_subheader = customtkinter.CTkFont('Arial', 20)
        self.boxes_font = CTkFont('Arial', 17)
        self.chosen_characters = customtkinter.CTkFont('Arial', 15)

        self.label = customtkinter.CTkLabel(master=self, text="Secure Password Generator",
                                            font=self.my_font_title, fg_color='white', text_color='black')
        self.label.pack(pady=40)
        self.label.place(relx=0.5, rely=0.06, anchor='center')

        self.label2 = customtkinter.CTkLabel(master=self, text='Create strong and secure passwords based on your preferences',
                                             font=self.my_font_subheader, fg_color='white', text_color='black')
        self.label2.place(relx=0.5, rely=0.12, anchor='center')

        self.frame = CTkFrame(master=self, fg_color='black', border_color='#808080', width=5000, height=2, border_width=0, corner_radius=0)
        self.frame.pack(expand=True)
        self.frame.place(relx=0.5, rely=0.17, anchor='center')
        
        self.description = customtkinter.CTkLabel(master=self, 
                                                  text='Use the fields below to specify your preferences for the password. Select the number of upper\n case letters, lower case letters, numbers, and punctuation symbols you want in your\n password.', fg_color='white',
                                                  text_color='black', font=self.my_font_description)
        self.description.pack(expand=True)
        self.description.place(relx=0.5, rely=0.23, anchor='center')

        self.upperCaseLetters = customtkinter.CTkLabel(master=self, text="Upper Case Letters", 
                                                       text_color='black', font=self.boxes_font)
        self.upperCaseLetters.pack(expand=True)
        self.upperCaseLetters.place(relx=0.15, rely=0.4, anchor='center')
        self.upperCaseLettersEntry = CTkEntry(master=self, placeholder_text="...", width=95, height=35)
        self.upperCaseLettersEntry.place(relx=0.15, rely=0.44, anchor='center')

        self.lowercaseLetter = customtkinter.CTkLabel(master=self, text='Lower Case Letters', text_color='black', font=self.boxes_font)
        self.lowercaseLetter.place(relx=0.41, rely=0.4, anchor='center')
        self.LowerCaseLettersEntry = CTkEntry(master=self, placeholder_text="...", width=95, height=35)
        self.LowerCaseLettersEntry.place(relx=0.41, rely=0.44, anchor='center')

        self.Numbers = customtkinter.CTkLabel(master=self, text='Numbers', text_color='black', font=self.boxes_font)
        self.Numbers.place(relx=0.62, rely=0.4, anchor='center')
        self.NumbersEntry = CTkEntry(master=self, placeholder_text="...", width=95, height=35)
        self.NumbersEntry.place(relx=0.62, rely=0.44, anchor='center')

        self.PunctuationSymbols = customtkinter.CTkLabel(master=self, text='Punctuation Symbols', text_color='black', font=self.boxes_font)
        self.PunctuationSymbols.place(relx=0.84, rely=0.4, anchor='center')
        self.PunctuationSymbolsEntry = CTkEntry(master=self, placeholder_text="...", width=95, height=35)
        self.PunctuationSymbolsEntry.place(relx=0.84, rely=0.44, anchor='center')


        self.button = CTkButton(master=self, text='Generate Password', fg_color="#e3f92a", 
                                border_width=0, width=80, height=50, text_color='black', command=self.submission)
        self.button.place(relx=0.5, rely=0.52, anchor='center')

        self.resultLabel = CTkLabel(master=self, text='Generated Password', fg_color='white',
                                    text_color='black', font=self.boxes_font)
        self.resultLabel.place(relx=0.5, rely=0.6, anchor='center')

        self.ResultEntry = CTkEntry(master=self, placeholder_text='......', width=550, height=35)
        self.ResultEntry.place(relx=0.5, rely=0.65, anchor='center')
        self.buttonClipBoard = CTkButton(master=self, text='Copy to Clipboard', fg_color="#e3f92a", 
                                border_width=0, width=80, height=50, text_color='black', 
                                command=self.copy_toClipboard)
        self.buttonClipBoard.place(relx=0.5, rely=0.72, anchor='center')
        self.product = CTkButton(master=self, text='Show Chosen Characters', fg_color="#e3f92a", 
                                border_width=0, width=550, height=30, text_color='black', command=self.show_characters)
        self.product.place(relx=0.5, rely=0.79, anchor='center')

    def generate_random_uppercase_letter(self):
        num_count = 0
        random_letters = []
        user_input_letters = int(self.upperCaseLettersEntry.get())

        if user_input_letters > 0:     
            while num_count < user_input_letters:
                upper_case_letter = chr(random.randint(65, 90))
                random_letters.append(upper_case_letter)
                num_count += 1
            print(f'These are your randomly chosen upper case letters: {" - ".join(random_letters)}')

        elif user_input_letters == 0:
            print('No upper case letter will be added')

        return random_letters

    def generate_random_lowercase_letter(self):
        num_count = 0
        random_lower_case_letters = []
        user_input_letter = int(self.LowerCaseLettersEntry.get())

        if user_input_letter > 0:
            while num_count < user_input_letter:
                random_lowercase = chr(random.randint(97, 122))
                random_lower_case_letters.append(random_lowercase)
                num_count += 1
            print(f'These are your randomly chosen lower case letters: {" - ".join(random_lower_case_letters)}')

        elif user_input_letter == 0:
            print('No lower case letters will be added')
        
        return random_lower_case_letters

    def generate_random_number(self):
        num_count = 0
        num_array = []
        user_input_number = int(self.NumbersEntry.get())

        if user_input_number > 0:
            while num_count < user_input_number:
                random_number = random.randint(0, 9)
                num_array.append(str(random_number))
                num_count += 1
            print(f'These are your randomly chosen numbers: {" - ".join(num_array)}')

        elif user_input_number == 0:
            print('No numbers will be added')
        
        return num_array

    def generate_random_punctuation_sign(self):
        punctuation_count = 0
        punctuation_array = []
        user_input_punctuation = int(self.PunctuationSymbolsEntry.get())

        if user_input_punctuation > 0:
            while punctuation_count < user_input_punctuation:
                random_punctuation = random.choice(string.punctuation)
                punctuation_array.append(random_punctuation)
                punctuation_count += 1
            print(f'These are your randomly chosen punctuations: {" ,".join(punctuation_array)}')

        elif user_input_punctuation == 0:
            print('No punctuations will be added')
        return punctuation_array

    def submission(self):
        self.pass1 = self.generate_random_uppercase_letter() 
        self.pass2 = self.generate_random_lowercase_letter() 
        self.pass3 = self.generate_random_number() 
        self.pass4 = self.generate_random_punctuation_sign()

        combined_password = self.pass1 + self.pass2 + self.pass3 + self.pass4

        random.shuffle(combined_password)
        shuffled_password = ''.join(combined_password)
        print(f'This is your password: {shuffled_password}')
        self.ResultEntry.delete(0, 'end')
        self.ResultEntry.insert(0, shuffled_password)
    
    def copy_toClipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.ResultEntry.get())
        self.update()
    
    def show_characters(self):
        self.pass1Label = CTkLabel(master=self, text=f'Upper Case Letters:   {" ".join(self.pass1)}', font=self.chosen_characters)
        self.pass1Label.place(relx=0.5, rely=0.85, anchor='center')
        self.pass2Label = CTkLabel(master=self, text=f'Lower Case Letters:   {" ".join(self.pass2)}', font=self.chosen_characters)
        self.pass2Label.place(relx=0.5, rely=0.88, anchor='center')
        self.pass3Label = CTkLabel(master=self, text=f'Numbers:   {" ".join(self.pass3)}', font=self.chosen_characters)
        self.pass3Label.place(relx=0.5, rely=0.92, anchor='center')
        self.pass4Label = CTkLabel(master=self, text=f'Punctuation Symbols:   {" ".join(self.pass4)}', font=self.chosen_characters)
        self.pass4Label.place(relx=0.5, rely=0.9618, anchor='center')

if __name__ == "__main__":
    app = App()
    app.mainloop()
