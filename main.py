# Passo a passo
#Titulo: chatNET
#Botao: iniciar chat
    #popup
        #Titulo: Bem vindo ao chatNET
        #Campo de texto: Escreva seu nome
        #Botão: Entrar no chat
            #Sumiu com o titulo e o botão inicial
            #fechar popup
            #criar o chat (com a mensagem de "nome do usuário entrou no chat")
                # campo de texto: Digite sua mensagem
                # Botão enviar
                    #Aparecer mensagem no chat com o nome do usuario
# Flet -> aplicativo/site/programa de computador            
import flet as ft

def main(pagina):
    titulo = ft.Text("chatNET")
    titulo_janela = ft.Text("Bem Vindo ao chatNET")
    campo_nome_usuario = ft.TextField(label="Nome de Usuário")
    texto_mensagem = ft.TextField(label="Digite sua mensagem")

    chat = ft.Column()
    linha_mensagem = ft.Row([texto_mensagem, ft.ElevatedButton("Enviar", on_click=lambda e: enviar_mensagem())])

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    def enviar_mensagem():
        if texto_mensagem.value:
            texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
            pagina.pubsub.send_all(texto)
            texto_mensagem.value = ""
            pagina.update()


    def entrar_chat(evento):
        pagina.controls.clear()
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)

        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    
    janela = ft.AlertDialog(title=titulo_janela,
                            content=campo_nome_usuario,
                            actions=[botao_entrar])

    pagina.add(titulo)
    pagina.add(botao_iniciar)

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # cria o tunel de comunicação
ft.app(main, view=ft.WEB_BROWSER)


