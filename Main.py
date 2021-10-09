import tkinter as tk
from tkinter import Button, Menu, image_names, ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
from tkinter.constants import END
from typing import Text


root = tk.Tk()
sx = root.winfo_screenwidth()
sy = root.winfo_screenheight()
root.geometry(f'{sx}x{sy}')
root.title('Text Editor | -Aditya Banik')


###################################| All Icons |###################################

New_File_Icon = tk.PhotoImage(file='Icons/New-File.png').subsample(2, 2)
Open_File_Icon = tk.PhotoImage(file='Icons/Open-File.png').subsample(2, 2)
Save_File_Icon = tk.PhotoImage(file='Icons/Save-File.png').subsample(2, 2)
Save_As_Icon = tk.PhotoImage(file='Icons/Save-As.png').subsample(2, 2)
Exit_Icon = tk.PhotoImage(file='Icons/Exit.png').subsample(2, 2)


Copy_Text_Icon = tk.PhotoImage(file='Icons/Copy-Text.png').subsample(2, 2)
Past_Text_Icon = tk.PhotoImage(file='Icons/Paste.png').subsample(2, 2)
cut_Text_Icon = tk.PhotoImage(file='Icons/Cut.png').subsample(2, 2)
Clear_Text_Icon = tk.PhotoImage(file='Icons/Clear.png').subsample(2, 2)
Find_Text_Icon = tk.PhotoImage(file='Icons/Find.png').subsample(2, 2)


ToolBar_Icon = tk.PhotoImage(file='Icons/ToolBar.png').subsample(2, 2)
status_Bar_Icon = tk.PhotoImage(file='Icons/Status-Bar.png').subsample(2, 2)


White_Theme_Icon = tk.PhotoImage(file='Icons/White-Theme.png').subsample(2, 2)
Dark_Theme_Icon = tk.PhotoImage(file='Icons/Dark-Theme.png').subsample(2, 2)

Bold_Button_Icon = tk.PhotoImage(file='Icons/Bold-Button.png').subsample(2, 2)
Under_Line_Icon = tk.PhotoImage(file='Icons/Under-Line.png').subsample(2, 2)
Italick_Icon = tk.PhotoImage(file='Icons/Italick.png').subsample(2, 2)
Font_color_Icon = tk.PhotoImage(file='Icons/Font-Color.png').subsample(2, 2)

Aline_Left_Icon = tk.PhotoImage(file='Icons/Aline-Left.png').subsample(2, 2)
Aline_Center_Icon = tk.PhotoImage(
    file='Icons/Aline-Center.png').subsample(2, 2)
Aline_Right_Icon = tk.PhotoImage(file='Icons/Aline-Right.png').subsample(2, 2)

#################################| End All Icons |#################################


###################################| Main Menu |###################################

main_menu = tk.Menu()

file = tk.Menu(main_menu, tearoff=False)

edit = tk.Menu(main_menu, tearoff=False)

view = tk.Menu(main_menu, tearoff=False)

color_Theme = tk.Menu(main_menu, tearoff=False)

theme = tk.StringVar()
color_icons = (White_Theme_Icon, Dark_Theme_Icon)

color_dic = {
    'Light Default ': ('#000000', '#ffffff'),
    'Dark ': ('#c4c4c4', '#2d2d2d')
}
count = 0


# ===| Adding Cascade |===

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_Theme)

#################################| End Main Menu |#################################


####################################| Toolbar |####################################

tool_Bar = ttk.Label(root)
tool_Bar.pack(side=tk.TOP, fill=tk.X)

# Font Box
font_Tuple = font.families()
font_family = tk.StringVar()
font_Box = ttk.Combobox(
    tool_Bar, width=30, textvariable=font_family, state='readonly')
font_Box['values'] = font_Tuple
font_Box.current(font_Tuple.index('Mongolian Baiti'))
font_Box.grid(row=0, column=0, padx=5)

# Size Box
size_var = tk.StringVar()
font_Size = ttk.Combobox(
    tool_Bar, width=14, textvariable=size_var, state='readonly')
font_Size['values'] = tuple(range(8, 80))
font_Size.current(9)
font_Size.grid(row=0, column=1, padx=5)

# Bold Button
bold_btn = ttk.Button(tool_Bar, image=Bold_Button_Icon, width=0)
bold_btn.grid(row=0, column=2, padx=5)

# Italick Button
Italick_btn = ttk.Button(tool_Bar, image=Italick_Icon, width=0)
Italick_btn.grid(row=0, column=3, padx=5)

# Under Line Button
under_line_btn = ttk.Button(tool_Bar, image=Under_Line_Icon, width=0)
under_line_btn.grid(row=0, column=4, padx=5)

# Font Color Button
Font_color_btn = ttk.Button(tool_Bar, image=Font_color_Icon, width=0)
Font_color_btn.grid(row=0, column=5, padx=5)

# Aline Left Button
Aline_Left_btn = ttk.Button(tool_Bar, image=Aline_Left_Icon, width=0)
Aline_Left_btn.grid(row=0, column=6, padx=5)

# Aline Center Button
aline_center_btn = ttk.Button(tool_Bar, image=Aline_Center_Icon, width=0)
aline_center_btn.grid(row=0, column=7, padx=5)

# Aline Right Button
aline_right_btn = ttk.Button(tool_Bar, image=Aline_Right_Icon, width=0)
aline_right_btn.grid(row=0, column=8, padx=5)

##################################| End Toolbar |##################################


##################################| Text Editor |##################################

Text_Editor = tk.Text(root)
Text_Editor.config(wrap='word', relief=tk.FLAT)

Scrool_Bar = tk.Scrollbar(root)
Text_Editor.focus_set()
Scrool_Bar.pack(side=tk.RIGHT, fill=tk.Y)
Text_Editor.pack(fill=tk.BOTH, expand=True)
Scrool_Bar.config(command=Text_Editor.yview)
Text_Editor.config(yscrollcommand=Scrool_Bar.set)

# Font Functinality
current_Font_Family = 'Mongolian Baiti'
current_Font_Size = 17


def Change_Font(root):
    global current_Font_Family
    current_Font_Family = font_family.get()
    Text_Editor.configure(font=(current_Font_Family, current_Font_Size))


def Change_Font_Size(root):
    global current_Font_Size
    current_Font_Size = size_var.get()
    Text_Editor.configure(font=(current_Font_Family, current_Font_Size))


font_Box.bind("<<ComboboxSelected>>", Change_Font)
font_Size.bind("<<ComboboxSelected>>", Change_Font_Size)

# Bold Button Functinality


def Change_Bold():
    Text_Property = font.Font(font=Text_Editor['font'])
    if Text_Property.actual()['weight'] == 'normal':
        Text_Editor.configure(
            font=(current_Font_Family, current_Font_Size, 'bold'))

    if Text_Property.actual()['weight'] == 'bold':
        Text_Editor.configure(
            font=(current_Font_Family, current_Font_Size, 'normal'))


bold_btn.configure(command=Change_Bold)

# italick Button Functinality


def Change_Italick():
    Text_Property = font.Font(font=Text_Editor['font'])
    if Text_Property.actual()['slant'] == 'roman':
        Text_Editor.configure(
            font=(current_Font_Family, current_Font_Size, 'italic'))

    if Text_Property.actual()['slant'] == 'italic':
        Text_Editor.configure(
            font=(current_Font_Family, current_Font_Size, 'roman'))


Italick_btn.configure(command=Change_Italick)

# Under Line Button Functinality


def Change_UnderLine():
    Text_Property = font.Font(font=Text_Editor['font'])
    if Text_Property.actual()['underline'] == 0:
        Text_Editor.configure(
            font=(current_Font_Family, current_Font_Size, 'underline'))

    if Text_Property.actual()['underline'] == 1:
        Text_Editor.configure(
            font=(current_Font_Family, current_Font_Size, 'normal'))


under_line_btn.configure(command=Change_UnderLine)

# Font color Functinality


def Change_Font_Color():
    Color_Var = colorchooser.askcolor()
    Text_Editor.configure(fg=Color_Var[1])


Font_color_btn.configure(command=Change_Font_Color)

# Aline Left Functinality


def Aline_Left():
    Text_Content = Text_Editor.get(1.0, END)
    Text_Editor.tag_config('left', justify=tk.LEFT)
    Text_Editor.delete(1.0, END)
    Text_Editor.insert(tk.INSERT, Text_Content, 'left')


Aline_Left_btn.configure(command=Aline_Left)

# Aline Center Functinality


def Aline_Center():
    Text_Content = Text_Editor.get(1.0, END)
    Text_Editor.tag_config('center', justify=tk.CENTER)
    Text_Editor.delete(1.0, END)
    Text_Editor.insert(tk.INSERT, Text_Content, 'center')


aline_center_btn.configure(command=Aline_Center)

# Aline Right Functinality


def Aline_Right():
    Text_Content = Text_Editor.get(1.0, END)
    Text_Editor.tag_config('right', justify=tk.RIGHT)
    Text_Editor.delete(1.0, END)
    Text_Editor.insert(tk.INSERT, Text_Content, 'right')


aline_right_btn.configure(command=Aline_Right)

Text_Editor.configure(font=('Mongolian Baiti', 17))

################################| End Text Editor |################################


###################################| Status Bar |##################################

Status_bar = ttk.Label(root, text='Status Bar')
Status_bar.pack(side=tk.BOTTOM)

Text_Change = False


def Change(even=None):
    global Text_Change
    if Text_Editor.edit_modified():
        Text_Change = True
        words = len(Text_Editor.get(1.0, 'end-1c').split())
        characters = len(Text_Editor.get(1.0, 'end-1c').replace(' ', ''))
        Status_bar.configure(
            text=f'Total Characters : {characters} Total Words : {words}')
    Text_Editor.edit_modified(False)


Text_Editor.bind("<<Modified>>", Change)

#################################| End Status Bar |################################


#############################| Main Menu Functinality |############################

# File Menu

url = ''


def New_File(event=None):
    global url
    url = ''
    Text_Editor.delete(1.0, tk.END)


def Open_File(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title='Select File', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
    try:
        with open(url, 'r') as File:
            Text_Editor.delete(1.0, tk.END)
            Text_Editor.insert(0.1, File.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url)+' | - Aditya Banik')


def Save_As(event=None):
    global url
    try:
        content = Text_Editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
            ('Text File', '*.txt'), ('All Fils', '*.*')))
        url.write(content)
        url.close()
    except:
        return


def Save(event=None):
    global url
    try:
        if url:
            content = str(Text_Editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as File:
                File.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
                ('Text File', '*.txt'), ('All Fils', '*.*')))
            con = str(Text_Editor.get(1.0, tk.END))
            url.write(con)
            url.close()

    except Exception as e:
        return e


def Exit(event=None):
    global url, Text_Change
    try:
        if Text_Change:
            mbox = messagebox.askyesnocancel(
                'Warning', 'Do You Want To Save This File ?')
            if mbox is True:
                if url:
                    content = Text_Editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as File:
                        File.write(content)
                        root.destroy()
                else:
                    content2 = str(Text_Editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
                        ('Text File', '*.txt'), ('All Fils', '*.*')))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return

# Edit Menu


def Find(event=None):

    def Fin():
        word = fi.get()
        Text_Editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = Text_Editor.search(
                    word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                Text_Editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                Text_Editor.tag_config(
                    'match', foreground='red', background='yellow')

    def Rep():
        word = fi.get()
        rt = ri.get()
        content = Text_Editor.get(1.0, tk.END)
        nc = content.replace(word, rt)
        Text_Editor.delete(1.0, tk.END)
        Text_Editor.insert(1.0, nc)

    fd = tk.Toplevel()
    fd.geometry('450x250+500+200')
    fd.title('Find')
    fd.resizable(0, 0)

    ff = ttk.LabelFrame(fd, text='Find/Replace')
    ff.pack(pady=20)

    tfl = ttk.Label(ff, text='Find : ')
    trl = ttk.Label(ff, text='Replace : ')

    fi = ttk.Entry(ff, width=30)
    ri = ttk.Entry(ff, width=30)

    fb = ttk.Button(ff, text='Find', command=Fin)
    rb = ttk.Button(ff, text='Replace', command=Rep)

    tfl.grid(row=0, column=0, padx=4, pady=4)
    trl.grid(row=1, column=0, padx=4, pady=4)

    fi.grid(row=0, column=1, pady=4, padx=4)
    ri.grid(row=1, column=1, pady=4, padx=4)

    fb.grid(row=2, column=0, pady=4, padx=8)
    rb.grid(row=2, column=1, pady=4, padx=8)

    fd.mainloop()

# File Commands


file.add_command(label='New File', image=New_File_Icon,
                 compound=tk.LEFT, accelerator='Ctrl+N', command=New_File)
file.add_command(label='Open File', image=Open_File_Icon,
                 compound=tk.LEFT, accelerator='Ctrl+O', command=Open_File)
file.add_command(label='Save As', image=Save_As_Icon,
                 compound=tk.LEFT, accelerator='Ctrl+Shift+S', command=Save_As)
file.add_command(label='Save', image=Save_File_Icon,
                 compound=tk.LEFT, accelerator='Ctrl+S', command=Save)
file.add_command(label='Exit', image=Exit_Icon,
                 compound=tk.LEFT, accelerator='Ctrl+Q', command=Exit)

# Edit commands


def clear(event=None):
    Text_Editor.delete(1.0, END)


edit.add_command(label='Copy', image=Copy_Text_Icon, compound=tk.LEFT,
                 accelerator='Ctrl+C', command=lambda: Text_Editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=Past_Text_Icon, compound=tk.LEFT,
                 accelerator='Ctrl+V', command=lambda: Text_Editor.event_generate("<Control p>"))
edit.add_command(label='Cut', image=cut_Text_Icon, compound=tk.LEFT,
                 accelerator='Ctrl+X', command=lambda: Text_Editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=Clear_Text_Icon,
                 compound=tk.LEFT, accelerator='Ctrl+Shift+C', command=clear)
edit.add_command(label='Find', image=Find_Text_Icon,
                 compound=tk.LEFT, accelerator='Ctrl+F', command=Find)

# View Check Button

Tool = tk.BooleanVar()
Tool.set(True)
Status = tk.BooleanVar()
Status.set(True)


def tb():
    global Tool
    if Tool:
        tool_Bar.pack_forget()
        Tool = False
    else:
        Text_Editor.pack_forget()
        Status_bar.pack_forget()
        tool_Bar.pack(side=tk.TOP, fill=tk.X)
        Text_Editor.pack(fill=tk.BOTH, expand=True)
        Status_bar.pack(side=tk.BOTTOM)
        Tool = True


def sb():
    global Status
    if Status:
        Status_bar.pack_forget()
        Status = False
    else:
        Status_bar.pack(side=tk.BOTTOM)
        Status = True


view.add_checkbutton(label='Tool Bar', image=ToolBar_Icon, compound=tk.LEFT,
                     onvalue=True, offvalue=False, variable=Tool, command=tb)
view.add_checkbutton(label='Status Bar', image=status_Bar_Icon, compound=tk.LEFT,
                     onvalue=True, offvalue=False, variable=Status, command=sb)

# Color Theme


def them():
    T = theme.get()
    ct = color_dic.get(T)
    fg_c, bg_c = ct[0], ct[1]
    Text_Editor.config(bg=bg_c, fg=fg_c)


count = 0
for i in color_dic:
    color_Theme.add_radiobutton(
        label=i, image=color_icons[count], variable=theme, compound=tk.LEFT, command=them)
    count += 1

###########################| End Main Menu Functinality |##########################

root.config(menu=main_menu)

# ====================================================================================
root.bind("<Control-n>", New_File)
root.bind("<Control-o>", Open_File)
root.bind("<Control-s>", Save)
root.bind("<Control-S>", Save_As)
root.bind("<Control-f>", Find)
root.bind("<Control-q>", Exit)
root.bind("<Control-C>", clear)


root.mainloop()
