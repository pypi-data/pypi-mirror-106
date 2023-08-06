import tp24.model.colour as colour
import tp24.model.m_rgb as col_rgb
import tp24.model.m_cmyk as col_cmyk
import tp24.errors as errors

class cmy(colour.Colour):
    RANGE = (255, 255, 255)
    c = None
    m = None
    y = None

    def __init__(self, vc: int, vm: int, vy: int):
        if not 0 <= vc <= self.RANGE[0]:
            raise errors.RangeError(f"Value of C channel is {vc} but is not in range of 0 <= c <= 255")
        elif not 0 <= vm <= self.RANGE[1]:
            raise errors.RangeError(f"Value of M channel is {vm} but is not in range of 0 <= m <= 255")
        elif not 0 <= vy <= self.RANGE[2]:
            raise errors.RangeError(f"Value of Y channel is {vy} but is not in range of 0 <= y <= 255")
        self.c = vc
        self.m = vm
        self.y = vy
    
    def __iter__(self):
        t = (self.c, self.m, self.y)
        for i in t:
            yield i

    def hsv(self):
        return self.rgb().hsv()

    def hsl(self):
        return self.rgb().hsl()

    def cmyk(self):
        c = self.c/255
        m = self.m/255
        y = self.y/255

        k = min(c, m, y)
        c *= k
        m *= k
        y -= k

        c *= 100
        m *= 100
        y *= 100

        if issubclass(type(self), colour.ColourAlpha):
            return col_cmyk.cmyka(c, m, y, k, self.a)
        else:
            return col_cmyk.cmyk(c, m, y, k)

    def rgb(self):
        r = 255 - self.c
        g = 255 - self.m
        b = 255 - self.y

        if issubclass(type(self), colour.ColourAlpha):
            return col_rgb.rgba(r, g, b, self.a)
        else:
            return col_rgb.rgb(r, g, b)

class cmya(cmy, colour.ColourAlpha):
    def __init__(self, *v):
        cmy.__init__(self, *v[:-1])
        colour.ColourAlpha.__init__(self, v[-1])

    def __iter__(self):
        t = (self.c, self.m, self.y, self.a)
        for i in t:
            yield i