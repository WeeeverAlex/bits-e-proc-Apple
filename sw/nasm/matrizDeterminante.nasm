; Arquivo: matrizDeterminante.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 03/2019
;
; Calcula o determinante de uma matriz 2x2 (RAM[1000]) e
;  salva seu resultado no endereço RAM[0]
;
; Calcula o determinante de uma matriz 2x2 (RAM[1000]) na forma
; [ a0, a1 ]
; [ b0, b1 ]
;
; Salva o resultado no endereço RAM[0]
;
; A matriz é salva na memória da seguinte maneira:
; RAM[1000] = a0
; RAM[1001] = a1
; RAM[1003] = b0
; RAM[1004] = b1


PREPARANDO:
    leaw $1, %A 
    movw $0, (%A) 
    leaw $2, %A
    movw $0, (%A) 

WHILE:
    leaw $1000, %A
    movw (%A), %D
    leaw $END, %A
    je
    nop


    leaw $1004, %A ; soma
    movw (%A), %D
    leaw $1, %A
    addw (%A), %D, %D
    movw %D, (%A)
    leaw $1000, %A 
    subw (%A), $1, %D
    movw %D, (%A)
    leaw $WHILE, %A
    jmp
    nop


END:

WHILE2:
    leaw $1001, %A
    movw (%A), %D
    leaw $END2, %A
    je
    nop


    leaw $1003, %A 
    movw (%A), %D
    leaw $2, %A
    addw (%A), %D, %D
    movw %D, (%A)
    leaw $1001, %A 
    subw (%A), $1, %D
    movw %D, (%A)
    leaw $WHILE2, %A
    jmp
    nop
    

END2:
leaw $1, %A
movw (%A), %D
leaw $2, %A
subw %D, (%A), %D
leaw $0, %A 
movw %D, (%A)