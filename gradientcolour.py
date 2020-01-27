import pygame as pg
import sys

class Colours:
    def __init__(self, size = (740, 480), start=(45,195,155, 255), end = (20,245,155,25)):
        self.start = start
        self.end = end
        pg.init()
        pg.key.set_repeat(50)
        self.clock = pg.time.Clock()
        self.size = size
        self.screen = pg.display.set_mode(self.size)
        self.rise = 1
        self.cycle = 0

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.y_gradient(), (0,0))
        pg.display.flip()

    def mainloop(self):
        while True:
            self.clock.tick(60)
            self.draw()
            self.events()
            self.sunrise()

    def y_gradient(self):
        gradsurf = pg.Surface((1,self.size[1])).convert_alpha()
        slopes =[(self.start[n], (self.end[n] - self.start[n])*(1.0/self.size[1])) for n in range(4)]
        for y in range(self.size[1]):
            gradsurf.set_at((0,y), tuple([int(slopes[n][0]+slopes[n][1]*y) for n in range(4)]))
        return pg.transform.scale(gradsurf, self.size)

    def minmaxcolour(self, rgba):
        r,g,b,a = rgba
        r = min(255, max(0,r))
        g = min(255, max(0,g))
        b = min(255, max(0,b))
        a = min(255, max(0,a))
        return r,g,b,a

    def sunrise(self):
        if self.cycle:
            e = 3 if self.rise else -1
            s = 1 if self.rise else -3
            if self.start[3] >= 255 and 255 <= self.end[3]:
                self.rise = 0
            elif self.start[3] <= 0 and 0 >= self.end[3]:
                self.rise = 1
            self.start, self.end = self.minmaxcolour((*self.start[:3], self.start[3]+s)), self.minmaxcolour((*self.end[:3], self.end[3]+e))


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_z: 
                    self.cycle = False if self.cycle else True
                    if self.cycle:
                        print('Rise and shine!')
                        self.start = (245,135,255,0)#(245,155,255,0)
                        self.end = (255,145,155,0)#(255,255,125,0)
                    return
                sr,sg,sb,st = self.start
                er,eg,eb,et = self.end
                startdict = {pg.K_q:(sr+10, sg,sb,st),
                         pg.K_a:(sr-10, sg,sb,st),
                         pg.K_w:(sr, sg+10, sb,st),
                         pg.K_s:(sr, sg-10, sb,st),
                         pg.K_e:(sr,sg, sb+10,st),
                         pg.K_d:(sr, sg, sb-10,st),
                         pg.K_r:(sr,sg,sb,st+10),
                         pg.K_f:(sr,sg,sb,st-10)}
                enddict = {
                         pg.K_y:(er+10,eg,eb,et), 
                         pg.K_h:(er-10,eg,eb,et), 
                         pg.K_u:(er,eg+10,eb,et), 
                         pg.K_j:(er,eg-10,eb,et), 
                         pg.K_i:(er,eg,eb+10,et), 
                         pg.K_k:(er,eg, eb-10,et),
                         pg.K_l:(er,eg,eb,et-10),
                         pg.K_o:(er,eg,eb,et+10)}

                if event.key in startdict.keys():
                    self.start = self.minmaxcolour(startdict[event.key])
                    print(self.start)
                elif event.key in enddict.keys():
                    self.end = self.minmaxcolour(enddict[event.key])
                    print(self.end)




if __name__ == '__main__':
    colour = Colours()
    colour.mainloop()
