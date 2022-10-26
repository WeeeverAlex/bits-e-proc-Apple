; Arquivo: SWeLED.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Faça os LEDs exibirem 
; LED = ON ON ON ON ON !SW3 !SW2 !SW1 0
; sw -> "interruptor"
; 21184 -> led
; 21185 -> sw
; 5 -> 1
; 3 -> sw
; 1 -> 0


;COMEÇANDO PELO SW

leaw $21185, %A
movw (%A), %D           ;D = RAM[21185]
notw %D                 ;D = !D -> !D = RAM[21185]

leaw $14, %A            ;14 = selecionador
andw %A, %D, %D         ;D = D & 14



;ON

leaw $496, %A           ;496 = selecionador
orw %A, %D, %D          ;D = D | 496


;FINALIZANDO

leaw $21184, %A         ;RAM[21184] = led
movw %D, (%A)           ;D = RAM[21184]