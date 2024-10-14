import flet as ft

def main(pagina):
    texto = ft.Text('Hashzap')
    chat = ft.Column()
    nome_usuario = ft.TextField(label= 'Escreva seu nome')

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem ['tipo']
        if tipo == 'mensagem':
            texto_mensagem = mensagem ['texto']
            usuario_mensagem = mensagem ['usuario']

            # Adicionar mensagem no chat
            chat.controls.append(ft.Text (f'{usuario_mensagem} : {texto_mensagem}'))
        else:
            usuario_mensagem = mensagem['usuario']
            chat.controls.append(ft.Text (f'{usuario_mensagem} entrou no chat', size=12, italic=True, color= ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all ({
            'texto': campo_mensagem.value, 
            'usuario': nome_usuario.value, 
            'tipo': 'mensagem'
            })
        
        # Limpar mensagem
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField (label= 'Digite uma mesagem', on_submit= enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton ('Enviar', on_click= enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all ({'usuario': nome_usuario.value, 'tipo': 'entrada'})

        # Adionar o chat
        pagina.add(chat)

        # Fechar o popup
        popup.open = False

        # Remover o botão iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        # Criar o campo de mensagem do usuario
        # Criar o botao de enviar mensagem do usuario
        pagina.add(ft.Row ([campo_mensagem, botao_enviar_mensagem]))
        pagina.update()


    popup = ft.AlertDialog(
        open= False,
        modal= True,
        title= ft.Text ('Bem vindo(a) ao Hashzap'),
        actions= [ft.ElevatedButton ('Entrar', on_click= entrar_popup)],
    )

    def entrar_chat(evento):
        pagina.overlay.append(popup)
        popup.open = True
        pagina. update ()

    botao_iniciar = ft.ElevatedButton ('Iniciar chat', on_click= entrar_chat)

    pagina.add(texto)
    pagina.add(nome_usuario)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)

# Deploy
