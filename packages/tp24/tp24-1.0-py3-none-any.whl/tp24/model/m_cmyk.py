import tp24.model.colour as colour
import tp24.model.m_rgb as col_rgb
import tp24.model.m_cmy as col_cmy
import tp24.errors as errors

class cmyk(colour.Colour):
    RANGE = (100, 100, 100, 100)
    c = None
    m = None
    y = None
    k = None

    def __init__(self, vc: int, vm: int, vy: int, vk: int):
        if not 0 <= vc <= self.RANGE[0]:
            raise errors.RangeError(f"Value of C channel is {vc} but is not in range of 0 <= C <= 100")
        elif not 0 <= vm <= self.RANGE[1]:
            raise errors.RangeError(f"Value of M channel is {vm} but is not in range of 0 <= m <= 100")
        elif not 0 <= vy <= self.RANGE[2]:
            raise errors.RangeError(f"Value of Y channel is {vy} but is not in range of 0 <= y <= 100")
        elif not 0 <= vk <= self.RANGE[3]:
            raise errors.RangeError(f"Value of K channel is {vk} but is not in range of 0 <= k <= 100")
        self.c = vc
        self.m = vm
        self.y = vy
        self.k = vk
    
    def __iter__(self):
        t = (self.c, self.m, self.y, self.k)
        for i in t:
            yield i

    def rgb(self):
        c = self.c/self.RANGE[0]
        m = self.m/self.RANGE[1]
        y = self.y/self.RANGE[2]
        k = self.k/self.RANGE[3]

        r = 255 * (1-c) * (1-k)
        g = 255 * (1-m) * (1-k)
        b = 255 * (1-y) * (1-k)

        r = round(r)
        g = round(g)
        b = round(b)

        if issubclass(type(self), colour.ColourAlpha):
            return col_rgb.rgba(r, g, b, self.a)
        else:
            return col_rgb.rgb(r, g, b)

    def hsl(self):
        return self.rgb().hsl()

    def hsv(self):
        return self.rgb().hsv()

    def cmy(self):
        if self.k == 0:
            c = self.c
            m = self.m
            y = self.y
        else:
            c = self.c/self.k
            m = self.m/self.k
            y = self.y+self.k

        c *= 100/255
        m *= 100/255
        y *= 100/255

        if issubclass(type(self), colour.ColourAlpha):
            return col_cmy.cmya(c, m, y, self.a)
        else:
            return col_cmy.cmy(c, m, y)

class cmyka(cmyk, colour.ColourAlpha):
    def __init__(self, *v):
        cmyk.__init__(self, *v[:-1])
        colour.ColourAlpha.__init__(self, v[-1])

    def __iter__(self):
        t = (self.c, self.m, self.y, self.k, self.a)
        for i in t:
            yield i