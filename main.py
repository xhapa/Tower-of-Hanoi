import pygame
from tower import Tower

pygame.font.init()
pygame.display.set_caption('Tower of Hanoi')
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE_FONT = pygame.font.SysFont('Future TimeSplitters', 40, bold=True, italic=False)
BUTTON_FONT = pygame.font.SysFont('Future TimeSplitters', 20, bold=True, italic=False)
FPS=60

def draw_screen(tower, reset_button):
    SCREEN.fill(('#98C1D9'))
    pygame.draw.rect(SCREEN, ('#FAF0CA'), reset_button, border_radius=10)
    SCREEN.blit(BUTTON_FONT.render('Reset', 1, (0,0,0)), (110,460))
    SCREEN.blit(TITLE_FONT.render('Tower Of Hanoi', 1, (0,0,0)), (280,25))
    tower.draw_tower(SCREEN)
    pygame.display.update()

def main():

    pygame.init()
    running = True
    clock=pygame.time.Clock()
    tower=Tower()
    reset_button = pygame.Rect(95, 450, 70, 40)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            mouse_presses = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION) and mouse_presses[0]:
                tower.select_disks(event, mouse_pos)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if tower.A[0]==[] and tower.C[0]==[]:
                    tower.solve(8, tower.B, tower.A, tower.C, SCREEN)
                elif tower.A[0]==[] and tower.B[0]==[]:
                    tower.solve(8, tower.C, tower.B, tower.A, SCREEN)
                elif tower.C[0]==[] and tower.B[0]==[]:
                    tower.solve(8, tower.A, tower.C, tower.B, SCREEN)
            if event.type == pygame.MOUSEBUTTONDOWN and reset_button.collidepoint(mouse_pos):
                tower.reset()


        draw_screen(tower, reset_button)
    main()    

if __name__ == '__main__':
    main()