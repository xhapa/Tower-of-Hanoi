import pygame

class Disk:
    def __init__(self, n, x_pos, y_pos):
        self.__value = n
        self.rect= pygame.Rect(x_pos, y_pos, 25+(20*(self.__value-1)), 20)

    def move_disk(self, event_pos):
        self.rect.x = event_pos[0] - self.rect.w/2
        self.rect.y = event_pos[1] - self.rect.h/2
    
    @property
    def get_value(self):
        return self.__value

    @get_value.setter
    def set_value(self, new_value):
        self.__value = new_value
class Tower:
    def __init__(self):
        self.N=8
        self.colors = ['#2D4739', '#09814A', '#9FD356', '#F4E04D', '#F6AE2D', '#FE5F55', '#E63462', '#726DA8']
        self.A=([], pygame.Rect(160, 180, 10, 200))
        self.B=([], pygame.Rect(400, 180, 10, 200))
        self.C=([], pygame.Rect(640, 180, 10, 200))
    
        for i in range(self.N, 0,-1):
            self.A[0].append(Disk(i, 160-(10*i), 200+(20*i)))

    def draw_tower(self, screen):
        pygame.draw.rect(screen, ('#5A350E'), pygame.Rect(50, 380, 700, 20))
        pygame.draw.rect(screen, ('#5A350E'), self.A[1])
        pygame.draw.rect(screen, ('#5A350E'), self.B[1])
        pygame.draw.rect(screen, ('#5A350E'), self.C[1])
        self.draw_disks(screen)
        pygame.display.update()

    def draw_disks(self, screen):
        for i in range(len(self.A[0])):
            pygame.draw.rect(screen, (self.colors[i]), self.A[0][i].rect)
        for i in range(len(self.B[0])):
            pygame.draw.rect(screen, (self.colors[i]), self.B[0][i].rect)
        for i in range(len(self.C[0])):
            pygame.draw.rect(screen, (self.colors[i]), self.C[0][i].rect)

    def move_disks(self, event, event_pos, origin, destiny1, destiny2):
        for disk in origin[0]:
            if disk.rect.collidepoint(event_pos):
               disk.move_disk(event_pos)
            if disk.rect.colliderect(destiny1[1]):
                origin[0].pop(origin[0].index(disk))
                self.append_disk(destiny1[0], disk, destiny1[1].x)
            if disk.rect.colliderect(destiny2[1]):
                origin[0].pop(origin[0].index(disk))
                self.append_disk(destiny2[0], disk, destiny2[1].x)

    def select_disks(self, event, event_pos):
        self.move_disks(event, event_pos, self.A, self.B, self.C)
        self.move_disks(event, event_pos, self.B, self.A, self.C)
        self.move_disks(event, event_pos, self.C, self.A, self.B)

    def append_disk(self, tower, disk, limit, screen=0, algorithm=False):
        tower.append(disk)
        index = tower.index(disk)
        disk.rect.x = limit-(10*disk.get_value)+5
        disk.rect.y = 360 - 20*index 
        if algorithm:
            self.draw_tower(screen)
        #self.__repr__()

    def solve(self, n, origin, destiny, aux, screen):
        if n>0 and origin[0]!=[]:
            self.solve(n-1, origin, aux, destiny, screen)
            disk = origin[0].pop()
            self.append_disk(destiny[0], disk, destiny[1].x, screen, True)
            self.solve(n-1, aux, destiny, origin, screen)
    
    def reset(self):
        self.A[0].clear()
        self.B[0].clear()
        self.C[0].clear()

        for i in range(self.N, 0,-1):
            self.A[0].append(Disk(i, 160-(10*i), 200+(20*i)))

    def __repr__(self):
        print('\nA', end='->')
        for disk in self.A[0]:
            print(disk.get_value, end=' ')
        print('\nB', end='->')
        for disk in self.B[0]:
            print(disk.get_value, end=' ')
        print('\nC', end='->')
        for disk in self.C[0]:
            print(disk.get_value, end=' ')
        print('\n')