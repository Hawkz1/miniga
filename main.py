import pygame 
import pygame_gui 

from Person import Person


pygame.init()

class Konstanter: 
    def __init__(self):
        self.WHITE = (255,255,255)
        self.GRAY = (128,128,128)
        self.DGRAY = (50,50,50)
        self.BLACK = (0,0,0)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)

        self.SCREENWIDTH = 1400
        self.SCREENHEIGHT = 600 

        self.TB_HEIGHT = 0.08*self.SCREENHEIGHT
        self.TB_NUM_WIDTH = 300
        self.TB_NAME_WIDTH = 400
        self.TB_VAL_WIDTH = 450

        self.PADDING = 0.1
        self.BG_COLOR = self.WHITE

        self.BORDER_WIDTH = 8
        self.font_size_labels = 25

        self.TB_SPACING = 2
        self.screen = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        self.manager = pygame_gui.UIManager((self.SCREENWIDTH, self.SCREENHEIGHT))
        Konstanter.TextBox_Dims(self)
        self.PERSONNUMMER_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect = self.tb_dims["PERSONNUMMER"], manager = self.manager, object_id = "PN_INPUT")
        self.NAMN_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect = self.tb_dims["NAMN"], manager = self.manager, object_id = "NAMN_INPUT")
        self.VAL_RIKS = pygame_gui.elements.UITextEntryLine(relative_rect = self.tb_dims["VAL0"], manager = self.manager, object_id = "VAL_RIKS")
        self.VAL_REGION = pygame_gui.elements.UITextEntryLine(relative_rect = self.tb_dims["VAL1"], manager = self.manager, object_id = "VAL_REGION")
        self.VAL_KOMMUN = pygame_gui.elements.UITextEntryLine(relative_rect = self.tb_dims["VAL2"], manager = self.manager, object_id = "VAL_KOMMUN")

        self.pn_label = '(bör införas id-scanning) PERSONNUMMER (ÅÅÅÅMMDD-####):'
        self.namn_label = 'NAMN (FÖRNAMN EFTERNAMN):'
        self.val_labels = ['PARTIVAL [RIKSDAG]:', 'PARTIVAL [REGION]:', 'PARTIVAL [KOMMUN]:']

    @staticmethod
    def TextBox_Dims(self):
        tb_dims = dict(); mid_width = self.SCREENWIDTH // 2; tb_dims["VAL"] = []

        initial_top = int((self.PADDING)*self.SCREENHEIGHT)
        PN_DIMS = (mid_width - self.TB_NUM_WIDTH//2, initial_top, self.TB_NUM_WIDTH, self.TB_HEIGHT)
        NAMN_DIMS = (mid_width - self.TB_NAME_WIDTH//2, initial_top + int(self.TB_SPACING*self.TB_HEIGHT), self.TB_NAME_WIDTH, self.TB_HEIGHT)

        tb_dims["PERSONNUMMER"] = pygame.rect.Rect(*PN_DIMS)
        tb_dims["NAMN"] =  pygame.rect.Rect(*NAMN_DIMS)
        for i in range(2,5):
            tb_dims["VAL" + str(i-2)] = pygame.rect.Rect(*(mid_width - self.TB_VAL_WIDTH//2, initial_top + int(i*self.TB_SPACING*self.TB_HEIGHT), self.TB_VAL_WIDTH, self.TB_HEIGHT))

        self.initial_top = initial_top 
        self.tb_dims = tb_dims


    @staticmethod
    def get_labels(self):
        ret = dict(); tb_dims = self.tb_dims

        font = pygame.font.SysFont(None, self.font_size_labels)
        PN_TEXT = font.render(self.pn_label, True, self.BLACK)
        PN_y = int(tb_dims["PERSONNUMMER"][1] + 1/2*tb_dims["PERSONNUMMER"][3] - 1/2 * font.size(self.pn_label)[1])
        PN_x = tb_dims["PERSONNUMMER"][0] - font.size(self.pn_label)[0] - 20 
        ret["PN"] = [PN_TEXT,PN_x,PN_y]

        NAMN_TEXT = font.render(self.namn_label, True, self.BLACK)
        NAMN_y = int(tb_dims["NAMN"][1] + 1/2*tb_dims["NAMN"][3] - 1/2 * font.size(self.namn_label)[1])
        NAMN_x = tb_dims["NAMN"][0] - font.size(self.namn_label)[0] - 20
        ret["NAMN"] = [NAMN_TEXT,NAMN_x,NAMN_y]

        for i in range(3):
            VAL_TEXT = font.render(self.val_labels[i], True, self.BLACK)
            VAL_y = int(tb_dims["VAL" + str(i)][1] + 1/2*tb_dims["VAL"+ str(i)][3] - 1/2 * font.size(self.val_labels[i])[1])
            VAL_x = tb_dims["VAL"+ str(i)][0] - font.size(self.val_labels[i])[0] - 20
            ret["VAL" + str(i)] = [VAL_TEXT,VAL_x,VAL_y]

        return ret


        

    
class Val:
    def __init__(self):
        pygame.display.set_caption("Digitalt Val Prototyp")
        Konstanter.__init__(self)
        labels = Konstanter.get_labels(self)
        self.clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, self.font_size_labels)
        tb_dims = self.tb_dims

        pygame.display.update()
        while True: 
            self.clock.tick(60)
            self.time_delta = self.clock.tick(60)/900.


            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                self.manager.process_events(event)
            self.screen.fill("white")
            for value in labels.values():
                self.screen.blit(value[0],(value[1],value[2]))


            self.manager.update(self.time_delta)
            self.manager.draw_ui(self.screen)
            self.manager.update(self.time_delta)
            pygame.display.update()
            
            
    def draw_tb_borders(self):
        return False

if __name__ == "__main__":
    Val()
