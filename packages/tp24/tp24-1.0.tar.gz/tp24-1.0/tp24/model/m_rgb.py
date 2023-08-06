import tp24.model.colour as colour
import tp24.model.m_cmyk as col_cmyk
import tp24.model.m_cmy as col_cmy
import tp24.model.m_hsv as col_hsv
import tp24.model.m_hsl as col_hsl
import tp24.errors as errors

class rgb(colour.Colour):
    RANGE = (255, 255, 255)
    r = None
    g = None
    b = None

    def __init__(self, vr: int, vg: int, vb: int):
        if not 0 <= vr <= self.RANGE[0]:
            raise errors.RangeError(f"Value of R channel is {vr} but is not in range of 0 <= r <= 255")
        elif not 0 <= vg <= self.RANGE[1]:
            raise errors.RangeError(f"Value of G channel is {vg} but is not in range of 0 <= g <= 255")
        elif not 0 <= vb <= self.RANGE[2]:
            raise errors.RangeError(f"Value of b channel is {vb} but is not in range of 0 <= b <= 255")
        self.r = vr
        self.g = vg
        self.b = vb
    
    def __iter__(self):
        t = (self.r, self.g, self.b)
        for i in t:
            yield i

    def hsv(self):
        r = self.r/self.RANGE[0]
        g = self.g/self.RANGE[1]
        b = self.b/self.RANGE[2]
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        d = cmax-cmin

        if d == 0: h = 0
        elif cmax == r: h = 60 * (((g-b)/d)%6)
        elif cmax == g: h = 60 * (((b-r)/d)+2)
        elif cmax == b: h = 60 * (((r-g)/d)+4)

        if cmax == 0: s = 0
        else: s = d / cmax

        v = cmax

        h = round(h)
        s = round(s*100)
        v = round(v*100)
        
        if issubclass(type(self), colour.ColourAlpha):
            return col_hsv.hsva(h, s, v, self.a)
        else:
            return col_hsv.hsv(h, s, v)

    def hsl(self):
        r = self.r/self.RANGE[0]
        g = self.g/self.RANGE[1]
        b = self.b/self.RANGE[2]
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        d = cmax-cmin

        if d == 0: h = 0
        elif cmax == r: h = 60 * (((g-b)/d)%6)
        elif cmax == g: h = 60 * (((b-r)/d)+2)
        elif cmax == b: h = 60 * (((r-g)/d)+4)
        
        l = (cmax+cmin)/2
        
        if d == 0: s = 0
        else: s = d / (1-abs(2*l-1))
        
        h = round(h)
        s = round(s*100)
        l = round(l*100)
        
        if issubclass(type(self), colour.ColourAlpha):
            return col_hsl.hsla(h, s, l, self.a)
        else:
            return col_hsl.hsl(h, s, l)


    def cmyk(self):
        r = self.r/self.RANGE[0]
        g = self.g/self.RANGE[1]
        b = self.b/self.RANGE[2]
        
        k = 1-max(r, g, b)

        if k==1:
            c = 0
            m = 0
            y = 0
        else:
            c = (1-r-k)/(1-k)
            m = (1-g-k)/(1-k)
            y = (1-b-k)/(1-k)

        c = round(c*100)
        m = round(m*100)
        y = round(y*100)
        k = round(k*100)

        if issubclass(type(self), colour.ColourAlpha):
            return col_cmyk.cmyka(c, m, y, k, self.a)
        else:
            return col_cmyk.cmyk(c, m, y, k)

    def cmy(self):
        c = 255 - self.r
        m = 255 - self.g
        y = 255 - self.b

        if issubclass(type(self), colour.ColourAlpha):
            return col_cmy.cmya(c, m, y, self.a)
        else:
            return col_cmy.cmy(c, m, y)


class rgba(rgb, colour.ColourAlpha):
    def __init__(self, *v):
        rgb.__init__(self, *v[:-1])
        colour.ColourAlpha.__init__(self, v[-1])

    def __iter__(self):
        t = (self.r, self.g, self.b, self.a)
        for i in t:
            yield i