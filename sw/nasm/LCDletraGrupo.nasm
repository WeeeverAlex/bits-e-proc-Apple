; Arquivo: LCDletraGrupo.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Escreva no LCD a letra do grupo de vocês
;  - Valide no hardawre
;  - Bata uma foto!

: Criando a Letra A
leaw $17592, %A
movw $-1, (%A)

leaw $17612, %A
movw $-1, (%A)

leaw $17593, %A
movw $-1, (%A)

leaw $17613, %A
movw $-1, (%A)

leaw $17594, %A
movw $-1, (%A)

leaw $17614, %A
movw $-1, (%A)

leaw $17595, %A
movw $-1, (%A)

leaw $17615, %A
movw $-1, (%A)

leaw $18592, %A
movw $-1, (%A)

leaw $18612, %A
movw $-1, (%A)

leaw $18593, %A
movw $-1, (%A)

leaw $18613, %A
movw $-1, (%A)

leaw $18594, %A
movw $-1, (%A)

leaw $18614, %A
movw $-1, (%A)

leaw $18595, %A
movw $-1, (%A)

leaw $18615, %A
movw $-1, (%A)
leaw $57344, %Amovw %A, %D
leaw $17636, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17656, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17676, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17696, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17716, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17736, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17756, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17776, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17796, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17816, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17836, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17856, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17876, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17896, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17816, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17836, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17856, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17876, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17896, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17916, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17936, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17956, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17976, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $17996, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18016, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18036, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18056, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18076, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18096, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18116, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18136, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18156, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18176, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18196, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18216, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18236, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18256, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18276, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18296, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18316, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18336, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18356, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18376, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18396, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18316, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18336, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18356, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18376, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18396, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18416, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18436, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18456, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18476, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18496, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18516, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18536, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18556, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18576, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18596, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18616, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18636, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18656, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18676, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18696, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18716, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18736, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18756, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18776, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18796, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18816, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18836, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18856, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18876, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18896, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18916, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18936, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18956, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18976, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $18996, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19016, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19036, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19056, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19076, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19096, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19116, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19136, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19156, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19176, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19196, %A
movw %D, (%A)


leaw $57344, %A
movw %A, %D
leaw $19216, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19236, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19256, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19276, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19296, %A
movw %D, (%A)


leaw $57344, %A
movw %A, %D
leaw $19316, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19336, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19356, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19376, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19396, %A
movw %D, (%A)


leaw $57344, %A
movw %A, %D
leaw $19416, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19436, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19456, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19476, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19496, %A
movw %D, (%A)


leaw $57344, %A
movw %A, %D
leaw $19516, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19536, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19556, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19576, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19596, %A
movw %D, (%A)


leaw $57344, %A
movw %A, %D
leaw $19616, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19636, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19656, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19676, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19696, %A
movw %D, (%A)


leaw $57344, %A
movw %A, %D
leaw $19716, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19736, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19756, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19776, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19796, %A
movw %D, (%A)


leaw $57344, %A
movw %A, %D
leaw $19816, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19836, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19856, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19876, %A
movw %D, (%A)

leaw $57344, %A
movw %A, %D
leaw $19896, %A
movw %D, (%A)
leaw $7, %Amovw %A, %D
leaw $17591, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17611, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17631, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17651, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17671, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17691, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17711, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17731, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17751, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17771, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17791, %A
movw %D, (%A)


leaw $7, %A
movw %A, %D
leaw $17811, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17831, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17851, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17871, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17891, %A
movw %D, (%A)


leaw $7, %A
movw %A, %D
leaw $17911, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17931, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17951, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17971, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $17991, %A
movw %D, (%A)


leaw $7, %A
movw %A, %D
leaw $18011, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18031, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18051, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18071, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18091, %A
movw %D, (%A)


leaw $7, %A
movw %A, %D
leaw $18111, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18131, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18151, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18171, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18191, %A
movw %D, (%A)


leaw $7, %A
movw %A, %D
leaw $18211, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18231, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18251, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18271, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18291, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18311, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18331, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18351, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18371, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18391, %A
movw %D, (%A)


leaw $7, %A
movw %A, %D
leaw $18411, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18431, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18451, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18471, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18491, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18511, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18531, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18551, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18571, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18591, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18611, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18631, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18651, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18671, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18691, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18711, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18731, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18751, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18771, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18791, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18811, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18831, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18851, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18871, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18891, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18911, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18931, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18951, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18971, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $18991, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19011, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19031, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19051, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19071, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19091, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19111, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19131, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19151, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19171, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19191, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19211, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19231, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19251, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19271, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19291, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19311, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19331, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19351, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19371, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19391, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19411, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19431, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19451, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19471, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19491, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19511, %A
movw %D, (%A)
leaw $7, %A
movw %A, %D
leaw $19531, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19551, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19571, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19591, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19611, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19631, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19651, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19671, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19691, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19711, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19731, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19751, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19771, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19791, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19811, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19831, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19851, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19871, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19891, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19911, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19931, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19951, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19971, %A
movw %D, (%A)

leaw $7, %A
movw %A, %D
leaw $19991, %A
movw %D, (%A)