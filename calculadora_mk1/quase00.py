from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from calculadora026 import Ui_MainWindow  
from operacao00 import Operacao

class Calculadora_App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.usuarios = {
            'admin': 'sith',
            'merci': '1234567',
            'ribamar': 'vasco',
            'luva': 'pedreiro',
            'novousuario': 'novasenha'  # Adicione novos usuários aqui
        }
        self.ui = Ui_MainWindow()#criando meu obj com a interface grafica
        self.ui.setupUi(self)
        self.result = 0
        self.current_operation = ""
        self.calculator_on = True
        self.result_history = []
        self.ui.frame_4.hide()
        self.zero_button_press_count = 0
        self.ui.img.setPixmap(QPixmap('img/imgcalculadora00.png'))
        self.ui.foto_login.setPixmap(QPixmap('foto_login/imglog.png'))
        
        #### definido pag inicial ####
        self.ui.stackedWidget.setCurrentIndex(0)
        
        #### acoes dos botoes numericos ####       
        self.ui.botao0.clicked.connect(self.on_digit_pressed)
        self.ui.botao1.clicked.connect(self.on_digit_pressed)
        self.ui.botao2.clicked.connect(self.on_digit_pressed)
        self.ui.botao3.clicked.connect(self.on_digit_pressed)
        self.ui.botao4.clicked.connect(self.on_digit_pressed)
        self.ui.botao5.clicked.connect(self.on_digit_pressed)
        self.ui.botao6.clicked.connect(self.on_digit_pressed)
        self.ui.botao7.clicked.connect(self.on_digit_pressed)
        self.ui.botao8.clicked.connect(self.on_digit_pressed)
        self.ui.botao9.clicked.connect(self.on_digit_pressed)
        self.ui.botaoponto.clicked.connect(self.on_digit_pressed)     
        
        #### colocando imagens ####
        img_logo = self.recalcular_tam_imagem('img/imgcalculadora00.png',self.ui.img.width(),self.ui.img.height())
        self.ui.img.setPixmap(img_logo)
        img_login = self.recalcular_tam_imagem('img/loginimg1.png',self.ui.foto_login.width(),self.ui.foto_login.height())
        self.ui.foto_login.setPixmap(img_login)
       
        

        #### acoes dos boteos com operacoes e texto ####
        self.ui.botaoquadrado.clicked.connect(self.on_operator_pressed)
        self.ui.botaomais.clicked.connect(self.on_operator_pressed)
        self.ui.botaomenos.clicked.connect(self.on_operator_pressed)
        self.ui.botaomult.clicked.connect(self.on_operator_pressed)
        self.ui.botaodividir.clicked.connect(self.on_operator_pressed)
        self.ui.botaoigual.clicked.connect(self.calculate_result)
        self.ui.reset.clicked.connect(self.clear_display)
        self.ui.tela_inicial.clicked.connect(self.clear_display)
        self.ui.Del.clicked.connect(self.delete_last_char)
        self.ui.historico_page.clicked.connect(self.abri_historico)
        self.ui.volta_page.clicked.connect(self.volta_pagina)
        self.ui.entra.clicked.connect(self.efetuar_login)
        self.ui.tela_inicial.clicked.connect(self.volta_pagina)
        self.ui.voltar.clicked.connect(self.volta_pagina)
        self.ui.voltar.clicked.connect(self.clear_display)
        self.ui.entra.clicked.connect(self.on_digit_pressed)
        self.ui.tela_inicial.clicked.connect(self.on_digit_pressed)
        self.ui.entra.clicked.connect(self.efetuar_login)
        self.ui.botao0.clicked.connect(self.on_zero_button_pressed)
        self.ui.fecha_msg_erro.clicked.connect(lambda:self.ui.frame_4.hide())
        self.ui.reset.clicked.connect(self.on_reset_button_pressed)
        self.ui.cadastro.clicked.connect(self.volta_pagina)
        #self.ui.cadastros.clicked.connect(self.volta_pagina)
        self.clear_display()
    #### zera contagem  de zeros ####
    def on_reset_button_pressed(self):
         self.zero_button_press_count = 0
     
    #### codigo secreto zero ####
    def on_zero_button_pressed(self):
        self.zero_button_press_count += 1
        if  self.zero_button_press_count == 4:
            self.zero_button_press_count = 0  # Reseta a contagem
            self.ui.stackedWidget.setCurrentWidget(self.ui.tela_login)
            self.ui.frame_4.hide()
   
    #### redimensionado ####
    def recalcular_tam_imagem(self, end_imagem:str, w: int = 16, h: int = 16):
        logo = QPixmap(end_imagem)
        logo = logo.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio)
        return logo
    #### efetuando login ####
    def efetuar_login(self):
        usuario = self.ui.usuario_login.text()
        senha = self.ui.senha_login.text()
        if usuario in self.usuarios and senha == self.usuarios[usuario]:
            self.ui.usuario_login.setText('')
            self.ui.senha_login.setText('')
            self.ui.frame_4.hide()
            self.entra_diario()
            print('login realizado com sucesso')
        else:
            self.ui.erro_us.setText('seu login ou senha estao incorretos')
            self.ui.frame_4.show()
    #### entra no diario ####
    def entra_diario(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.diario)
    #### habilitar boteos no inicio ####
    def habilitar_botoes_operacao(self, liberar = True):
        self.ui.botaomais.setEnabled(liberar)
        self.ui.botaomenos.setEnabled(liberar)
        self.ui.botaomult.setEnabled(liberar)
        self.ui.botaodividir.setEnabled(liberar)
        self.ui.botaoigual.setEnabled(liberar)
        self.ui.botaoquadrado.setEnabled(liberar)
          #desativar la no qt

    #### amarzenar dados ####
    def armazena_dados(self):
        self.calculate_result()  
    
    #### limpar tela ####   
    def clear_display(self):
        self.ui.tela.setText("")
        self.result = 0
        self.current_operation = ""

    #### Apagar caractere ####
    def delete_last_char(self):
        current_display = self.ui.tela.text()
        new_display = current_display[:-1]
        self.ui.tela.setText(new_display)
    
    #### x² ####
    def quadrado(self):

        if self.current_operation == "x²":
            if "." in self.ui.tela.text():
                self.result = float(self.ui.tela.text())
                
        else:
            x = float(self.ui.tela.text())
            quadrado = x ** 2
            self.ui.tela.setText(str(quadrado))
            self.current_operation = ""  # Limpa a operação após o cálculo
            self.ui.tela.setText(f"{self.result}{self.current_operation}")
        return
              
    #### Abrir historico do resultado ####
    def abri_historico(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_historico)
        self.ui.hist.setRowCount(len(self.result_history))
        for row, operacao_obj in enumerate(self.result_history):
            valor1 = operacao_obj.get_valor1()
            operador = operacao_obj.get_operador()
            valor2 = operacao_obj.get_valor2()
            resultado = operacao_obj.get_resultado()
            item_valor1 = QtWidgets.QTableWidgetItem(str(valor1))
            item_operador = QtWidgets.QTableWidgetItem(str(operador))
            item_valor2 = QtWidgets.QTableWidgetItem(str(valor2))
            item_resultado = QtWidgets.QTableWidgetItem(str(resultado))
            self.ui.hist.setItem(row, 0, item_valor1)
            self.ui.hist.setItem(row, 1, item_operador)
            self.ui.hist.setItem(row, 2, item_valor2)
            self.ui.hist.setItem(row, 3, item_resultado)
     
    #### volta para primeira pag ####
    def volta_pagina(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.tela_de_cadastro)
        #self.ui.stackedWidget.setCurrentWidget(self.ui.tela_login)
    #### digitar ####
    def on_digit_pressed(self):
        
        if self.calculator_on:
            # sender(): indica quem realizou a acao
            digit = self.sender().text()
            
            current_display = self.ui.tela.text()
            if "." in digit:
                new_display = current_display + "."
                self.ui.tela.setText(new_display)
            else:
                new_display = current_display + digit
                self.ui.tela.setText(new_display)
        self.habilitar_botoes_operacao()
    
    ####valor decimal####
    def on_decimal_pressed(self):
        
        if self.calculator_on:
            
            current_display = self.ui.tela.text()
            if "." not in current_display:
                new_display = current_display + "."
                self.ui.tela.setText(new_display)
            print (current_display)
        return float(current_display)
    
    #### operadores ####
    def on_operator_pressed(self):
        
        if self.calculator_on:
            
            self.current_operation = self.sender().text()

            if "." in self.ui.tela.text():
                self.result = float (self.ui.tela.text())
            else:
                print(self.ui.tela.text())
                self.result = int(self.ui.tela.text())
                        
            self.ui.tela.setText(f"{self.result}{self.current_operation}")
    
    ####verificar ponto####
    def tem_ponto(self, result):
        if "." in result:
            return float(result)
    
    #### calculando resultado ####
    def calculate_result(self):
            ''' calculando resultado'''
            if self.current_operation == "+":
                esq_dir = self.ui.tela.text().split('+')
                if "." in esq_dir[0] or "."in esq_dir[1]:
                    self.result = float(esq_dir [0]) + float(esq_dir [1])
                else:
                    self.result = int(esq_dir [0]) + int(esq_dir [1])
            elif self.current_operation == "-":
                if self.current_operation == "-":
                    esq_dir = self.ui.tela.text().split('-')
                if "." in esq_dir[0] or "."in esq_dir[1]:
                    self.result = float(esq_dir [0]) - float(esq_dir [1])
                else:
                    self.result = int(esq_dir [0]) - int(esq_dir [1])
            elif self.current_operation == "x":
                if self.current_operation == "x":
                    esq_dir = self.ui.tela.text().split('x')
                if "." in esq_dir[0] or "."in esq_dir[1]:
                    self.result = float(esq_dir [0]) * float(esq_dir [1])
                else:
                    self.result = int(esq_dir [0]) * int(esq_dir [1])
            elif self.current_operation == "/":
                if self.current_operation == "/":
                    esq_dir = self.ui.tela.text().split('/')
                if "." in esq_dir[0] or "."in esq_dir[1]:
                    self.result = float(esq_dir [0]) / float(esq_dir [1])
                else:
                    self.result = int(esq_dir [0]) / int(esq_dir [1])
            elif self.current_operation == 'x²':
                esq_dir = self.ui.tela.text().split('x²')
                self.result = float(esq_dir [0] )** 2
            else:
                self.ui.tela.setText("Error")
                return
            
           # Criar objeto Operacao
            operacao_obj = Operacao(esq_dir[0], self.current_operation, esq_dir[1], self.result)
            self.result_history.append(operacao_obj)  # Adicionar o objeto Operacao à lista
            self.ui.tela.setText(str(self.result))
            self.current_operation = ""
if __name__ == "__main__":
    import sys
    app =QApplication(sys.argv)
    window = Calculadora_App()
    window.show()
    sys.exit(app.exec())


