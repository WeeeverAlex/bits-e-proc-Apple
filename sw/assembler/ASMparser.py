import sys


class Parser:
    # DONE
    def __init__(self, inputFile):
        self.file = inputFile  # self.openFile()  # arquivo de leitura
        self.code = self.file.readlines()
        self.lineNumber = 0  # linha atual do arquivo (nao do codigo gerado)
        self.currentCommand = []  # comando atual
        self.currentLine = ""  # linha de codigo atual
        self.CommandType = {"A": "A_COMMAND", "C": "C_COMMAND", "L": "L_COMMAND"}

    # DONE
    def openFile(self):
        try:
            return open(self.inputFile, "r")
        except IOError:
            sys.exit("Erro: inputFile not found: {}".format(self.inputFile))

    # DONE
    def reset(self):
        self.file.seek(0)

    # DONE
    def close(self):
        self.file.close()

    # DONE
    def advanced(self):
        """
        Carrega uma instrução e avança seu apontador interno para o próxima
        linha do arquivo de entrada. Caso não haja mais linhas no arquivo de
        entrada o método retorna "Falso", senão retorna "Verdadeiro".
        @return Verdadeiro se ainda há instruções, Falso se as instruções terminaram.
        """

        # você deve varrer self.file (arquivo já aberto) até encontrar: fim de arquivo
        # ou uma nova instrucao
        texto = self.code
        while len(texto) > self.lineNumber:
            self.currentCommand = []
            linhas = texto[self.lineNumber].strip()
            linhas = linhas.split()
            self.lineNumber += 1

            for linha in linhas:
                if linha == ';':
                    break
                else:
                    self.currentCommand.append(linha.replace(",",""))

            if self.currentCommand != []:
                return True

        return False
            

    # DONE
    def commandType(self):
        """
        Retorna o tipo da instrução passada no argumento:
         - self.commandType['A'] para leaw, por exemplo leaw $1,%A
         - self.commandType['L'] para labels, por exemplo Xyz: , onde Xyz é um símbolo.
         - self.commandType['C'] para todos os outros comandos
        @param  self.currentCommand
        @return o tipo da instrução.
        """

        if self.currentCommand[0] == "leaw":
            return self.CommandType["A"]
        elif self.currentCommand[0][-1] == ":":
            return self.CommandType["L"]
        else:
            return self.CommandType["C"]



    # TODO
    def symbol(self):
        """
        Retorna o símbolo ou valor numérico da instrução passada no argumento.
        Deve ser chamado somente quando commandType() é A_COMMAND.
        @param  command instrução a ser analisada.
        @return somente o símbolo ou o valor número da instrução.
        """

        if self.commandType() == self.CommandType["A"]:
            return self.currentCommand[1].replace("$","")

    # TODO
    def label(self):
        """
        Retorna o símbolo da instrução passada no argumento.
        Deve ser chamado somente quando commandType() é L_COMMAND.
        @param  command instrução a ser analisada.
        @return o símbolo da instrução (sem os dois pontos).
        """

        if self.commandType() == self.CommandType["L"]:
            return self.currentCommand[0].replace(":","")

    # DONE
    def command(self):
        return self.currentCommand

    # DONE
    def instruction(self):
        return self.currentCommand