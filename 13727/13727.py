mod = 10**9+7;

class vector:
    def __init__(self, size=0, default=0):
        if type(size) == list:
            self.raw = size
        else:
            self.raw = [default]*size

    def __getitem__(self, index):
        if index < self.size():
            return self.raw[index]
        else:
            raise IndexError

    def __setitem__(self, index, value):
        if index < self.size():
            self.raw[index] = value
        else:
            raise IndexError

    def size(self):
        return len(self.raw)

    def empty(self):
        return self.size() == 0

    def resize(self, size, default=0):
        if self.size() >= size:
            self.raw = self.raw[:size]
        else:
            while self.size() < size:
                self.raw.append(default)

    def push_back(self, value):
        self.raw.append(value)

def ipow(x, p):
    ret = 1
    piv = x
    while p:
        if p & 1: 
            ret = ret * piv % mod
        piv = piv * piv % mod
        p >>= 1
    return ret

def berlekamp_massey(x):
    ls, cur = vector(), vector()
    lf, ld = 0, 0
    for i in range(x.size()):
        t = 0
        for j in range(cur.size()):
            t = (t + x[i-j-1] * cur[j]) % mod
        # end
        if (t - x[i]) % mod == 0: continue
        if cur.empty():
            cur.resize(i+1)
            lf = i
            ld = (t - x[i]) % mod
            continue
        # end
        k = -(x[i] - t) * ipow(ld, mod - 2) % mod
        c = vector(i-lf-1)
        c.push_back(k)
        for j in ls: c.push_back(-j * k % mod)
        if c.size() < cur.size(): c.resize(cur.size())
        for j in range(cur.size()):
            c[j] = (c[j] + cur[j]) % mod
        # end
        if i-lf+ls.size() >= cur.size():
            ls, lf, ld = cur, i, (t - x[i]) % mod
        # end
        cur = c
    for i in range(cur.size()):
        cur[i] = (cur[i] % mod + mod) % mod
    return cur
# end

def get_nth(rec, dp, n):
    m = rec.size()
    s, t = vector(m), vector(m)
    s[0] = 1
    if m != 1: t[1] = 1
    else: t[0] = rec[0]
    def mul(v, w):
        m = v.size()
        t = vector(2*m)
        for j in range(m):
            for k in range(m):
                t[j+k] += v[j] * w[k] % mod
                if t[j+k] >= mod: t[j+k] -= mod
            # end
        # end
        for j in range(2*m-1, m-1, -1):
            for k in range(1, m+1):
                t[j-k] += t[j] * rec[k-1] % mod
                if t[j-k] >= mod: t[j-k] -= mod
            # end
        # end
        t.resize(m)
        return t
    # end
    while n:
        if n & 1:
            s = mul(s, t)
        t = mul(t, t)
        n //= 2

    ret = 0
    for i in range(m):
        ret += s[i] * dp[i] % mod
    return ret % mod
# end

def guess_nth_term(x, n):
    if n < x.size(): return x[n]
    v = berlekamp_massey(x)
    if v.empty(): return 0
    return get_nth(v, x, n)

x = vector([
    1, 272, 589185, 930336768, 853401154,
    217676188, 136558333, 415722813, 985269529, 791527976,
    201836136, 382110354, 441223705, 661537677, 641601343,
    897033284, 816519670, 365311407, 300643484, 936803543,
    681929467, 462484986, 13900203, 657627114, 96637209,
    577140657, 600647073, 254604056, 102389682, 811580173,
    592550067, 587171680, 526467503, 265885773, 951722780,
    219627841, 371508152, 283501391, 159234514, 439380999,
    722868959, 125599834, 351398134, 456317548, 365496182,
    614778702, 502680047, 193063685, 309004764, 743901785,
    870955115, 312807829, 160375015, 691844624, 137034372,
    350330868, 895680450, 282610535, 317897557, 28600551,
    583305647, 539409363, 327406961, 627805385, 680183978,
    681299085, 954964592, 743524009, 788048339, 699454626,
    666369521, 857206425, 490463127, 477198247, 599963928,
    21247982, 107843532, 753662937, 239039324, 608530376,
    523383010, 654448101, 801430395, 393034561, 93313778,
    983052766, 240336620, 825539982, 525118275, 563899476,
    706271688, 547405697, 477082486, 664058071, 353207278,
    729486413, 795704637, 999271072, 540749624, 411451016,
    736422999, 879369181, 918733916, 982303557, 512499644,
    261033810, 391766409, 334092786, 931794834, 854181848,
    821090190, 751839258, 433126935, 571194155, 52438113,
    552977155, 320805296, 173355929, 969659468, 258854248,
    159509877, 374487748, 401382023, 44060530, 510164669,
    336596764, 652050424, 373872552, 517226592, 719871041,
    43959496, 235333335, 304962191, 253114421, 43638769,
    361871585, 8060121, 147014624, 114846460, 430864038,
    368951246, 863795701
])

print(guess_nth_term(x, int(input())))
