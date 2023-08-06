
a = 'mo'
b = 'mO'
c = 'Mo'
d = 'MO'
e = 'mOo'
f = 'MOo'
g = 'MOO'
h = 'MoO'
i = 'moO'
j = 'moo'
k = 'Mmoo'
l = 'MmOo'
m = 'MMoO'
n = 'mMOO'
o = 'mmOO'
p = 'mMoO'
r = 'MmOo'
s = 'ooM'
t = 'oOm'
q = 'ooMM'
u = 'Moomo'



def Encode(word):
    #word =word.replace('o', o)
    #word =word.replace('m', m)
    #for i in word:
    word = word.replace('a', a)
    word =word.replace('b', b)
    word =word.replace('c', c)
    word =word.replace('d', d)
    word =word.replace('e', e)
    word =word.replace('f', f)
    word =word.replace('g', g)
    word =word.replace('h', h)
    word =word.replace('i', i)
    word =word.replace('j', j)
    word =word.replace('k', k)
    word =word.replace('l', l)
    word =word.replace('n', n)
    word =word.replace('p', p)
    word =word.replace('r', r)
    word =word.replace('s', s)
    word =word.replace('t', t)
    word =word.replace('q', q)
    word = word.replace('u', u)

def Decode(word):
    #word =word.replace(o, 'o')
    #word =word.replace(m, 'm')
    #for i in word:
    word = word.replace(u, 'u')
    word =word.replace(r, 'r')
    word =word.replace(i, 'i')
    word =word.replace(e, 'e')
    word = word.replace(a, 'a')
    word =word.replace(b, 'b')
    word =word.replace(c, 'c')
    word =word.replace(d, 'd')
    word =word.replace(f, 'f')
    word =word.replace(g, 'g')
    word =word.replace(h, 'h')
    word =word.replace(j, 'j')
    word =word.replace(k, 'k')
    word =word.replace(l, 'l')
    word =word.replace(n, 'n')
    word =word.replace(p, 'p')
    word =word.replace(s, 's')
    word =word.replace(t, 't')
    word =word.replace(q, 'q')
    word = word.replace(' ', '')
