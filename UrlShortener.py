from tkinter import *
from tkinter import ttk
import pyperclip
import customtkinter

window = Tk()
window.title("G-URL Shortener")
window.configure(bg="#FBF4C4")
window.geometry("1260x700")

def generateLink():
    username = entry.get()
    print('Musta' + username) #INSERT FUNCTIONALITY AND INVALID INPUTS
    
def copyText():
    text = entry1.get()
    pyperclip.copy(text) 
    
def OpenLink():
    print('hello') #INSERT FUNCTIONALITY
    
def pasteText():
    clipboard_text = pyperclip.paste()
    entry.delete(0, END)  
    entry.insert(0, clipboard_text)

#GENERATE LINK
label = customtkinter.CTkLabel(window,
    font =('Consolas',17,'bold'), 
    text = 'Paste your link below',
    text_color='black')
label.place(x=370,y=195)

generateLink = customtkinter.CTkButton(
    window,
    font =('Georgia',20,'bold'), 
    text = 'Generate Link',
    corner_radius=300,
    fg_color='#21531C',  
    text_color='#FBF4C4',  
    hover_color='#3D6C38',
    width=100,
    height=50, 
    command = generateLink)

generateLink.place(x=531,y=283)

pasteText = customtkinter.CTkButton(
    window,
    text='PASTE',
    corner_radius=100,
    fg_color='#21531C',  
    text_color='#FBF4C4',  
    hover_color='#3D6C38',
    width=45,
    command=pasteText)
pasteText.place(x=920,y=237)

entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Enter your link here", 
    placeholder_text_color='#2B7025',
    font=('Times New Roman', 20),             
    fg_color="#21531C",                       
    text_color="white",                       
    corner_radius=300,                         
    width=570,                                
    height=50                                 
)
entry.place(x=630, y=250, anchor='center')

#SHORTENED LINK
label1 = customtkinter.CTkLabel(window,
    font =('Consolas',17,'bold'), 
    text = 'Shortened Link',
    text_color='black')
label1.place(x=370,y=360)

entry1 = customtkinter.CTkEntry(
    master=window,
    font=('Times New Roman', 20),             
    fg_color="#21531C",                       
    text_color="white",                       
    corner_radius=300,                         
    width=570,                                
    height=50)
entry1.place(x=630,y=415,anchor='center')

OpenLink = customtkinter.CTkButton(
    window,
    font =('Georgia',18,'bold'), 
    text = 'Open Shortened Link',
    corner_radius=300,
    fg_color='#21531C',  
    text_color='#FBF4C4',  
    hover_color='#3D6C38',
    width=100,
    height=48, 
    command = OpenLink)
OpenLink.place(x=506,y=448)

copyText = customtkinter.CTkButton(
    window,
    text=' COPY ',
    corner_radius=100,
    fg_color='#21531C',  
    text_color='#FBF4C4',  
    hover_color='#3D6C38',
    width=50,
    command=copyText)
copyText.place(x=920,y=403)

# DROPDOWN MENU
style = ttk.Style()
style.theme_use('default')  
style.configure(
    "Custom.TCombobox",            
    fieldbackground="#21531C",     
    foreground="white",            
    background="#FBF4C4",          
    selectbackground="#21531C",    
    selectforeground="white",     
)

label_dropdown = Label(window, 
                       text='Select the number of links to shorten:',
                       font=('Times New Roman', 11,'bold'),
                       fg='black',
                       bg='#FBF4C4')
label_dropdown.place(x=420, y=528)

dropdown = ttk.Combobox(window, 
                        values=['--    --', 2, 3], 
                        font=('Consolas', 10,'bold'),
                        style="Custom.TCombobox")
dropdown.current(0)  # Set default value
dropdown.place(x=678, y=530)

#ABOUT US
AboutUs = customtkinter.CTkButton(
    window,
    font =('Georgia',20,'bold'), 
    text = ' About Us ',
    corner_radius=300,
    fg_color='#21531C',  
    text_color='#FBF4C4',  
    hover_color='#3D6C38',
    width=100,
    height=50)
AboutUs.place(x=60, y=600)

#ABOUT US
TermsCondition = customtkinter.CTkButton(
    window,
    font =('Georgia',20,'bold'), 
    text = 'Terms & Condition',
    corner_radius=300,
    fg_color='#21531C',  
    text_color='#FBF4C4',  
    hover_color='#3D6C38',
    width=100,
    height=50)

TermsCondition.place(x=960, y=600)

window.mainloop()
