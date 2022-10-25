; Arquivo: isEven.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; par. Se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.


Preparando:
    leaw $0, %A                                                
    movw $0, (%0)                                                

WHILE:
    leaw $5, %A                                                   
    movw (%A), %D                                                 
    leaw $ENDWHILE, %A                                            
    jle %A                                                       
    nop

    leaw $5, %A                                                   
    movw (%A), %D                                                 
    leaw $2, %A                                                   
    subw D, %A, %D                                                
    movw %D, (%A)                                                 

    leaw $WHILE, %A                                              
    jmp %A                                                        
    nop

ENDWHILE:

leaw $0, %A                                                      
movw (%A), %D                                                    
jl %A                                                             
nop

leaw $0, %A                                                       
movw $1, (%A)                                                     

END: