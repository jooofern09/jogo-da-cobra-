import pygame
import random

pygame.init()

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# definição da tela
largura_tela = 700
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("jogo da cobrinha")

# conf da cobrinha
tamanho_celula = 10
velocidade = 12
clock = pygame.time.Clock()

# fontes para mensagem e pontuação
fonte = pygame.font.SysFont("bahnschrift", 25)

# função para mostrar a pontuação
def pontuacao(score):
    valor = fonte.render("Pontuação: " + str(score), True, branco)
    tela.blit(valor, [0, 0])

# função de desenhar a cobra
def cobra(tamanho_celula, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_celula, tamanho_celula])

# função principal do jogo
def jogo():
    # posições da cobra
    x_cobra = largura_tela / 2
    y_cobra = altura_tela / 2

    # movimentos iniciais
    x_mudanca = 0
    y_mudanca = 0

    # corpo da cobrinha
    lista_cobra = []
    comprimento_cobra = 1

    # posição inicial da comida
    x_comida = round(random.randrange(0, largura_tela - tamanho_celula) / 10.0) * 10.0
    y_comida = round(random.randrange(0, altura_tela - tamanho_celula) / 10.0) * 10.0

    # variável de controle de loop
    fim_jogo = False
    perdeu = False

    while not fim_jogo:
        while perdeu:
            tela.fill(azul)
            mensagem = fonte.render("Você perdeu! Aperte Q para sair, ou C para continuar!", True, vermelho)
            tela.blit(mensagem, [largura_tela / 8, altura_tela / 3])
            pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                    perdeu = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        perdeu = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_celula
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_celula
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    x_mudanca = 0
                    y_mudanca = -tamanho_celula
                elif evento.key == pygame.K_DOWN:
                    x_mudanca = 0
                    y_mudanca = tamanho_celula
        
        # posição da cobra
        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            perdeu = True

        x_cobra += x_mudanca
        y_cobra += y_mudanca

        # preencher tela de fundo
        tela.fill(preto)

        # desenho da comida
        pygame.draw.rect(tela, vermelho, [x_comida, y_comida, tamanho_celula, tamanho_celula])

        # atualizar o corpo da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x_cobra)
        cabeca_cobra.append(y_cobra)
        lista_cobra.append(cabeca_cobra)

        # remove a cauda da cobra
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # verificar se cobra colidiu com ela mesma
        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                perdeu = True

        # desenha a cobra e a pontuação
        cobra(tamanho_celula, lista_cobra)
        pontuacao(comprimento_cobra - 1)

        # atualizar a tela
        pygame.display.update()

        # cobra come a comida
        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura_tela - tamanho_celula) / 10.0) * 10.0
            y_comida = round(random.randrange(0, altura_tela - tamanho_celula) / 10.0) * 10.0
            comprimento_cobra += 1

        # controla a velocidade do jogo
        clock.tick(velocidade)

    # sai do jogo 
    pygame.quit()
    quit()

# INICIAR O JOGO
jogo()
