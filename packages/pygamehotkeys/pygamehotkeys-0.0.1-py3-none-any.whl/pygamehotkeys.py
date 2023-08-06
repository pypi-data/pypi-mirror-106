import pygame, sys

class SelfDeletingItem:
    def __init__(self, value, time):
        self.value = value
        self.time = time
    def tick(self):
        self.time = max(self.time-1, 0)
    def __repr__(self):
        return f'({self.time}){self.value}'

class SelfDeletingList:
    def __init__(self):
        self.items = []
    def append(self, item):
        self.items.append(SelfDeletingItem(item, 120))
    def __repr__(self):
        return self.items.__repr__()
    def tick(self):
        to_delete = []
        for item in self.items:
            item.tick()
            if item.time < 1:
                to_delete.append(item)
        for item in to_delete:
            self.items.remove(item)
    def join(self):
        return ''.join([key.value for key in self.items])
    def reset(self):
        self.items = []
    def __eq__(self, other):
        if [item.value for item in self.items] == other:
            return True
        else:
            return False

class HotkeyManager:

    def __init__(self, hotkey):

        self.hotkey = pygame.key.key_code(hotkey)
        self.pressed = 0
        self.keys = SelfDeletingList()
        self.hotkeys = []
        self.active = []

    def tick(self):

        self.pressed -= 1
        self.keys.tick()
        self.active = []

    def feed_event(self, event):

        if event.key == self.hotkey:
            self.pressed = 50

        elif self.pressed > 0:
            self.keys.append(pygame.key.name(event.key))
            self.pressed = 30

    def add_hotkey(self, hk):
        self.hotkeys.append([char for char in hk])

    def match_hotkeys(self):

        if -50 < self.pressed < 0:
            #if self.keys == ['w']:
            #    print('QWERTY')

            for hk in self.hotkeys:
                #print(hk)
                #print(self.keys)
                if self.keys == hk:
                    self.active.append(hk)

            self.keys.reset()

    def used(self, hk):
        splt = [char for char in hk]
        return splt in self.active

    def draw_widget(self, screen, font, font2, height):
        bg = pygame.Surface(font.size(self.keys.join()))
        bg.set_alpha(128)
        bg.fill((0, 0, 0))
        screen.blit(bg, (0, height-15))

        textsurface = font.render(self.keys.join(), False, (0, 0, 0))
        textsurface2 = font2.render('Keys pressed:', False, (0, 0, 0))
        screen.blit(textsurface, (0, height-15))
        if self.keys.join() != '':
            screen.blit(textsurface2, (3, height-26))
