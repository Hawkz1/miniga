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

        self.SCREENWIDTH = 1200
        self.SCREENHEIGHT = 800 

        self.TB_HEIGHT = 200
        self.TB_NUM_WIDTH = 300
        self.TB_NAME_WIDTH = 600 

        self.PADDING = 0.1
        self.BG_COLOR = self.DGRAY

        self.BORDER_WIDTH = 50

class TextBox(Konstanter):
    def get_tb_dims(self):
        tb_dims = dict()

        mid_width = self.SCREENWIDTH // 2
        initial_top = (1-self.PADDING)*self.SCREENWIDTH 
        PN_DIMS_OUTER = (mid_width-self.TB_NUM_WIDTH//2, initial_top, self.TB_NUM_WIDTH, self.TB_HEIGHT)
        NAMN_DIMS_OUTER = (mid_width - self.TB_NAME_WIDTH//2, initial_top - 3*self.TB_HEIGHT, self.TB_NAME_WIDTH, self.TB_HEIGHT)
        PN_DIMS_INNER = tuple([x - self.BORDER_WIDTH for x in PN_DIMS_OUTER])
        NAMN_DIMS_INNER = tuple([x - self.BORDER_WIDTH for x in NAMN_DIMS_OUTER])     

        tb_dims["PERSONNUMER"] = pygame.rect.Rect(*PN_DIMS_OUTER), pygame.rect.Rect(*PN_DIMS_INNER)
        tb_dims["NAMN"] =  pygame.rect.Rect(*NAMN_DIMS_OUTER), pygame.rect.Rect(*NAMN_DIMS_INNER)


        self.tb_dims = tb_dims
    
    @staticmethod
    def draw_borders(self):
        pygame.Rectr


    
class Val:
    def __init__(self):
        pygame.display.set_caption("Digitalt Val")
        Konstanter.__init__(self)
        screen = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        pygame.display.flip()
        clock = pygame.time.Clock()
        
        tb_dims = TextBox.get_tb_dims(self)

        while True: 
            screen.fill(self.BG_COLOR)

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()
            clock.tick(30)

    def draw_tb_borders(self):
        return False

if __name__ == "__main__":
    Val()
