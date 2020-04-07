import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Usuario_dados_parceiro():
    def __init__(self, id, nome, tel, email, indicado):
        self.id = id
        self.nome = nome
        self.tel = tel
        self.email = email
        self.indicado = indicado

class Usuario_endereco_parceiro():
    def __init__(self, rua, numero, bairro, cidade):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade


class Usuario_dados_carro():
    def __init__(self, modelo, cor, placa):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa

class Usuario_contato_familiar():
    def __init__(self, nome_familiar, tel_familiar):
        self.nome_familiar = nome_familiar
        self.tel_familiar = tel_familiar


class Controlador(object):
    def __init__(self):
        self.Stack = Builder.get_object("stack")

        self.modelo_armazenamento_dados_parceiro: Gtk.ListStore = Builder.get_object("dados_parceiro")
        self.modelo_armazenamento_endereco_parceiro: Gtk.ListStore = Builder.get_object("endereco_parceiro")
        self.modelo_armazenamento_dados_carro: Gtk.ListStore = Builder.get_object("dados_carro")
        self.modelo_armazenamento_dados_contato_familiar: Gtk.ListStore = Builder.get_object("contato_familiar")

        self.banco_dados_parceiro = []
        self.banco_dados_endereco_parceiro = []
        self.banco_dados_carro = []
        self.banco_dados_contato_familiar = []



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
        self.modelo_armazenamento_dados_parceiro.clear()
        self.modelo_armazenamento_endereco_parceiro.clear()
        self.modelo_armazenamento_dados_carro.clear()
        self.modelo_armazenamento_dados_contato_familiar.clear()

        for Usuario_dados_parceiro in self.banco_dados_parceiro:
                self.modelo_armazenamento_dados_parceiro.append((Usuario_dados_parceiro.id,
                                              Usuario_dados_parceiro.nome,
                                              Usuario_dados_parceiro.tel,
                                              Usuario_dados_parceiro.email,
                                              Usuario_dados_parceiro.indicado))

        for Usuario_endereco_parceiro in self.banco_dados_endereco_parceiro:
                self.modelo_armazenamento_endereco_parceiro.append((Usuario_endereco_parceiro.rua,
                                              Usuario_endereco_parceiro.numero,
                                              Usuario_endereco_parceiro.bairro,
                                              Usuario_endereco_parceiro.cidade))


        for Usuario_dados_carro in self.banco_dados_carro:
                self.modelo_armazenamento_dados_carro.append((Usuario_dados_carro.modelo,
                                              Usuario_dados_carro.cor,
                                              Usuario_dados_carro.placa))

        for Usuario_contato_familiar in self.banco_dados_contato_familiar:
                self.modelo_armazenamento_dados_contato_familiar.append((Usuario_contato_familiar.nome_familiar,
                                              Usuario_contato_familiar.tel_familiar))

        print(self.banco_dados_parceiro)



    def on_button_cad_cadastrar_clicked(self, button):

        nome = Builder.get_object("nome_cad").get_text()
        tel = Builder.get_object("tel_cad").get_text()
        email = Builder.get_object("email_cad").get_text()
        indicado = Builder.get_object("indicado_cad").get_text()

        rua = Builder.get_object("rua_cad").get_text()
        numero = Builder.get_object("num_cad").get_text()
        bairro = Builder.get_object("bairro_cad").get_text()
        cidade = Builder.get_object("cidade_cad").get_text()

        cor = Builder.get_object("cor_cad").get_text()
        placa = Builder.get_object("placa_cad").get_text()
        modelo = Builder.get_object("modelo_cad").get_text()

        nome_fam = Builder.get_object("nome_cad_familiar").get_text()
        tel_fam = Builder.get_object("tel_cad_familiar").get_text()

        if nome != '':
            self.banco_dados_parceiro.append(Usuario_dados_parceiro(len(self.banco_dados_parceiro) + 1,
                                                                    nome, tel, email, indicado))
            self.banco_dados_endereco_parceiro.append(Usuario_endereco_parceiro(rua, numero, bairro, cidade))
            self.banco_dados_carro.append(Usuario_dados_carro(modelo, cor, placa))
            self.banco_dados_contato_familiar.append(Usuario_contato_familiar(nome_fam, tel_fam))

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
