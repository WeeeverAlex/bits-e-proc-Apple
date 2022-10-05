#!/usr/bin/env python3

from myhdl import *
from .components import *

@block
def ram(dout, din, addr, we, clk, rst, width, depth):
    loads = [Signal(bool(0)) for i in range(depth)]
    outputs = [Signal(modbv(0)[width:]) for i in range(depth)]
    registersList = [None for i in range(depth)]

    @always_comb
    def comb():
        pass

    return instances()


@block
def pc(increment, load, i, output, width, clk, rst):
    regIn = Signal(modbv(0)[width:])
    regOut = Signal(modbv(0)[width:])
    regLoad = Signal(bool(0))
    

    @always_comb
    def comb():
        pass

    return instances()


@block
def registerN(i, load, output, width, clk, rst):
    binaryDigitList = [None for n in range(width)]
    outputs = [Signal(bool(0)) for n in range(width)]

    for a in range(len(binaryDigitList)):
        binaryDigitList[a] = binaryDigit(i(a), load, outputs[a], clk, rst)

    @always_comb
    def comb():
        for b in range(len(outputs)):
            output.next[b] = outputs[b]

    return instances()


@block
def register8(i, load, output, clk, rst):
    binaryDigitList = [None for n in range(8)]
    output_n = [Signal(bool(0)) for n in range(8)]

    for a in range(len(binaryDigitList)):
        binaryDigitList[a] = binaryDigit(i(a), load, output_n[a], clk, rst)

    @always_comb
    def comb():
        for b in range(len(output_n)):
            output.next[b] = output_n[b]

    return instances()


@block
def binaryDigit(i, load, output, clk, rst):
    q, d, clear, presset = [Signal(bool(0)) for i in range(4)]
    dff_ = dff(q, d, clear, presset, clk, rst)
    mux = mux2way(d, q, i, load)
    
    @always_comb
    def comb():
        output.next = q
    
    return instances()


@block
def dff(q, d, clear, presset, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def logic():
        if clear:
            q.next = 0
        elif presset:
            q.next = 1
        else:
            q.next = d

    return instances()