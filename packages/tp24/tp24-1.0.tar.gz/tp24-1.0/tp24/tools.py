import tp24.internal as internal
import tp24.model.colour as colour
from typing import Union

def gradient(a: colour.Colour, b: colour.Colour, ap: Union[int, float]=0.5, bp: Union[int, float]=0.5):
    b = internal.samemodel(a, b)
    av, bv = internal.tuplify(a, b)
    new = tuple(round((p*ap+q*bp)/(ap+bp)) for p, q in zip(av, bv))
    return internal.getclass(a, b)(*new)

def similarity(a: colour.Colour, b: colour.Colour):
    b = internal.samemodel(a, b)
    at = internal.unalpha(tuple(a), a)
    bt = internal.unalpha(tuple(b), b)
    ait = internal.unalpha(tuple(a.complementary()), a)

    if at == bt: return 1.0
    elif ait == bt: return 0.0

    scores = []
    for c in range(0, len(at)):
        minv = min(at[c], ait[c])
        maxv = max(at[c], ait[c])
        if (bt[c] == at[c]): scores.append(1)
        elif (bt[c] == ait[c]): scores.append(0)
        elif type(a).__name__.startswith("hs") and c == 0:
            #for degrees scales
            swap = False
            if bt[c] < minv:
                minv, maxv = maxv-360, minv
                swap = True
            elif bt[c] > maxv:
                minv, maxv = maxv, minv+360
                swap = True

            if (maxv == at[c] and not swap) or (maxv == at[c] and swap): #-ve gradient
                # m = (0-1)/(maxv-minv) = -1/(maxv-minv)
                # (p-1)/(bv-minv) = m
                # p-1 = m*(bv-minv)
                # p-1 = -1/(maxv-minv)*(bv-minv)
                # p = -1/(maxv-minv)*(bv-minv)+1
                scores.append(-1/(maxv-minv)*(bt[c]-minv)+1)
            elif (minv == at[c] and not swap) or (minv == at[c] and swap): #+ve gradient
                # m = (1-0)/(maxv-minv) = 1/(maxv-minv)
                # (p-0)/(bv-minv) = m
                # p = m*(bv-minv)
                # p = 1/(maxv-minv)*(bv-minv)
                scores.append(1/(maxv-minv)*(bt[c]-minv))
        else:
            if bt[c] < minv and minv == at[c]:
                # m = (1-.5)/minv = .5/minv
                # (p-.5)/(bv-0) = m
                # (p-.5)/bv = m
                # p-.5 = m*bv
                # p-.5 = .5/minv*bv
                # p = .5/min*bv + .5
                scores.append(0.5/minv*bt[c]+0.5)
            elif bt[c] < minv and minv == ait[c]:
                # m = (0-.5)/minv = -.5/minv
                # (p-.5)/(bv-0) = m
                # (p-.5)/bv = m
                # p-.5 = m*bv
                # p-.5 = -.5/minv*bv
                # p = -.5/min*bv + .5
                scores.append(-0.5/minv*bt[c]+0.5)
            elif bt[c] > maxv and maxv == at[c]:
                # m = (.5-1)/(maxr-maxv)) = -.5/(maxr-maxv))
                # (p-1)/(bv-maxv) = m
                # p-1 = m*(bv-maxv)
                # p-1 = -.5/(1-maxv)*(bv-maxv)
                # p = -.5/(maxr-maxv)*(bv-maxv)+1
                scores.append(-0.5/(a.RANGE[c]-maxv)*(bt[c]-maxv)+1)
            elif bt[c] > maxv and maxv == ait[c]:
                # m = (.5-0)/(maxr-maxv)) = .5/(maxr-maxv))
                # (p-0)/(bv-maxv) = m
                # p/(bv-maxv) = m
                # p = m*(bv-maxv)
                # p = .5/(maxr-maxv)*(bv-maxv)
                scores.append(0.5/(a.RANGE[c]-maxv)*(bt[c]-maxv))
            elif minv < bt[c] < maxv and minv == at[c]:
                # m = (0-1)/(maxv-minv) = -1/(maxv-minv)
                # (p-1)/(bv-minv) = m
                # p-1 = m*(bv-minv)
                # p-1 = -1/(maxv-minv)*(bv-minv)
                # p = -1/(maxv-minv)*(bv-minv)+1
                scores.append(-1/(maxv-minv)*(bt[c]-minv)+1)
            elif minv < bt[c] < maxv and minv == ait[c]:
                # m = (1-0)/(maxv-minv) = 1/(maxv-minv)
                # (p-0)/(bv-minv) = m
                # p = m*(bv-minv)
                # p = 1/(maxv-minv)*(bv-minv)
                scores.append(1/(maxv-minv)*(bt[c]-minv))
    
    return sum(scores)/len(scores)