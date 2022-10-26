; Arquivo: Abs.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Copia o valor de RAM[1] para RAM[0] deixando o valor sempre positivo.


PREPARANDO:
    leaw $1, %A
    movw (%A), %D


leaw $ELSE, %A; 
jl
nop

leaw $0, %A
movw %D, (%A)
leaw $END, %A
jmp
nop

ELSE:
    negw %D; 
    leaw $0, %A
    movw %D, (%A)

END: