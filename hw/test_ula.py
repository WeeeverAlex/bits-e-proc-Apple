#!/usr/bin/env python3
import random
from myhdl import block, instance, Signal, intbv, delay, bin
from .ula import *

random.seed(5)
randrange = random.randrange


@block
def test_ula():
    x = Signal(intbv(1)[16:])
    y = Signal(intbv(2)[16:])
    saida = Signal(intbv(0)[16:])
    control = Signal(intbv(0))
    zr = Signal(bool(0))
    ng = Signal(bool(0))
    ula_1 = ula(x, y, control, zr, ng, saida)

    @instance
    def stimulus():
        control.next = 0b000010
        yield delay(10)
        if saida != x + y:
            print("erro 1")

        control.next = 0b000000
        yield delay(10)
        if saida != (x & y):
            print("erro 2")

        control.next = 0b100010
        yield delay(10)
        if saida != y:
            print("erro 3")

        control.next = 0b001010
        yield delay(10)
        if saida != x:
            print("erro 4")

        control.next = 0b100110
        yield delay(10)
        if saida != ~y:
            print("erro 5")

        control.next = 0b011010
        yield delay(10)
        if saida != ~x:
            print("erro 6")

        control.next = 0b101010
        yield delay(10)
        if saida != 0:
            print("erro 7")

        control.next = 0b101000
        yield delay(10)
        if saida != 0:
            print("erro 8")

        control.next = 0b101001
        yield delay(10)
        if saida != intbv(-1)[16:]:
            print("erro 9")

        # ------ zr ng --------#
        if zr != 0 and ng != 1:
            print("erro 10")

        control.next = 0b101000
        yield delay(10)
        if zr != 1 and ng != 0:
            print("erro 11")

        control.next = 0b000010
        yield delay(10)
        if zr != 0 and ng != 0:
            print("erro 12")

    return ula_1, stimulus


@block
def test_zerador():
    z = Signal(bool(0))
    a = Signal(intbv(0))
    y = Signal(intbv(0))
    zerador_1 = zerador(z, a, y)

    @instance
    def stimulus():
        a.next = randrange(2**16 - 1)
        z.next = 0
        yield delay(10)
        if y != a:
            print("erro 1")
            print("%s %s %s" % (bin(z, 1), bin(a, 16), bin(y, 16)))
        z.next = 1
        yield delay(10)
        if y != 0:
            print("erro 2")
            print("%s %s %s" % (bin(z, 1), bin(a, 16), bin(y, 16)))

    return zerador_1, stimulus


@block
def test_comparador():
    a = Signal(intbv(0))
    ng = Signal(bool(0))
    zr = Signal(bool(0))
    comparador_1 = comparador(a, zr, ng, 16)

    @instance
    def stimulus():
        a.next = 0
        yield delay(10)
        if ng != 0 or zr != 1:
            print("erro 1")
            print("%s %s %s" % (bin(a, 16), bin(zr, 1), bin(ng, 1)))
        a.next = 0xFFFF
        yield delay(10)
        if ng != 1 or zr != 0:
            print("erro 2")
            print("%s %s %s" % (bin(a, 16), bin(zr, 1), bin(ng, 1)))
        a.next = 32
        yield delay(10)
        if ng != 0 or zr != 0:
            print("erro 3")
            print("%s %s %s" % (bin(a, 16), bin(zr, 1), bin(ng, 1)))

    return comparador_1, stimulus


@block
def test_inversor():
    z = Signal(bool(0))
    a = Signal(intbv(0))
    y = Signal(intbv(0))

    inversor_1 = inversor(z, a, y)

    @instance
    def stimulus():
        for i in range(256):
            a.next = randrange(2**16 - 1)
            z.next = randrange(2)
            yield delay(10)
            if z == 0:
                if a != y:
                    print("erro")
                    print("%s %s %s" % (bin(z, 1), bin(a, 16), bin(y, 16)))
                    break
            else:
                if a != ~y:
                    print("erro")
                    print("%s %s %s" % (bin(z, 1), bin(a, 16), bin(y, 16)))
                    break

    return inversor_1, stimulus


@block
def test_inc():
    a = Signal(intbv(0))
    q = Signal(intbv(0))

    inc16_1 = inc(a, q)

    @instance
    def stimulus():
        for i in range(256):
            a.next = randrange(2**16 - 2)
            yield delay(1)
            if q != a + 1:
                print("erro")
                print("%s %s" % (a, q))
                print("%s %s" % (bin(a, 16), bin(q, 16)))
                break

    return inc16_1, stimulus


@block
def test_add():
    a = Signal(intbv(0))
    b = Signal(intbv(0))
    q = Signal(intbv(0))

    add16_1 = add(a, b, q)

    @instance
    def stimulus():
        for i in range(256):
            a.next, b.next = [randrange(2**15 - 1) for i in range(2)]
            yield delay(1)
            if q != a + b:
                print("erro")
                print("%s %s %s" % (a, b, q))
                print("%s %s %s" % (bin(a, 16), bin(b, 16), bin(q, 16)))
                print("%s" % (bin(a + b, 16)))
                break

    return add16_1, stimulus

