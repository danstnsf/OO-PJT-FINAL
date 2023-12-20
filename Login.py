import tkinter as tk
from tkinter import ttk, messagebox
from Ludo import start

def cadastrar():
    username = entry_username.get()
    password = entry_password.get()

    with open('usuarios.txt', 'a') as file:
        file.write(f'{username},{password}\n')

    messagebox.showinfo('Cadastro', 'Cadastro realizado com sucesso!')

def fazer_login():
    username = entry_username_login.get()
    password = entry_password_login.get()

    with open('usuarios.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                messagebox.showinfo('Login', 'Login bem-sucedido!')
                root.destroy()
                start()
                return

    messagebox.showerror('Login', 'Usuário ou senha incorretos.')

# Interface Gráfica
root = tk.Tk()
root.title('Cadastro e Login')
root.geometry('800x630')

# Estilo de "jogos antigos"
root.tk_setPalette(background='#000000', foreground='#00ff00')

# Centralizar a janela na horizontal e vertical
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - 800) // 2
y_coordinate = (screen_height - 630) // 2
root.geometry(f'800x630+{x_coordinate}+{y_coordinate}')

# Adicionar uma label no topo
label_title = tk.Label(root, text='LUDO OO', bg='#000000', fg='#00ff00', font=('Fixedsys', 36))
label_title.pack(side='top', pady=20)

# Página de Cadastro
frame_cadastro = tk.Frame(root, bg='#000000')
frame_cadastro.pack(padx=10, pady=50)

label_username = tk.Label(frame_cadastro, text='Usuário:', bg='#000000', fg='#00ff00', font=('Fixedsys', 18))
label_username.grid(row=0, column=0, sticky='e')

label_password = tk.Label(frame_cadastro, text='Senha:', bg='#000000', fg='#00ff00', font=('Fixedsys', 18))
label_password.grid(row=1, column=0, sticky='e')

entry_username = tk.Entry(frame_cadastro, font=('Fixedsys', 18))
entry_username.grid(row=0, column=1, padx=5, pady=5)

entry_password = tk.Entry(frame_cadastro, show='*', font=('Fixedsys', 18))
entry_password.grid(row=1, column=1, padx=5, pady=5)

button_cadastrar = tk.Button(frame_cadastro, text='Cadastrar', command=cadastrar, bg='#000000', fg='#00ff00', font=('Fixedsys', 18))
button_cadastrar.grid(row=2, column=1, pady=10)

# Página de Login
frame_login = tk.Frame(root, bg='#000000')
frame_login.pack(padx=10, pady=10)

label_username_login = tk.Label(frame_login, text='Usuário:', bg='#000000', fg='#00ff00', font=('Fixedsys', 18))
label_username_login.grid(row=0, column=0, sticky='e')

label_password_login = tk.Label(frame_login, text='Senha:', bg='#000000', fg='#00ff00', font=('Fixedsys', 18))
label_password_login.grid(row=1, column=0, sticky='e')

entry_username_login = tk.Entry(frame_login, font=('Fixedsys', 18))
entry_username_login.grid(row=0, column=1, padx=5, pady=5)

entry_password_login = tk.Entry(frame_login, show='*', font=('Fixedsys', 18))
entry_password_login.grid(row=1, column=1, padx=5, pady=5)

button_login = tk.Button(frame_login, text='Login', command=fazer_login, bg='#000000', fg='#00ff00', font=('Fixedsys', 18))
button_login.grid(row=2, column=1, pady=10)

root.mainloop()
