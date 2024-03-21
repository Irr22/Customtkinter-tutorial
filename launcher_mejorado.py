import minecraft_launcher_lib, os, subprocess, tkinter, customtkinter

ventana = tkinter.Tk()
ventana.geometry('450x350')
ventana.title('Launcher MC')
ventana.resizable(False,False)

user_window = os.environ["USERNAME"]
minecraft_directori = f"C:/Users/{user_window}/AppData/Roaming/.minecraftLauncher"

bt_ejecutar_minecraft = customtkinter.CTkButton(ventana, text="Ejecutar")
bt_instalar_versiones = customtkinter.CTkButton(ventana, text="Instalar Vanilla")
bt_instalar_forge = customtkinter.CTkButton(ventana, text="Instalar Forge")

label_nombre = tkinter.Label(text='NOMBRE')
laber_ram = tkinter.Label(text='RAM')

entry_versiones = customtkinter.CTkEntry(ventana, placeholder_text="Ingresa version")
entry_nombre = customtkinter.CTkEntry(ventana, placeholder_text="Ingresa nombre")
entry_ram = customtkinter.CTkEntry(ventana, placeholder_text="Ingresa la ram")

versiones_forge = ['0','0','0']

# Ver todas las versiones que tengo instaladas y mostrarla en un desplegable
versiones_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directori)

versiones_instaladas_lista = []
for versiones_instaladas in versiones_instaladas:
    versiones_instaladas_lista.append(versiones_instaladas['id'])

if len(versiones_instaladas_lista) != 0: # Comprovar haver si ahy versiones instaladas
    vers = tkinter.StringVar(ventana)
    vers.set(versiones_instaladas_lista[0])
elif len(versiones_instaladas_lista) == 0:
    vers = 'sin versiones instaladas'
    versiones_instaladas_lista.append('sin versiones instaladas')

versiones_menu_desplegable = customtkinter.CTkOptionMenu(ventana,values = versiones_instaladas_lista) # Para crear el desplegable con donde se va a crear que va a mostrar y que opciones tiene
versiones_menu_desplegable.configure()

def instalar_minecraft():
    version = entry_versiones.get()
    if version:
        minecraft_launcher_lib.install.install_minecraft_version(version,minecraft_directori)
        print(f'Se ha instalado la version {version}')
    else:
        print('No se ingreso ninguna version')

def instalar_forge():
    global versiones_forge_menu_desplegable
    version = versiones_forge_menu_desplegable._current_value
    minecraft_launcher_lib.forge.install_forge_version(version,minecraft_directori)
    print('Forge instalado')

def ejecutar_minecraft():
    mine_user = entry_nombre.get()
    version = vers.get()
    ram = f"-Xmx{entry_ram.get()}G"

    options = {
        'username': mine_user,
        'uuid' : '',
        'token': '',

        'jvArguments': [ram,ram], # 4G es para 4 de gigas de RAM
        'launcherVersion': "0.0.2"
    }

    ventana.destroy()
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version,minecraft_directori,options)
    subprocess.run(minecraft_command)

def instalar_versiones_normales():
    global entry_versiones
    ventana_versiones = tkinter.Toplevel(ventana)
    entry_versiones = customtkinter.CTkEntry(ventana_versiones,placeholder_text="Version")
    entry_versiones.place(x=10,y=0) # Podeis poner la posicion como querais

    bt_instalar_vers = customtkinter.CTkButton(ventana_versiones,command=instalar_minecraft,text='Instalar')
    bt_instalar_vers.place(x=10,y=50) # Podeis poner la posicion como querais

def instalar_versiones_forge():
    global entry_versiones, versiones_forge, vers_forge, versiones_forge_menu_desplegable
    ventana_versiones = tkinter.Toplevel(ventana)
    entry_versiones = customtkinter.CTkEntry(ventana_versiones, placeholder_text="Version")
    entry_versiones.place(x=0,y=0) # Podeis poner la posicion como querais

    bt_instalar_vers = customtkinter.CTkButton(ventana_versiones,command=instalar_forge,text='Instalar')
    bt_instalar_vers.place(x=0,y=150) # Podeis poner la posicion como querais

    bt_instalar_ver_vers = customtkinter.CTkButton(ventana_versiones,command=lambda:ver_versiones_forge(ventana_versiones),text='Ver versiones')
    bt_instalar_ver_vers.place(x=0,y=50) # Podeis poner la posicion como querais

    vers_forge = tkinter.StringVar(ventana_versiones)
    versiones_forge_menu_desplegable = customtkinter.CTkOptionMenu(ventana_versiones, values = versiones_forge)
    versiones_forge_menu_desplegable.configure()
    versiones_forge_menu_desplegable.place(x=0,y=100)

def ver_versiones_forge(ventana):
    global vers_forge, versiones_forge, versiones_forge_menu_desplegable

    # Obtener las nuevas opciones (pueden ser de cualquier origen)
    versiones_forge = saver_versiones_instaladas_forge(entry_versiones.get())

    vers_forge = tkinter.StringVar(ventana)
    versiones_forge_menu_desplegable = customtkinter.CTkOptionMenu(ventana, values = versiones_forge)
    versiones_forge_menu_desplegable.configure()
    versiones_forge_menu_desplegable.place(x=0,y=100)

def saver_versiones_instaladas_forge(version):
    numero = str(version)[2:]
    ultima_terminacion = None
    ultima_version = None
    versiones_forge_instaladas = []
    for version_de_minecraft in minecraft_launcher_lib.forge.list_forge_versions():
        if int(numero) >= 10:
            if ultima_version != version_de_minecraft[0:6]:
                if version_de_minecraft[2] == str(numero)[0] and ultima_terminacion != version_de_minecraft[5]:
                    if version_de_minecraft[3] == str(numero)[1]:
                        versiones_forge_instaladas.append(version_de_minecraft)
                        ultima_terminacion = version_de_minecraft[5]
                        ultima_version = version_de_minecraft[0:6]

        elif int(numero) >= 1 and version_de_minecraft[5] == '.' or version_de_minecraft[5] == '-':
            if ultima_version != version_de_minecraft[0:5]:
                if version_de_minecraft[2] == str(numero):
                    versiones_forge_instaladas.append(version_de_minecraft)
                    ultima_terminacion = version_de_minecraft[4]
                    ultima_version = version_de_minecraft[0:5]

    return versiones_forge_instaladas

def menu():
    bt_instalar_versiones.configure(command=instalar_versiones_normales)
    bt_instalar_versiones.place(x=250,y=50)

    bt_instalar_forge.configure(command=instalar_versiones_forge)
    bt_instalar_forge.place(x=250,y=100)

    label_nombre.place(x=50,y=50)
    laber_ram.place(x=50,y=100)

    entry_nombre.place(x=50,y=70)
    entry_ram.place(x=50,y=120)

    bt_ejecutar_minecraft.configure(command=ejecutar_minecraft)
    bt_ejecutar_minecraft.place(x=50,y=250)

    versiones_menu_desplegable.place(x=50,y=200)
        
    ventana.mainloop()

menu()