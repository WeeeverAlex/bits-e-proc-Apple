

#!/usr/bin/env python3

from myhdl import *
@block
def mux2way(q, a, b, sel):
    """
    q: 16 bits
    a: 16 bits
    b: 16 bits
    sel: 2 bits

    Mux entre a e b, sel é o seletor
    """
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        if sel == 0:
            q.next = a
        elif sel == 1:
            q.next = b
    return comb

@block
def and16(a, b, q):
    """
    a: 16 bits
    b: 16 bits
    q: 16 bits

    and bit a bit entre a e b
    """
    foo = Signal(0)

    @always_comb
    def comb():
        print(a)
        print(b)
        q.next = a and b 

    return comb

@block
def ula(x, y, c, zr, ng, saida, width=16):
    

    zx_out = Signal(modbv(0)[width:])
    nx_out = Signal(modbv(0)[width:])
    zy_out = Signal(modbv(0)[width:])
    ny_out = Signal(modbv(0)[width:])
    and_out = Signal(modbv(0)[width:])
    add_out = Signal(modbv(0)[width:])
    mux_out = Signal(modbv(0)[width:])
    no_out = Signal(modbv(0)[width:])

    c_zx = c(5)
    c_nx = c(4)
    c_zy = c(3)
    c_ny = c(2)
    c_f = c(1)
    c_no = c(0)
    
    z1 = zerador(c_zx,zx_out,x)
    i1 =inversor(c_nx,zx_out, nx_out)
    z2 =zerador(c_zy,zy_out,y)
    i2 =inversor(c_ny,zy_out, ny_out)
    #and1 =and16(nx_out,ny_out,and_out)
    add1 =add(nx_out,ny_out, add_out)
    mux =mux2way(mux_out,and_out,add_out,c_f)
    i_final =inversor(c_no, mux_out,no_out)
    c1 =comparador(no_out,zr,ng,16)


    @always_comb
    def comb():

        saida.next = no_out
        

    return instances()



# -z faz complemento de dois
# ~z inverte bit a bit
@block
def inversor(z, a, y):
    @always_comb
    def comb():
        # pq foi atualizado?
        if z == 0:
            y.next = a
        else:
            y.next = ~a

    return instances()


@block
def comparador(a, zr, ng, width):
    # width insica o tamanho do vetor a
    @always_comb
    def comb():
        if a == 0:
            zr.next = 1
        else:
            zr.next = 0

        if a[width-1]:
            ng.next = 1
        else:
            ng.next = 0
        
    return instances()


@block
def zerador(z, a, y):
    @always_comb
    def comb():
        if z == 0:
            a.next = y
        else:
            a.next = 0

    return instances()


@block
def add(a, b, q):
    @always_comb
    def comb():
        q.next = a + b

    return instances()


@block
def inc(a, q):
    @always_comb
    def comb():
        #add(a, 1, q)
        q.next = a + 1

    return instances()


# ----------------------------------------------
# Conceito B
# ----------------------------------------------


@block
def halfAdder(a, b, soma, carry):
    s = Signal(bool())
    c = Signal(bool())

    @always_comb
    def comb():
        s = a ^ b
        c = a & b

        soma.next = s
        carry.next = c

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]

    haList[0] = halfAdder(a, b, s[0], s[1])  # 2
    haList[1] = halfAdder(c, s[0], soma, s[2])  # 3

    @always_comb
    def comb():
        carry.next = s[1] | s[2]  # 4

    return instances()


@block
def addcla4(a, b, q):
    @always_comb
    def comb():
        pass

    return instances()


@block
def addcla16(a, b, q):
    @always_comb
    def comb():
        q.next = a + b

    return instances()


# ----------------------------------------------
# Conceito A
# ----------------------------------------------


@block
def ula_new(x, y, c, zr, ng, sr, sf, bcd, saida, width=16):
    pass


@block
def bcdAdder(x, y, z):
    pass