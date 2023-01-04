from multiprocessing import Event
import requests
from PySimpleGUI import PySimpleGUI as sg
import sqlite3 as sq
        
sg.theme('darkblack1')


def janela_logon():
    
    layout = [
        [sg.Text('NSCAN é um software de código aberto que é alimentado por uma biblioteca HTTP em Python. ')],
        
        [sg.Text('Requests HTTP                Port Scanning')],
        [sg.Text('PING and Traceroute          Remote Access such TELNET,SSH,FTP etc.              ')],
        [sg.Text('Usuário')],[sg.Input(key='usuario1')],
        
        [sg.Text('Senha')],[sg.Input(key='senha1',password_char='*')],
        
        [sg.Button('Continuar',key='continuar')],
        [sg.Button('Esqueceu a senha?',key='red1')],
        
        
        [sg.Text('                                                              Produzido por:MATHEUSLOPES°')]
]

    return sg.Window('NSCAN for Network°',layout,finalize=True, no_titlebar=False)


def redefinir_senha():
    
    layout = [
        [sg.Text('Por favor,Confirme seu email:',key='email')],[sg.Input(key='email1')],
                                                            
        [sg.Text('Digite sua nova senha:',)],[sg.Input(key='novasenha1')],
        [sg.Text('Confirme sua nova senha:')] ,[sg.Input(key='confsenha1')],
        
        [sg.Button('Redefinir',key='redefinir1')]
                                                                        
        
    ]
    
    return sg.Window('Redefinir Senha',layout,finalize=True)

def janela_test():
    
    layout = [
        [sg.Text('Digite abaixo sua URL:',key='url')],[sg.Input(key='rurl')],
        
        [sg.Button('Testar',key='test1')],   [sg.Button('Voltar',key='voltar1')]
    ]
    
    return sg.Window('NSCAN for Network°',layout,finalize=True)




janelalog,janelatester,janelaredefinir=janela_logon(),None,None



while True:
    
    window, event,values = sg. read_all_windows()
    senha = values ['senha1']
    nome = values ['usuario1']
    #print(nome,senha)
    
    def cadastrar_dados():
        
        try:
            bank = sq.connect('random.db')
            cursor = bank.cursor()
            cursor.execute("INSERT INTO usuarios VALUES ('"+nome+"','"+senha+"')")
            bank.commit()
            bank.close()
            print('DADOS INSERIDOS COM SUCESSO')
        except sq.Error as erro:
            print('ERRO AO INSERIR NO BANCO DE DADOS')
        
    def atualizar_dados():
    
        try:
            bank= sq.connect('random.db')
            cursor = bank.cursor()
            cursor.execute('''UPDATE usuarios SET senha = 5000 WHERE senha > 0''')
            bank.commit()
            bank.close()
            print('QUERIDO DBA , DADOS FORAM ATUALIZADOS!')
        except sq.Error as erro :
            print('DADOS NÃO FORAM ATUALIZADOS!')
            
        
    def deletar_dados():
        
        try :
            bank = sq.connect('random.db')
            cursor = bank.cursor()
            cursor.execute('''DELETE FROM usuarios WHERE senha = 5000 ''')
            bank.commit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            bank.close()
            print('DBA,DADOS FORAM EXCLUIDOS!')
        except sq.Error as erro :
            print('DADOS NÃO FORAM EXCLUIDOS')
            
            
            
        
    if window == janelalog == event == sg.WINDOW_CLOSED:
        break
    
    elif window == janelalog and event == 'continuar':
        janelatester=janela_test() ; janelalog.hide() ; cadastrar_dados()
                                                
    elif window == janelatester and values == 'test1':
    #pegando valor de um l     
        r=requests.get (values['rurl'])
        codificacao=r.encoding
        head=r.headers
        pagina=r.text
        codigo=r.status_code
        sg.popup ('Status da Conexão:',codigo, 'Status da Codificacao:',codificacao,head)
        
    
    elif  window == janelalog and  event == 'red1' :
        janelaredefinir=redefinir_senha() ; janelalog.hide()
        
    elif window == janelaredefinir and event == 'redefinir1' :
        atualizar_dados() 
                  
        
    

            