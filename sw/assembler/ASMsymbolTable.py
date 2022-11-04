

class SymbolTable:
    # DONE
    def __init__(self):
        self.table = {}
        self.init()

    # TODO
    def init(self):
        """
        Inicializa a tabela de simbolos com os simbolos pre definidos
        exemplo: R0, R1, ...
        SP, LCL, ARG, THIS, THAT
        SCREEN, KBD, ..
        """
        self.table[ "SP" ] = 0
        self.table[ "LCL" ] = 1
        self.table[ "ARG" ] = 2
        self.table[ "THIS" ] = 3
        self.table[ "THAT" ] = 4
        self.table[ "SCREEN" ] = 16384
        self.table[ "LED" ] = 21184
        self.table[" SW "] = 21185
        self.table[ "KBD" ] = 24576

        for i in range(16):
            self.table[ "R" + str(i) ] = i
        return self.table

    # TODO
    def addEntry(self, symbol: str, address: int):
        """
        Insere uma entrada de um símbolo com seu endereço numérico na tabela de símbolos (self.table).
        @param symbol símbolo a ser armazenado na tabela de símbolos.
        @param address símbolo a ser armazenado na tabela de símbolos.
        """
        self.table[symbol] = address
        return self.table

    # TODO
    def contains(self, symbol):
        """
        Confere se o símbolo informado já foi inserido na tabela de símbolos.
        @param  symbol símbolo a ser procurado na tabela de símbolos.
        @return Verdadeiro se símbolo está na tabela de símbolos, Falso se não está na tabela de símbolos.
        """
        lista_simbolos = []
        for simbolo in self.table.keys():
            lista_simbolos.append(simbolo)

        if symbol in lista_simbolos:
            return True
        else:
            return False

    # TODO
    def getAddress(self, symbol):
        """
        Retorna o valor númerico associado a um símbolo já inserido na tabela de símbolos.
        @param  symbol símbolo a ser procurado na tabela de símbolos.
        @return valor numérico associado ao símbolo procurado.
        """
        return self.table[symbol]
