from .ASMsymbolTable import SymbolTable
from .ASMcode import Code
from .ASMparser import Parser


class ASM:

    # DONE
    def __init__(self, nasm, hack):
        self.hack = hack
        self.symbolTable = SymbolTable()
        self.parser = Parser(nasm)
        self.code = Code()

    # DONE
    def run(self):
        try:
            self.fillSymbolTable()
            self.generateMachineCode()
            return 0
        except:
            print("--> ERRO AO TRADUZIR: {}".format(self.parser.currentLine))
            return -1

    # TODO
    def fillSymbolTable(self):
        """
        primeiro passo para a construção da tabela de símbolos de marcadores (labels)
        varre o código em busca de novos Labels e Endereços de memórias (variáveis)
        e atualiza a tabela de símbolos com os endereços (table).

        Dependencia : Parser, SymbolTable
        """
        rom = 0
        while self.parser.advanced():

            if self.parser.commandType() == "L_COMMAND":
                self.symbolTable.addEntry(self.parser.label(), rom)

            else:
                rom += 1

        self.parser.reset()

    # TODO
    def generateMachineCode(self):
        """
        Segundo passo para a geração do código de máquina
        Varre o código em busca de instruções do tipo A, C
        gerando a linguagem de máquina a partir do parse das instruções.

        Dependencias : Parser, Code
        """

        while self.parser.advanced():
            if self.parser.commandType() == "C_COMMAND":
                if self.parser.currentCommand[0] == "nop":
                    bin = "0000000000000000"
                else:
                    bin = "111" + self.code.comp(self.parser.comp()) + self.code.dest(self.parser.dest()) + self.code.jump(self.parser.jump())
                self.hack.write(bin)

            elif self.parser.commandType() == "A_COMMAND":
                if self.parser.symbol().isdigit():
                    bin = "0" + self.toBinary(self.parser.symbol())
                else:
                    if self.symbolTable.contains(self.parser.symbol()):
                        bin = "0" + self.toBinary(self.symbolTable.getAddress(self.parser.symbol()))
                    else:
                        self.symbolTable.addEntry(self.parser.symbol(), self.symbolTable.getNextAddress())
                        bin = "0" + self.toBinary(self.symbolTable.getAddress(self.parser.symbol()))
                self.hack.write(bin)

    # DONE
                
                

                
