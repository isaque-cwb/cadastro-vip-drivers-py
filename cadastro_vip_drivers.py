import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Usuario():
    def __init__(self, id, nome, tel, email, indicado):
        self.id = id
        self.nome = nome
        self.tel = tel
        self.email = email
        self.indicado = indicado


class Controlador(object):
    def __init__(self):
        self.modelo_armazenamento: Gtk.ListStore = Builder.get_object("dados_parceiro")
        self.Stack = Builder.get_object("stack")
        self.banco_dados = []

    def on_tela_principal_destroy(self, window):
        Gtk.main_quit()

    def on_button_login_clicked(self, button):
        nome = Builder.get_object("nome").get_text()
        senha = Builder.get_object("senha").get_text()
        lembrar = Builder.get_object("lembrar").get_active()
        self.login(nome, senha, lembrar)

    def login(self, nome, senha, lembrar):
        if nome == 'admin' and senha == '1234':
            self.mensagem('Bem-vindo!', 'Usuário logado com sucesso!', 'emblem-default')
            self.Stack.set_visible_child_name("tela_inicial")
            Window.props.title = 'Cadastro Vip Drivers'
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

    def on_button_cadastrar_clicked(self, button):
        self.Stack.set_visible_child_name("tela_cadastro")

    def on_button_listar_inicial_clicked(self, button):
        self.Stack.set_visible_child_name("tela_listar")

    def on_button_sair_clicked(self, button):
        self.Stack.set_visible_child_name("tela_login")

    def on_button_cad_voltar_clicked(self, button):
        self.Stack.set_visible_child_name("tela_inicial")

    def on_button_listar_voltar_clicked(self, button):
        self.Stack.set_visible_child_name("tela_inicial")

    def on_button_lista_clicked(self, button):
        self.modelo_armazenamento.clear()
        for Usuario in self.banco_dados:
            self.modelo_armazenamento.append((Usuario.id, Usuario.nome, Usuario.tel, Usuario.email, Usuario.indicado))

    def on_button_cad_cadastrar_clicked(self, button):
        nome = Builder.get_object("nome_cad").get_text()
        tel = Builder.get_object("tel_cad").get_text()
        email = Builder.get_object("email_cad").get_text()
        indicado = Builder.get_object("indicado_cad").get_text()
        rua = Builder.get_object("rua_cad").get_text()
        numero = Builder.get_object("num_cad").get_text()
        bairro = Builder.get_object("bairro_cad").get_text()
        cidade = Builder.get_object("cidade_cad").get_text()
        nome_fam = Builder.get_object("nome_cad_familiar").get_text()
        tel_fam = Builder.get_object("tel_cad_familiar").get_text()
        modelo = Builder.get_object("modelo_cad").get_text()
        cor = Builder.get_object("cor_cad").get_text()
        placa = Builder.get_object("placa_cad").get_text()

        if nome != '':
            self.banco_dados.append(Usuario(len(self.banco_dados)+1, nome, tel, email, indicado))
            self.mensagem('Aviso', 'Usuário ' + nome + ' cadastrado!', 'dialog-emblem-default')
        else:
            self.mensagem('Aviso', 'Campo "Nome" Obrigatório!', 'dialog-error')




    def on_lembrar_toggled(self, activ):
        pass


Builder = Gtk.Builder()
Builder.add_from_file("inteface_grafica.glade")
Builder.connect_signals(Controlador())
Window: Gtk.Window = Builder.get_object("tela_principal")
Window.show_all()
Gtk.main()
