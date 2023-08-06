import importlib
import tp24.model.colour as colour

def tuplify(s, o):
    if type(s).__name__ != type(o).__name__:
        pass
    sv = tuple(s)
    ov = tuple(o)
    if len(sv) < len(ov): sv = tuple(list(sv)+[255])
    if len(ov) < len(sv): ov = tuple(list(ov)+[255])
    return sv, ov

def getclass(cls, cls2):
    classname = type(cls).__name__
    if (issubclass(type(cls), colour.ColourAlpha) or issubclass(type(cls2), colour.ColourAlpha)) and not classname.endswith("a"):
        classname += 'a'
    modulename = type(cls).__name__ if not issubclass(type(cls), colour.ColourAlpha) else type(cls).__name__[:-1]
    module = importlib.import_module("tp24.model.m_"+modulename)
    return getattr(module, classname)

def unalpha(i, cls):
    return i[:-1] if issubclass(type(cls), colour.ColourAlpha) else i

def samemodel(a, b):
    if unalpha(type(a).__name__, a) != unalpha(type(b).__name__, b):
        funcname = unalpha(type(a).__name__, a)
        return getattr(b, funcname)()
    else:
        return b