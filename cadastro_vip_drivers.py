import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class Controlador(object):
    def __init__(self):
        pass

    def on_tela_principal_destroy(self, window):
        Gtk.main_quit()

    def on_button_login_clicked(self, button):
        nome = Builder.get_object("nome").get_text()
        senha = Builder.get_object("senha").get_text()
        lembrar = Builder.get_object("lembrar").get_active()
        self.login(nome, senha, lembrar)

    def login(self, nome, senha, lembrar):
        if nome ==  'admin' and senha == '1234':
            self.mensagem('Bem-vindo!', 'Usuário logado com sucesso!', 'emblem-default')
        else:
            self.mensagem('Aviso!', 'Email ou senha incorretos!', 'dialog-error')

    def mensagem(self, param, param1, param2):
        mensagem: Gtk.MessageDialog = Builder.get_object('mensagem')
        mensagem.props.text = param
        mensagem.props.secondary_text = param1
        mensagem.props.icon_name = param2
        mensagem.show_all()
        mensagem.run()
        mensagem.hide()




Builder = Gtk.Builder()
Builder.add_from_file("inteface_grafica.glade")
Builder.connect_signals(Controlador())
Window: Gtk.Window = Builder.get_object("tela_principal")
Window.show_all()
Gtk.main()
