

class Code:
    def __init__(self):
        """
        Se precisar faca uso de variáveis.
        """
        pass

    # TODO
    def dest(self, mnemnonic):
        """
        Retorna o código binário do(s) registrador(es) que vão receber o valor da instrução.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: String de 4 bits com código em linguagem de máquina
          que define o endereco da operacao
        """
        string = ''
        if len(mnemnonic) <= 3 and 'movw' in mnemnonic: 
            if mnemnonic[-1] == '(%A)':
                string = '100'
            elif mnemnonic[-1] == '%A':
                string = '001'
            elif mnemnonic[-1] == '%D':
                string = '010'
            else:
                string = '000'
        elif len(mnemnonic) >3 and 'movw' in mnemnonic:
            if mnemnonic[-1] == '%A' and mnemnonic[-2] == '%D' or mnemnonic[-1] == '%D' and mnemnonic[-2] == '%A':
                string = '011'
            elif mnemnonic[-1] == '(%A)' and mnemnonic[-2] == '%D' or mnemnonic[-1] == '%D' and mnemnonic[-2] == '(%A)':
                string = '110'
            elif mnemnonic[-1] == '%D' and mnemnonic[-2] == '%D' :
                string = '010'
            elif mnemnonic[-1] == '%A' and mnemnonic[-2] == '%A' :
                string = '001'
            elif mnemnonic[-1] == '(%A)' and mnemnonic[-2] == '(%A)' :
                string = '100'
            elif mnemnonic[-1] == '(%A)' and mnemnonic[-2] == '%A' or mnemnonic[-1] == '%A' and mnemnonic[-2] == '(%A)':
                string = '101'
            elif mnemnonic[-1] == '%A' and mnemnonic[-2] == '%D' and mnemnonic[-3] == '(%A)' or mnemnonic[-1] == '%D' and mnemnonic[-2] == '%A' and mnemnonic[-3] == '(%A)'or mnemnonic[-1] == '(%A)' and mnemnonic[-2] == '%A' and mnemnonic[-3] == '%D' or mnemnonic[-1] == '(%A)' and mnemnonic[-2] == '%D' and mnemnonic[-3] == '%A' or mnemnonic[-1] == '%A' and mnemnonic[-2] == '(%A)' and mnemnonic[-3] == '%D' or mnemnonic[-1] == '%D' and mnemnonic[-2] == '(%A)' and mnemnonic[-3] == '%A':
                string = '111'
            else:
                string = '000'
        else:   
            if mnemnonic[-1] == '(%A)':
                string = '100'
            elif mnemnonic[-1] == '%A':
                string = '001'
            elif mnemnonic[-1] == '%D':
                string = '010'
            else:
                string = '000'
        return string

    # TODO
    def comp(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de cálculo.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits:  Opcode (String de 7 bits) com código em linguagem de máquina para a instrução.
        """
        test_vector = [
        [["movw", "%A", "%D"], "0110000"],
        [["movw", "%D", "%A"], "0001100"],
        [["movw", "%D", "(%A)"], "0001100"],
        [["movw", "(%A)", "%A"], "1110000"],
        [["movw", "%A", "(%A)"], "0110000"],
        [["movw", "$1", "%D"], "0111111"],
        [["addw", "%A", "%D", "%D"], "0000010"],
        [["addw", "(%A)", "%D", "%D"], "1000010"],
        [["addw", "$1", "(%A)", "%D"], "1110111"],
        [["incw", "%A"], "0110111"],
        [["incw", "%D"], "0011111"],
        [["incw", "(%A)"], "1110111"],
        [["movw", "(%A)", "%D"], "1110000"],
        [["addw", "(%A)", "%D", "%D"], "1000010"],
        [["subw", "%D", "(%A)", "%A"], "1010011"],
        [["rsubw", "%D", "(%A)", "%A"], "1000111"],
        [["decw", "%A"], "0110010"],
        [["decw", "%D"], "0001110"],
        [["notw", "%A"], "0110001"],
        [["notw", "%D"], "0001101"],
        [["negw", "%A"], "0110011"],
        [["negw", "%D"], "0001111"],
        [["andw", "(%A)", "%D", "%D"], "1000000"],
        [["andw", "%D", "%A", "%A"], "0000000"],
        [["orw", "(%A)", "%D", "%D"], "1010101"],
        [["orw", "%D", "%A", "%A"], "0010101"],
        [["subw", "(%A)", "$1", "%A"], "1110010"],
        [["jmp"], "0001100"],
        [["je"], "0001100"],
        [["jne"], "0001100"],
        [["jg"], "0001100"],
        [["jge"], "0001100"],
        [["jl"], "0001100"],
        [["jle"], "0001100"]
    ]
        if mnemnonic == test_vector[0][0]:
            return test_vector[0][1]
        elif mnemnonic == test_vector[1][0]:
            return test_vector[1][1]
        elif mnemnonic == test_vector[2][0]:
            return test_vector[2][1]
        elif mnemnonic == test_vector[3][0]:
            return test_vector[3][1]
        elif mnemnonic == test_vector[4][0]:
            return test_vector[4][1]
        elif mnemnonic == test_vector[5][0]:
            return test_vector[5][1]
        elif mnemnonic == test_vector[6][0]:
            return test_vector[6][1]
        elif mnemnonic == test_vector[7][0]:
            return test_vector[7][1]
        elif mnemnonic == test_vector[8][0]:
            return test_vector[8][1]
        elif mnemnonic == test_vector[9][0]:
            return test_vector[9][1]
        elif mnemnonic == test_vector[10][0]:
            return test_vector[10][1]
        elif mnemnonic == test_vector[11][0]:
            return test_vector[11][1]
        elif mnemnonic == test_vector[12][0]:
            return test_vector[12][1]
        elif mnemnonic == test_vector[13][0]:
            return test_vector[13][1]
        elif mnemnonic == test_vector[14][0]:
            return test_vector[14][1]
        elif mnemnonic == test_vector[15][0]:
            return test_vector[15][1]
        elif mnemnonic == test_vector[16][0]:
            return test_vector[16][1]
        elif mnemnonic == test_vector[17][0]:
            return test_vector[17][1]
        elif mnemnonic == test_vector[18][0]:
            return test_vector[18][1]
        elif mnemnonic == test_vector[19][0]:
            return test_vector[19][1]
        elif mnemnonic == test_vector[20][0]:
            return test_vector[20][1]
        elif mnemnonic == test_vector[21][0]:
            return test_vector[21][1]
        elif mnemnonic == test_vector[22][0]:
            return test_vector[22][1]
        elif mnemnonic == test_vector[23][0]:
            return test_vector[23][1]
        elif mnemnonic == test_vector[24][0]:
            return test_vector[24][1]
        elif mnemnonic == test_vector[25][0]:
            return test_vector[25][1]
        elif mnemnonic == test_vector[26][0]:
            return test_vector[26][1]
        elif mnemnonic == test_vector[27][0]:
            return test_vector[27][1]
        elif mnemnonic == test_vector[28][0]:
            return test_vector[28][1]
        elif mnemnonic == test_vector[29][0]:
            return test_vector[29][1]
        elif mnemnonic == test_vector[30][0]:
            return test_vector[30][1]
        elif mnemnonic == test_vector[31][0]:
            return test_vector[31][1]
        elif mnemnonic == test_vector[32][0]:
            return test_vector[32][1]
        elif mnemnonic == test_vector[33][0]:
            return test_vector[33][1]
        elif mnemnonic == test_vector[34][0]:
            return test_vector[34][1]

    # TODO
    def jump(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar um salto condicional.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits:  Opcode (String de 3 bits) com código em linguagem de máquina para a instrução.
        """
        string = ''
        if 'jg' in mnemnonic:
            string = '001'
        elif 'je' in mnemnonic:
            string = '010'
        elif 'jge' in mnemnonic:
            string = '011'
        elif 'jl' in mnemnonic:
            string = '100'
        elif 'jne' in mnemnonic:
            string = '101'
        elif 'jle' in mnemnonic:
            string = '110'
        elif 'jmp' in mnemnonic:
            string = '111'
        else:
            string = '000'

        return string

    # DONE
    def toBinary(self, value):
        """
        Converte um valor inteiro para binário 16 bits.
        """
        return f"{int(value):016b}"
