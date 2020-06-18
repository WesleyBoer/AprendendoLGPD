# Personagens
define p = Character("[protagonista]", color="fff896")
define a = Character("Jimmy (Assistente)", color="fc0303")
define k = Character("Kevin", color="a5eb7c")
define d = Character("Developer", color="f2eddf")

# Imagens - Backgrounds
image AssisBg = "images/AssisBg.jpg"
image QuartoBg = "images/quartobg.png"
image CafeBg = "images/cafebg.png"
image Office = "images/office.png"
image UmAnoDepois = "images/UmAnoDepois.jpg"
image UmDiaDepois = "images/UmDiaDepois.jpg"
image PesquisaNoPC = "images/PesquisaNoPC.jpg"
image ComputadorZoom1 = "images/ComputadorZoom1.png"
image ComputadorZoom2 = "images/ComputadorZoom2.png"
image ComputadorZoom3 = "images/ComputadorZoom3.png"
image ComputadorZoom4 = "images/ComputadorZoom4.png"
image ComputadorZoom5 = "images/ComputadorZoom5.png"
image ComputadorZoom6 = "images/ComputadorZoom6.png"


# Imagens - Personagens
image AssisNormal = "images/AssisNormal.png"
image AssisFeliz = "images/AssisFeliz.png"
image AssisPensativo = "images/AssisPensativo.png"
image AssisBravo = "images/AssisBravo.png"
image ProtPensativo = "images/ProtPensativo.png"
image ProtFalando = "images/ProtFalando.png"
image ProtNormal = "images/ProtNormal.png"
image ProtEmpolgado = "images/ProtEmpolgado.png"
image ProtSurpreso = "images/ProtSurpreso.png"
image ProtComMedo = "images/ProtMedo.png"
image ProtIndeciso = "images/ProtIndeciso.png"
image KevinNormal = "images/KevinNormal.png"
image KevinFalando = "images/KevinFalando.png"
image KevinReceoso = "images/KevinReceoso.png"
image KevinPensativo = "images/KevinPensativo.png"
image KevinBravo = "images/KevinBravo.png"
image KevinInseguro = "images/KevinInseguro.png"
image KevinInseguroQuieto = "images/KevinInseguroQ.png"
image DevNormal = "images/DevNormal.png"
image DevSmile = "images/DevSmile.png"
image DevFalando = "images/DevFalando.png"
image Contrato = "images/contrato.png"



label start:
    
    $ pontuacao = 0
    
    scene AssisBg
    with dissolve

    show AssisNormal at right:
        zoom 0.5
    with dissolve
    a "Olá! Bem-vindo ao Aprendendo LGPD."
    a "O meu nome é Jimmy e eu serei o seu assistente durante o game."
    a "Qual é o seu nome?"
    $ protagonista = renpy.input("Qual é o seu nome?")
    hide AssisNormal
    show AssisPensativo at right:
        zoom 0.5
    with dissolve
    a "Legal, %(protagonista)s!"
    hide AssisPensativo
    show AssisNormal at right:
        zoom 0.5
    with dissolve
    a "%(protagonista)s, eu não irei influenciar na história do jogo e não terei nenhuma conexão com os personagens, beleza?"
    hide AssisNormal
    show AssisFeliz at right:
        zoom 0.5
    with dissolve
    a "Entao, vamos lá!"
    jump capitulo1
    
    return

label capitulo1:

    scene QuartoBg
    with dissolve

    show ProtPensativo at left:
        zoom 0.5
    with dissolve
    p "Acho que chegou a hora de montar a minha própria empresa..."
    p "Eu sempre quis ter uma agência de talentos..."
    p "Já sei! Vou falar com o Kevin e ver o que ele acha da idéia!"

    scene CafeBg
    with dissolve
    hide ProtPensativo
    show ProtNormal at left:
        zoom 0.5
    with dissolve
    show KevinNormal at right:
        zoom 0.5
    with dissolve
    "Você e Kevin resolvem se encontrar para discutir a idéia de abrir uma agência de talentos."

    hide ProtNormal
    show ProtFalando at left:
        zoom 0.5
    p "Cara, estava pensando em lançar uma agência de talentos. O que você acha?"

    hide KevinNormal
    hide ProtFalando
    show ProtNormal at left:
        zoom 0.5
    show KevinFalando at right:
        zoom 0.5
    k "Como assim? Como funcionaria?"

    hide ProtNormal
    hide KevinFalando
    show KevinNormal at right:
        zoom 0.5
    show ProtFalando at left:
        zoom 0.5
    p "Pelo o que eu andei estudando, não seria difícil."
    p "Nós iremos fazer a gestão de pessoas que possuem algum tipo de talento e possa nos trazer rentabilidade."

    hide KevinNormal
    hide ProtFalando
    show ProtNormal at left:
        zoom 0.5
    show KevinFalando at right:
        zoom 0.5
    k "Legal! O que iríamos precisar para executar o projeto?"

    hide ProtNormal
    hide KevinFalando
    show KevinNormal at right:
        zoom 0.5
    show ProtPensativo at left:
        zoom 0.5
    with dissolve
    p "Então... de início vamos precisar de um bom networking e um software para facilitar a nossa gestão dos futuros talentos."

    hide KevinNormal
    hide ProtPensativo
    show ProtNormal at left:
        zoom 0.5
    with dissolve
    show KevinFalando at right:
        zoom 0.5
    k "Show! Eu fico responsável pelo networking e você responsável pela parte operacional. O que acha?"

    hide ProtNormal
    hide KevinFalando
    show KevinNormal at right:
        zoom 0.5
    show ProtFalando at left:
        zoom 0.5
    p "Ótimo!"

    hide KevinNormal
    hide ProtFalando
    show ProtNormal at left:
        zoom 0.5
    show KevinPensativo at right:
        zoom 0.5
    k "Nós precisamos pensar em um nome para empresa..."

    hide ProtNormal
    hide KevinPensativo
    show KevinNormal at right:
        zoom 0.5
    show ProtPensativo at left:
        zoom 0.5
    with dissolve
    p "Hmm.. É verdade."
    $ nomeEmpresa = renpy.input("Qual será o nome da sua agência de talentos?")

    hide ProtPensativo
    show ProtFalando at left:
        zoom 0.5
    p "Que tal %(nomeEmpresa)s?"

    hide KevinNormal
    hide ProtFalando
    show ProtNormal at left:
        zoom 0.5
    show KevinFalando at right:
        zoom 0.5
    k "Achei ótimo!"
    k "Então, pronto para iniciar o projeto?"

    hide ProtNormal
    hide KevinFalando
    show KevinNormal at right:
        zoom 0.5
    show ProtFalando at left:
        zoom 0.5
    p "Sim! Vamos lá."

    scene Office
    with dissolve
    "Inicialmente, a %(nomeEmpresa)s estará operando no modelo home office."

    show ProtEmpolgado at left:
        zoom 0.5
    with dissolve
    p "Eu preciso resolver essa questão da gestão dos nossos talentos logo..."
    p "Vou fazer algumas ligações para ver o que consigo."

    scene CafeBg
    with dissolve
    show ProtNormal at left:
        zoom 0.5
    with dissolve
    show DevNormal at right:
        zoom 0.5
    with dissolve
    "Após dois meses trabalhando no projeto, você finalmente encontra com o Developer que irá criar o software de gestão da %(nomeEmpresa)s."

    hide ProtNormal
    show ProtFalando at left:
        zoom 0.5
    p "Então daqui 2 meses ficará tudo pronto, né?"

    hide DevNormal
    hide ProtFalando
    show ProtNormal at left:
        zoom 0.5
    show DevSmile at right:
        zoom 0.5
    d "Sim, %(protagonista)s! Daqui a 2 meses você terá toda a gestão por meio do nosso software."
    show Contrato at truecenter:
        zoom 0.7
    with fade
    "Empolgado, você acaba assinando os contratos e a reunião é finalizada com ambos satisfeitos."
    jump capitulo2

    return

label capitulo2:

    scene UmAnoDepois
    with dissolve
    "..."

    scene office
    with dissolve
    "Após um ano de startup, lucros e problemas começam a surgir."
    "Um talento que você gerencia tem os dados vazados em um site de entretenimento."
    "Naturalmente, o talento irá questionar a sua empresa, visto que, os dados vazados denegriram a sua imagem, resultando em uma petição contra a sua empresa à ANPD."

    show ProtNormal at left:
        zoom 0.5
    show KevinInseguro at right:
        zoom 0.5
    k "%(protagonista)s! Você viu essa notificação aqui???"

    hide ProtNormal
    hide KevinInseguro
    show KevinInseguroQuieto at right:
        zoom 0.5
    show ProtFalando at left:
        zoom 0.5
    p "Chegou hoje cedo e não tive tempo de checar. O que é?"

    hide ProtFalando
    hide KevinInseguroQuieto
    show KevinBravo at right:
        zoom 0.5
    show ProtSurpreso at left:
        zoom 0.5
    k "É uma intimação contra nossa empresa!"
    k "Um de nossos talentos teve os seu dados vazados em um site de entretenimento."
    k "O que iremos fazer???"

    menu:
        "Relaxa! Isso é normal no nosso ramo. Deixa pra lá!":
            $ renpy.block_rollback()
            $ pontuacao -= 5
            hide ProtSurpreso
            hide KevinBravo
            show ProtComMedo at left:
                zoom 0.5
            with dissolve
            show KevinInseguro at right:
                zoom 0.5
            with dissolve
            k "Não acho que isso seja normal."
            k "Acho que deveríamos verificar o que aconteceu e solucionar com o responsável pelo tratamento de dados."
            
            hide ProtComMedo
            hide KevinInseguro
            show KevinInseguroQuieto at right:
                zoom 0.5
            show ProtSurpreso at left:
                zoom 0.5
            p "É verdade! Vamos fazer isso."
            
            jump PosDecisao1
        "É culpa do desenvolvedor! Não temos nada a ver com isso!":
            $ renpy.block_rollback()
            $ pontuacao -= 5
            hide ProtSurpreso
            hide KevinBravo
            show ProtComMedo at left:
                zoom 0.5
            with dissolve
            show KevinInseguro at right:
                zoom 0.5
            with dissolve
            k "Mesmo que seja erro do desenvolvedor, nós somos os responsáveis por esse talento."
            k "Fomos nós que fizemos o compromisso e assinamos o contrato com ela. Então, devemos resolver."
            k "Acho que deveríamos verificar o que aconteceu e solucionar com o responsável pelo tratamento de dados."
            
            hide ProtComMedo
            hide KevinInseguro
            show KevinInseguroQuieto at right:
                zoom 0.5
            show ProtSurpreso at left:
                zoom 0.5
            p "É verdade! Vamos fazer isso."

            jump PosDecisao1
        "Vamos verificar o que aconteceu e solucionar com o responsável pelo tratamento de dados.":
            $ renpy.block_rollback()
            $ pontuacao += 5
            
            jump PosDecisao1

    return

label PosDecisao1:

    
    scene office
    show KevinReceoso at right:
        zoom 0.5
    show ProtComMedo at left:
        zoom 0.5
    k "Sim! Essa é a decisão correta no momento."

    hide KevinReceoso
    hide ProtComMedo
    show ProtPensativo at left:
        zoom 0.5
    with dissolve
    p "Acho que antes da reunião eu deveria pesquisar um pouco mais sobre isso e saber quais as consequências."
    p "Eu tinha ouvido falar sobre uma nova lei LGPD, mas não dei muita bola pra isso..."

    scene PesquisaNoPC
    with dissolve

    p "Hmm... Vamos ver melhor sobre a lei LGPD."

    scene ComputadorZoom1
    with dissolve

    p "Então o tratamento de dados é permitido somente nesses casos..."

    scene ComputadorZoom2
    with dissolve

    p "Então a lei LGPD é válido nesses casos..."

    scene ComputadorZoom3
    with dissolve

    p "E esses são os dados sensíveis."

    scene ComputadorZoom4
    with dissolve

    p "Hmm.. Então essa é a diferença entre dados pessoais e não pessoais."

    scene ComputadorZoom5
    with dissolve

    p "Caramba! Então essa é a multa para empresas que infringirem a lei."
    p "Bom.. Melhor ir pra casa descansar e amanhã resolvemos isso com o Developer."

    scene UmDiaDepois
    with dissolve
    "..."

    scene office
    with dissolve
    show KevinInseguroQuieto at left:
        zoom 0.5
        xalign 0.3
    show ProtComMedo at left:
        zoom 0.5
        xalign 0.01
    show DevNormal at right:
        zoom 0.5
    "Finalmente você, Kevin e o desenvolvedor do seu software se encontram para discutir o ocorrido."

    hide ProtComMedo
    show ProtSurpreso at left:
        zoom 0.5
        xalign 0.01
    p "E então… nós estamos garantidos em relação a isso?"

    hide DevNormal
    hide ProtSurpreso
    show ProtComMedo at left:
        zoom 0.5
        xalign 0.01
    show DevFalando at right:
        zoom 0.5
    d "Não totalmente… nós fizemos apenas o que estava acordado no contrato!"

    hide DevFalando
    hide KevinInseguroQuieto
    show KevinReceoso at left:
        zoom 0.5
        xalign 0.3
    show DevNormal at right:
        zoom 0.5
    k "Você tem uma cópia do contrato em mãos? Nós queremos analisar."

    hide KevinReceoso
    hide DevNormal
    show KevinNormal at left:
        zoom 0.5
        xalign 0.3
    show DevSmile at right:
        zoom 0.5
    d "Claro! Eu tenho uma cópia aqui comigo."

    scene ComputadorZoom6
    with dissolve
    "..."

    k "E aí? Estamos garantidos? O contrato está de acordo com a lei?"

    menu:
        "Não! Precisamos nos readequar.":
            $ renpy.block_rollback()
            $ pontuacao += 5
            
            jump PosDecisao2
        "Sim! Está tudo certo de acordo com a lei LGPD.":
            $ renpy.block_rollback()
            $ pontuacao -= 5
            scene AssisBg
            with dissolve
            show AssisNormal at right:
                zoom 0.5
            with dissolve
            a "Opa! Não é bem assim..."
            a "O tratamento de dados só é permitido quando o usuário concorda explicitamente com isso e em outras ocasiões que vimos anteriormente."
            
            hide AssisNormal
            show AssisPensativo at right:
                zoom 0.5
            with dissolve
            a "Será que você realmente leu sobre a lei LGPD?"

            hide AssisPensativo
            show AssisNormal at right:
                zoom 0.5
            with dissolve
            a "Bom.. vamos voltar ao jogo!"

            scene ComputadorZoom6
            with dissolve

            k "Você tem certeza que está tudo certo?"
            p "Não… li novamente e identifiquei alguns erros. Precisamos nos readequar."

            jump PosDecisao2
    return

label PosDecisao2:
    
    scene office
    with dissolve
    show KevinPensativo at left:
        zoom 0.5
        xalign 0.3
    show ProtIndeciso at left:
        zoom 0.5
        xalign 0.01
    show DevNormal at right:
        zoom 0.5
    k "E aí, %(protagonista)s? O que devemos fazer?"

    menu:
        "Por enquanto, vamos deixar tudo assim mesmo. Estamos lucrando e isso foi apenas um imprevisto.":
            $ renpy.block_rollback()
            $ pontuacao -= 5
            scene AssisBg
            with dissolve
            show AssisNormal at right:
                zoom 0.5
            with dissolve
            a "Com certeza você não terá nenhum lucro se fizer isso."
            a "Você se lembra do valor da multa??"

            hide AssisNormal
            show AssisBravo at right:
                zoom 0.5
            with dissolve
            a "A sua empresa pode ser multada em 2 por cento do seu faturamento anual ou até o limite de R$ 50 milhões!"

            scene office
            with dissolve
            show KevinPensativo at left:
                zoom 0.5
                xalign 0.3
            show ProtIndeciso at left:
                zoom 0.5
                xalign 0.01
            show DevNormal at right:
                zoom 0.5
            k "%(protagonista)s, você não acha melhor solucionarmos isso agora e evitar futuros problemas?"

            hide ProtIndeciso
            hide KevinPensativo
            show KevinInseguroQuieto at left:
                zoom 0.5
                xalign 0.3
            show ProtFalando at left:
                zoom 0.5
                xalign 0.01
            p "Sim! Você está certo. Vamos solucionar isso o mais rápido possível."
            jump PosDecisao3
        "Vamos nos readequar totalmente de acordo com a nova lei LGPD, resolvendo isso e evitando futuros problemas.":
            $ renpy.block_rollback()
            $ pontuacao += 5
            jump PosDecisao3
    return


label PosDecisao3:
    
    scene UmDiaDepois
    with dissolve
    "..."
    "Na noite anterior, você e Kevin conversaram para achar uma resolução para o problema."

    scene office
    with dissolve
    hide ProtIndeciso
    hide KevinPensativo
    show KevinInseguroQuieto at left:
        zoom 0.5
        xalign 0.3
    show ProtFalando at left:
        zoom 0.5
        xalign 0.01
    show DevNormal at right:
        zoom 0.5
    k "Então... como iremos agir?"

    hide DevNormal
    hide KevinPensativo
    show KevinInseguroQuieto at left:
        zoom 0.5
        xalign 0.3
    show DevFalando at right:
        zoom 0.5
    d "O que vocês querem que eu altere ou implemente?"

    menu:
        "Na página de cadastro, deverá ser explícito sobre o uso dos dados coletados do talento.":
            $ renpy.block_rollback()
            $ pontuacao += 5
            scene AssisBg
            with dissolve
            show AssisNormal at right:
                zoom 0.5
            with dissolve
            a ""
            

        "Na página de cadastro, deverá ser implícito sobre o uso dos dados coletados do talento.":
            $ renpy.block_rollback()
            $ pontuacao -= 5
            jump PosDecisao4

    return

label PosDecisao4:
    "..."

    return



    

