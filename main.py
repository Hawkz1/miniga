import pygame 

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
        self.TB_NAME_WIDTH = 600 

        self.PADDING = 0.1
        self.BG_COLOR = self.DGRAY

        self.BORDER_WIDTH = 8
        self.font_size_labels = 25

        self.TB_SPACING = 2
        self.screen = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        Konstanter.TextBox_Dims(self)

        self.pn_label = 'SCANNA ID-HANDLING FÖR PERSONNUMMER (12 SIFFROR):'
        self.val_label = ''
    @staticmethod
    def TextBox_Dims(self):
        tb_dims = dict()
        mid_width = self.SCREENWIDTH // 2
        br = self.BORDER_WIDTH

        initial_top = int((self.PADDING)*self.SCREENHEIGHT)
        PN_DIMS_OUTER = (mid_width - self.TB_NUM_WIDTH//2, initial_top, self.TB_NUM_WIDTH, self.TB_HEIGHT)
        NAMN_DIMS_OUTER = (mid_width - self.TB_NAME_WIDTH//2, initial_top + int(self.TB_SPACING*self.TB_HEIGHT), self.TB_NAME_WIDTH, self.TB_HEIGHT)
        PN_DIMS_INNER = (mid_width - self.TB_NUM_WIDTH//2 + br, initial_top + br, self.TB_NUM_WIDTH - 2*br, self.TB_HEIGHT - 2*br)
        NAMN_DIMS_INNER = (mid_width - self.TB_NAME_WIDTH//2 + br, initial_top + int(self.TB_SPACING*self.TB_HEIGHT) + br, self.TB_NAME_WIDTH - 2*br, self.TB_HEIGHT - 2*br)

        tb_dims["PERSONNUMMER"] = pygame.rect.Rect(*PN_DIMS_OUTER), pygame.rect.Rect(*PN_DIMS_INNER)
        tb_dims["NAMN"] =  pygame.rect.Rect(*NAMN_DIMS_OUTER), pygame.rect.Rect(*NAMN_DIMS_INNER)

        self.initial_top = initial_top 

        self.tb_dims = tb_dims

class TextBox(Konstanter): 
    @staticmethod
    def draw_borders(self, tb_dims):
        Konstanter.__init__(self)

        # borders personnummer
        self.screen.fill(self.BG_COLOR)
        pygame.draw.rect(self.screen, self.BLACK, tb_dims["PERSONNUMMER"][0])
        pygame.draw.rect(self.screen, self.GRAY, tb_dims["PERSONNUMMER"][1])
        #borders namn 
        pygame.draw.rect(self.screen, self.BLACK, tb_dims["NAMN"][0])
        pygame.draw.rect(self.screen, self.WHITE, tb_dims["NAMN"][1])
        TextBox.draw_labels(self, tb_dims)
    @staticmethod
    def draw_labels(self, tb_dims):
        font = pygame.font.SysFont(None, self.font_size_labels)
        pn_label = 'SCANNA ID-HANDLING FÖR PERSONNUMMER (12 SIFFROR):'
        PN_TEXT = font.render(pn_label, True, self.WHITE)
        PN_y = int(tb_dims["PERSONNUMMER"][0][1] + 1/2*tb_dims["PERSONNUMMER"][0][3] - 1/2 * font.size(pn_label)[1])
        PN_x = tb_dims["PERSONNUMMER"][0][0] - font.size(pn_label)[0] - 20 
        self.screen.blit(PN_TEXT,(PN_x,PN_y))
        
        val_label = 'PARTIVAL:'
        NAMN_TEXT = font.render(val_label, True, self.WHITE)
        NAMN_y = int(tb_dims["NAMN"][0][1] + 1/2*tb_dims["NAMN"][0][3] - 1/2 * font.size(val_label)[1])
        print(int(1/2*(tb_dims["NAMN"][0][1] + tb_dims["NAMN"][0][3]) + 1) )
        NAMN_x = tb_dims["NAMN"][0][0] - font.size(val_label)[0] - 20
        self.screen.blit(NAMN_TEXT, (NAMN_x, NAMN_y))

    
class Val:
    def __init__(self):
        pygame.display.set_caption("Digitalt Val")
        Konstanter.__init__(self)
        pygame.display.flip()
        clock = pygame.time.Clock()
        print(self.tb_dims)
        screen = self.screen
        while True: 
            screen.fill(self.BG_COLOR)

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            
            TextBox.draw_borders(self, self.tb_dims)
            
            pygame.display.flip()
            clock.tick(30)
            
    def draw_tb_borders(self):
        return False

if __name__ == "__main__":
    Val()
