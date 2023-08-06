import tp24.model.colour as colour
import tp24.errors as errors
import tp24.model.m_rgb as col_rgb
import tp24.model.m_hsv as col_hsv

class hsl(colour.Colour):
    RANGE = (360, 100, 100)
    h = None
    s = None
    l = None

    def __init__(self, vh: int, vs: int, vl: int):
        if not 0 <= vh <= self.RANGE[0]:
            raise errors.RangeError(f"Value of H channel is {vh} but is not in range of 0 <= h <= 360")
        elif not 0 <= vs <= self.RANGE[1]:
            raise errors.RangeError(f"Value of S channel is {vs} but is not in range of 0 <= s <= 100")
        elif not 0 <= vl <= self.RANGE[2]:
            raise errors.RangeError(f"Value of L channel is {vl} but is not in range of 0 <= l <= 100")
        self.h = vh
        self.s = vs
        self.l = vl
    
    def __iter__(self):
        t = (self.h, self.s, self.l)
        for i in t:
            yield i

    def rgb(self):
        h = self.h if self.h != self.RANGE[0] else 0
        s = self.s/self.RANGE[1]
        l = self.l/self.RANGE[2]
        c = (1 - abs(2*l-1)) * s
        x = c * (1 - abs((h/60)%2 - 1))
        m = l - c/2

        if 0 <= h < 60:      r, g, b = c, x, 0
        elif 60 <= h < 120:  r, g, b = x, c, 0
        elif 120 <= h < 180: r, g, b = 0, c, x
        elif 180 <= h < 240: r, g, b = 0, x, c
        elif 240 <= h < 300: r, g, b = x, 0, c
        elif 300 <= h < 360: r, g, b = c, 0, x
        r = round((r+m)*255)
        g = round((g+m)*255)
        b = round((b+m)*255)

        if issubclass(type(self), colour.ColourAlpha):
            return col_rgb.rgba(r, g, b, self.a)
        else:
            return col_rgb.rgb(r, g, b)

    def hsv(self):
        h = self.h
        s = self.s/self.RANGE[1]
        l = self.l/self.RANGE[2]

        v = l + s*min(l, 1-l)
        if v == 0: s == 0
        else: s == 2-(2*l)/v

        s = round(s*self.RANGE[1])
        v = round(v*self.RANGE[2])

        if issubclass(type(self), colour.ColourAlpha):
            return col_hsv.hsva(h, s, v, self.a)
        else:
            return col_hsv.hsv(h, s, v)

    def cmyk(self):
        return self.rgb().cmyk()

    def cmy(self):
        return self.rgb().cmy()

class hsla(hsl, colour.ColourAlpha):
    def __init__(self, *v):
        hsl.__init__(self, *v[:-1])
        colour.ColourAlpha.__init__(self, v[-1])

    def __iter__(self):
        t = (self.h, self.s, self.l, self.a)
        for i in t:
            yield i