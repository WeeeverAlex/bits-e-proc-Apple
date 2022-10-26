; Arquivo: Pow.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Eleva ao quadrado o valor da RAM[1] e armazena o resultado na RAM[0].
; Só funciona com números positivos

;jmp -> vai fazer o desvio sem se preocupar com o valor do registrador
;je -> vai fazer o desvio se o valor do registrador for igual a zero
;jne -> vai fazer o desvio se o valor do registrador for diferente de zero
;jg -> vai fazer o desvio se o valor do registrador for maior que zero
;jge -> vai fazer o desvio se o valor do registrador for maior ou igual a zero
;jl -> vai fazer o desvio se o valor do registrador for menor que zero
;jle -> vai fazer o desvio se o valor do registrador for menor ou igual a zero


Preparando:
    leaw $0, %A
    movw $0, (%A)   ;RAM[0] = 0

    leaw $1, %A
    movw (%A), %D   ;RAM[1] = D

    leaw $2, %A
    movw %D, (%A)   ;RAM[2] = D


WHILE:
    leaw $2, %A     ;A = 2
    movw (%A), %D   ;D = RAM[2]
    leaw $END, %D   
    je  
    nop

    leaw $1, %A         ;A = 1
    movw (%A), %D       ;D = RAM[1]
    leaw $0, %A         ;A = 0
    addw (%A), %D, %D   ;D = RAM[1] + RAM[0]
    movw %D, (%A)       ;RAM[0] = RAM[1] + RAM[0]

    leaw $2, %A         ;A = 2
    subw (%A), $1, %D   ;D = RAM[2] - 1
    movw %D, (%A)       ;RAM[2] = D 

    leaw $WHILE, %A
    jmp
    nop
END:
