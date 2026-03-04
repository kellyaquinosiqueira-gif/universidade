from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton
)

from screen.cadastrar import Cadastrar
from screen.Listar import Listar

import sys  

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        
        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(400, 200)
        self.janela.setLayout(self.layout)
        
        self.criar_botoes()
        self.aplicar_estilo()  # ← adicionamos apenas isso
        
        self.janela.show()
        
        
    def criar_botoes(self):
        botao_cadastrar = QPushButton("Cadastro")
        self.layout.addWidget(botao_cadastrar)
        botao_cadastrar.clicked.connect(self.abrir_cadastro)
    
        botao_listar = QPushButton("Listar")
        self.layout.addWidget(botao_listar)
        botao_listar.clicked.connect(self.abrir_listagem)
         
    # 🔥 ESTILO PADRÃO DO SISTEMA
    def aplicar_estilo(self):
        self.janela.setStyleSheet("""
            QWidget {
                background-color: #0B3D2E;
                color: black;
                font-family: Arial;
                font-size: 14px;
            }

            QPushButton {
                background-color: #145A32;
                border-radius: 10px;
                padding: 12px;
                font-weight: bold;
                margin: 12px;
                color: black;
            }

            QPushButton:hover {
                background-color: #27AE60;
            }

            QPushButton:pressed {
                background-color: #0E6655;
            }
        """)
         
    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.app)
        self.tela_cadastro.janela.show()
           
    def abrir_listagem(self):
        self.tela_listagem = Listar(self.app)
        self.tela_listagem.janela.show()
        
        
if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())