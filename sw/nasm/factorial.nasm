; Arquivo: Factorial.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Calcula o fatorial do número em R0 e armazena o valor em R1.


PREPARANDO:
leaw $1, %A
movw $1, (%A)

leaw $0, %A
movw (%A), %D

leaw $BREAK, %A
je %D
nop

DO:
    leaw $0, %A
    movw (%A), %D

    leaw $BREAK, %A
    decw %D
    je %D
    nop

    leaw $COUNTER, %A
    movw %D, (%A)
    
    leaw $1, %A
    movw (%A), %D
    leaw $NUM, %A
    movw %D, (%A)

    MULT:
        leaw $NUM, %A
        movw (%A), %D

        leaw $1, %A
        addw (%A), %D, %D
        movw %D, (%A)

        leaw $COUNTER, %A
        movw (%A), %D
        decw %D
        movw %D, (%A)

        leaw $MULT, %A
        jne %D
        nop

        leaw $0, %A
        movw (%A), %D
        decw %D
        movw %D, (%A)

        leaw $DO, %A
        jmp
        nop

BREAK: