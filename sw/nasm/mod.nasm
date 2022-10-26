; Arquivo: Mod.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Divide o número posicionado na RAM[0] pelo número posicionado no RAM[1] e armazena a sobra na RAM[2].

;exemplo

;ram[0]-20
;ram[1]-7

;começa while
;20 - 7
;13 - 7
;6 - 7
;-1 verifica que é negativo e pega o cima 



;preparando
leaw $0, %A
movw (%A), %D
; MEU D É 20

WHILE:
leaw $2, %A
movw %D, (%A)
leaw $1, %A
subw %D, (%A), %D
leaw $WHILE 
jge 
nop

;






