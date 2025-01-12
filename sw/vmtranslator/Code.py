#!/usr/bin/env python3
import io
import os
import queue
import uuid


class Code:
    def __init__(self, outFile):
        self.outFile = outFile
        self.counter = 0
        self.vmFileName = None
        self.labelCounter = 0

    # DONE
    def close(self):
        self.outFile.close()

    # DONE
    def updateVmFileName(self, name):
        self.vmFileName = os.path.basename(name).split(".")[0]

    # DONE
    def commandsToFile(self, commands):
        for line in commands:
            self.outFile.write(f"{line}\n")

    # DONE
    def getUniqLabel(self):
        return self.vmFileName + str(self.labelCounter)

    # DONE
    def updateUniqLabel(self):
        self.labelCounter = self.labelCounter + 1

    # DONE
    def writeHead(self, command):
        self.counter = self.counter + 1
        return ";; " + command + " - " + str(self.counter)

    # DONE
    def writeInit(self, bootstrap, isDir):
        commands = []

        if bootstrap or isDir:
            commands.append(self.writeHead("init"))

        if bootstrap:
            commands.append("leaw $256,%A")
            commands.append("movw %A,%D")
            commands.append("leaw $SP,%A")
            commands.append("movw %D,(%A)")

        if isDir:
            commands.append("leaw $Main.main, %A")
            commands.append("jmp")
            commands.append("nop")

        if bootstrap or isDir:
            self.commandsToFile(commands)

    # TODO
    def writeLabel(self, label):
        commands = []
        commands.append(self.writeHead("label") + " " + label)

        commands.append(label + ":")
        # TODO ...
        commands.append(label + ":")
        self.commandsToFile(commands)

    # TODO
    def writeGoto(self, label):
        commands = []
        commands.append(self.writeHead("goto") + " " + label)
        commands.append("leaw $" + label + ", %A")
        commands.append("jmp")
        commands.append("nop")

        commands.append("leaw $" + label + ", %A")
        commands.append("jmp")
        commands.append("nop")
        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeIf(self, label):
        commands = []
        commands.append(self.writeHead("if") + " " + label)

        commands.append("leaw $SP, %A") 
        commands.append("subw (%A), $1, %D")
        commands.append('movw %D, (%A)')
        commands.append('movw %D, %A')
        commands.append('movw (%A), %D')
        commands.append("notw %D") 
        commands.append("leaw $" + label + ", %A")
        commands.append('je')
        
        self.commandsToFile(commands)

     # TODO
    def writeArithmetic(self, command):
        self.updateUniqLabel()
        if len(command) < 2:
            print("instrucão invalida {}".format(command))
        commands = []
        commands.append(self.writeHead(command))

        if command == "add":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")  # A ta com 258 
            commands.append("decw %A")   # A = 257
            commands.append("movw (%A), %D")  # D ta com y
            commands.append("decw %A")   # A = 256
            commands.append("addw (%A), %D, %D") # (A) ta com x, x+y em D
            commands.append("movw %D, (%A)") 
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")


        elif command == "sub":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")  # A ta com 258 
            commands.append("decw %A")   # A = 257
            commands.append("movw (%A), %D")  # D ta com y
            commands.append("decw %A")   # A = 256
            commands.append("subw (%A), %D, %D") # (A) ta com x, x+y em D
            commands.append("movw %D, (%A)") 
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
        
        elif command == "or":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")  # A ta com 258 
            commands.append("decw %A")   # A = 257
            commands.append("movw (%A), %D")  # D ta com y
            commands.append("decw %A")   # A = 256
            commands.append("orw (%A), %D, %D") # (A) ta com x, xory em D
            commands.append("movw %D, (%A)") 
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            
        elif command == "and":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")  # A ta com 258 
            commands.append("decw %A")   # A = 257
            commands.append("movw (%A), %D")  # D ta com y
            commands.append("decw %A")   # A = 256
            commands.append("andw (%A), %D, %D") # (A) ta com x, xory em D
            commands.append("movw %D, (%A)") 
            commands.append("incw %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            
            

        elif command == "not":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")  # A ta com 257
            commands.append("decw %A")   # A = 256
            commands.append("movw (%A), %D")  # D ta com x
            commands.append("notw, %D, %D") # D ta x not 
            commands.append("movw %D, (%A)")  # D em 256
            commands.append("incw %A")   
            commands.append("movw %A, %D")  # 
            commands.append("leaw $SP ,%A")   
            commands.append("movw %D, (%A)")  # 
        
        
        
        elif command == "neg":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")  # A ta com 257
            commands.append("decw %A")   # A = 256
            commands.append("movw (%A), %D")  # D ta com x
            commands.append("negw, %D, %D") # D ta x not 
            commands.append("movw %D, (%A)")  # D em 256
            commands.append("incw %A")   
            commands.append("movw %A, %D")  # 
            commands.append("leaw $SP ,%A")   
            commands.append("movw %D, (%A)")  # 
        
        elif command == "eq":
            # dica, usar self.getUniqLabel() para obter um label único

            zerou = self.getUniqLabel()
            self.updateUniqLabel()
            fim = self.getUniqLabel()

            commands.append("leaw $SP, %A")   
            commands.append("movw (%A), %A")  # A = 258 
            
            commands.append("decw %A")   # A= 257
            commands.append("movw (%A), %D")   # D TA C Y
            commands.append("decw %A")  # A= 256
            commands.append("subw (%A), %D, %D")   # D TA C X-Y

            commands.append(f"leaw ${zerou}, %A")     
            commands.append("je")  
            commands.append("nop")  
            
            commands.append("leaw $0, %A")  
            commands.append("movw %A, %D") 
            
            commands.append("leaw $SP, %A") 
            commands.append('movw (%A), %A')
            commands.append("decw %A") 
            commands.append("decw %A") 
            commands.append("movw %D, (%A)")      

            commands.append(f"leaw ${fim}, %A")     
            commands.append("jmp")  
            commands.append("nop")       
            
            
            commands.append(f"{zerou}:")  
            
            commands.append("leaw $65535, %A")  
            commands.append("movw %A, %D") 
            commands.append("leaw $SP, %A") 
            commands.append('movw (%A), %A')
            commands.append("decw %A") 
            commands.append("decw %A") 
            commands.append("movw %D, (%A)") 

            commands.append(f"{fim}:")  
            commands.append("leaw $SP, %A")  
            commands.append("movw (%A), %D") 
            commands.append("decw %D") 
            commands.append("movw %D, (%A)") 
        


            



            pass # TODO
        elif command == "gt":

            pozi = self.getUniqLabel()
            self.updateUniqLabel()
            fim= self.getUniqLabel()

            commands.append("leaw $SP, %A")   
            commands.append("movw (%A), %A")  # A = 258 
            
            commands.append("decw %A")   # A= 257
            commands.append("movw (%A), %D")   # D TA C Y
            commands.append("decw %A")  # A= 256
            commands.append("subw (%A), %D, %D")   # D TA C X-Y

            commands.append(f"leaw ${pozi}, %A")     
            commands.append("jg")  
            commands.append("nop")  
            
            commands.append("leaw $0, %A")  
            commands.append("movw %A, %D") 
            
            commands.append("leaw $SP, %A") 
            commands.append('movw (%A), %A')
            commands.append("decw %A") 
            commands.append("decw %A") 
            commands.append("movw %D, (%A)")      

            commands.append(f"leaw ${fim}, %A")     
            commands.append("jmp")  
            commands.append("nop")       
            
            
            commands.append(f"{pozi}:")  
            
            commands.append("leaw $65535, %A")  
            commands.append("movw %A, %D") 
            commands.append("leaw $SP, %A") 
            commands.append('movw (%A), %A')
            commands.append("decw %A") 
            commands.append("decw %A") 
            commands.append("movw %D, (%A)") 

            commands.append(f"{fim}:")  
            commands.append("leaw $SP, %A")  
            commands.append("movw (%A), %D") 
            commands.append("decw %D") 
            commands.append("movw %D, (%A)") 
        




        elif command == "lt":
            # dica, usar self.getUniqLabel() para obter um label único
            neg = self.getUniqLabel()
            self.updateUniqLabel()
            fim= self.getUniqLabel()

            commands.append("leaw $SP, %A")   
            commands.append("movw (%A), %A")  # A = 258 
            
            commands.append("decw %A")   # A= 257
            commands.append("movw (%A), %D")   # D TA C Y
            commands.append("decw %A")  # A= 256
            commands.append("subw (%A), %D, %D")   # D TA C X-Y

            commands.append(f"leaw ${neg}, %A")     
            commands.append("jl")  
            commands.append("nop")  
            
            commands.append("leaw $0, %A")  
            commands.append("movw %A, %D") 
            
            commands.append("leaw $SP, %A") 
            commands.append('movw (%A), %A')
            commands.append("decw %A") 
            commands.append("decw %A") 
            commands.append("movw %D, (%A)")      

            commands.append(f"leaw ${fim}, %A")     
            commands.append("jmp")  
            commands.append("nop")       
            
            
            commands.append(f"{neg}:")  
            
            commands.append("leaw $65535, %A")  
            commands.append("movw %A, %D") 
            commands.append("leaw $SP, %A") 
            commands.append('movw (%A), %A')
            commands.append("decw %A") 
            commands.append("decw %A") 
            commands.append("movw %D, (%A)") 

            commands.append(f"{fim}:")  
            commands.append("leaw $SP, %A")  
            commands.append("movw (%A), %D") 
            commands.append("decw %D") 
            commands.append("movw %D, (%A)") 
        

        self.commandsToFile(commands)


    def writePop(self, command, segment, index):
        self.updateUniqLabel()
        commands = []
        commands.append(self.writeHead(command) + " " + segment + " " + str(index))

        if segment == "" or segment == "constant":
            return False
        
        elif segment == "static":
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %A')
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $16, %A')
            variavel = 0 
            while variavel<index:
                commands.append('incw %A')
                variavel += 1
            commands.append('movw %D, (%A)')
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %D')
            commands.append('leaw $0, %A')
            commands.append('movw %D, (%A)')
        
        elif segment == "local":
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $32, %A')
            variavel = 0 
            while variavel<index:
                commands.append('incw %A')
                variavel += 1
            commands.append('movw %D, (%A)')
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %D')
            commands.append('leaw $0, %A')
            commands.append('movw %D, (%A)')
             
        elif segment == "argument":
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $BR, %A')
            variavel = 0 
            while variavel<index:
                commands.append('incw %A')
                variavel += 1
            commands.append('movw %D, (%A)')
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %D')
            commands.append('leaw $0, %A')
            commands.append('movw %D, (%A)')
        
        elif segment == "this":
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $1024, %A')
            variavel = 0 
            while variavel<index:
                commands.append('incw %A')
                variavel += 1
            commands.append('movw %D, (%A)')
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %D')
            commands.append('leaw $0, %A')
            commands.append('movw %D, (%A)')
        
        elif segment == "that":
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $1024, %A')
            variavel = 0 
            while variavel<index:
                commands.append('incw %A')
                variavel += 1
            commands.append('movw %D, (%A)')
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %D')
            commands.append('leaw $0, %A')
            commands.append('movw %D, (%A)')
        
        elif segment == "temp":
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $5, %A')
            variavel = 0 
            while variavel<index:
                commands.append('incw %A')
                variavel += 1
            commands.append('movw %D, (%A)')
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %D')
            commands.append('leaw $0, %A')
            commands.append('movw %D, (%A)')
        
        elif segment == "pointer":
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %A')
            commands.append('movw (%A), %D')
            commands.append('leaw $3, %A')
            variavel = 0 
            while variavel<index:
                commands.append('incw %A')
                variavel += 1
            commands.append('movw %D, (%A)')
            commands.append('leaw $0, %A')
            commands.append('movw (%A), %D') 
            commands.append('leaw $1, %A')
            commands.append('subw %D, %A, %D')
            commands.append('leaw $0, %A')
            commands.append('movw %D, (%A)')

        self.commandsToFile(commands)

    def writePush(self, command, segment, index):
        commands = []
        commands.append(self.writeHead(command + " " + segment + " " + str(index)))

        if segment == "constant":
            
            commands.append(f"leaw ${index}, %A")       # A = index
            commands.append("movw %A, %D")              # D = A = index
            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw (%A), %A")            # A = RAM[0] = 256
            commands.append("movw %D, (%A)")            # RAM[256] = D
            commands.append("incw %A")                  # A = 257
            commands.append("movw %A, %D")              # D = 257

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw %D, (%A)") 

        elif segment == "local":

            # LOCAL = RAM[1]    

            commands.append(f"leaw ${index}, %A")       # A = index
            commands.append("movw %A, %D")              # D = index
            commands.append("leaw $1, %A")              # A = 1
            commands.append("movw (%A), %A")            # A = RAM[1]
            commands.append("addw %A, %D, %D")          # D = RAM[1] + index
            commands.append("movw %D, %A")              # A = RAM[1] + index
            commands.append("movw (%A), %D")            # D = RAM[RAM[1] + index]

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw (%A), %A")            # A = RAM[0] = 256
            commands.append("movw %D, (%A)")            # RAM[256] = D
            commands.append("incw %A")                  # A = 257
            commands.append("movw %A, %D")              # D = 257 

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw %D, (%A)")            # RAM[0] = D -> RAM[0] = 257

        elif segment == "argument":

            # ARGUMENT = RAM[2]    

            commands.append(f"leaw ${index}, %A")       # A = index
            commands.append("movw %A, %D")              # D = index
            commands.append("leaw $2, %A")              # A = 2
            commands.append("movw (%A), %A")            # A = RAM[2]
            commands.append("addw %A, %D, %D")          # D = RAM[2] + index
            commands.append("movw %D, %A")              # A = RAM[2] + index
            commands.append("movw (%A), %D")            # D = RAM[RAM[2] + index]

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw (%A), %A")            # A = RAM[0] = 256
            commands.append("movw %D, (%A)")            # RAM[256] = D
            commands.append("incw %A")                  # A = 257
            commands.append("movw %A, %D")              # D = 257 

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw %D, (%A)")            # RAM[0] = D -> RAM[0] = 257

        elif segment == "this":

            # THIS = RAM[3]    

            commands.append(f"leaw ${index}, %A")       # A = index
            commands.append("movw %A, %D")              # D = index
            commands.append("leaw $3, %A")              # A = 3
            commands.append("movw (%A), %A")            # A = RAM[3]
            commands.append("addw %A, %D, %D")          # D = RAM[3] + index
            commands.append("movw %D, %A")              # A = RAM[3] + index
            commands.append("movw (%A), %D")            # D = RAM[RAM[3] + index]

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw (%A), %A")            # A = RAM[0] = 256
            commands.append("movw %D, (%A)")            # RAM[256] = D
            commands.append("incw %A")                  # A = 257
            commands.append("movw %A, %D")              # D = 257 

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw %D, (%A)")            # RAM[0] = D -> RAM[0] = 257

        elif segment == "that":

            # THAT = RAM[4]    

            commands.append(f"leaw ${index}, %A")       # A = index
            commands.append("movw %A, %D")              # D = index
            commands.append("leaw $4, %A")              # A = 4
            commands.append("movw (%A), %A")            # A = RAM[4]
            commands.append("addw %A, %D, %D")          # D = RAM[4] + index
            commands.append("movw %D, %A")              # A = RAM[4] + index
            commands.append("movw (%A), %D")            # D = RAM[RAM[4] + index]

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw (%A), %A")            # A = RAM[0] = 256
            commands.append("movw %D, (%A)")            # RAM[256] = D
            commands.append("incw %A")                  # A = 257
            commands.append("movw %A, %D")              # D = 257 

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw %D, (%A)")            # RAM[0] = D -> RAM[0] = 257
        
        elif segment == "static":

            # STATIC = RAM[16]    

            commands.append(f"leaw ${index}, %A")       # A = index
            commands.append("movw %A, %D")              # D = A = index
            commands.append("leaw $16, %A")             # A = 16
            commands.append("addw %A, %D, %D")          # D = 16 + index
            commands.append("movw %D, %A")              # A = 16 + index
            commands.append("movw (%A), %D")            # D = RAM[16 + index]

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw (%A), %A")            # A = RAM[0] = 256
            commands.append("movw %D, (%A)")            # D = RAM[256]
            commands.append("incw %A")                  # A = 257
            commands.append("movw %A, %D")              # D = 257

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw %D, (%A)")            # RAM[0] = 257

        elif segment == "temp":

            # TEMP = RAM[5]

            commands.append(f"leaw ${index}, %A")       # A = index
            commands.append("movw %A, %D")              # D = A = index
            commands.append("leaw $5, %A")              # A = 5
            commands.append("addw %A, %D, %D")          # D = 5 + index
            commands.append("movw %D, %A")              # A = 5 + index
            commands.append("movw (%A), %D")            # D = RAM[5 + index]

            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw (%A), %A")            # A = RAM[0] = 256
            commands.append("movw %D, (%A)")            # D = RAM[256]
            commands.append("incw %A")                  # A = 257
            commands.append("movw %A, %D")              # D = 257
            
            commands.append("leaw $SP, %A")             # A = SP
            commands.append("movw %D, (%A)")            # RAM[0] = 257
           
        elif segment == "pointer":
            
            # se o pointer for 0 -> this
            # se o pointer for 1 -> that

            if index == 0:

                # THIS = RAM[3]

                commands.append('leaw $3, %A')          # A = 3
                commands.append('movw (%A), %D')        # D = RAM[3]

                commands.append('leaw $SP, %A')         # A = SP
                commands.append('movw (%A), %A')        # A = RAM[0] = 256
                commands.append('movw %D, (%A)')        # D = RAM[256]
                commands.append('incw %A')              # A = 257
                commands.append('movw %A, %D')          # D = 257

                commands.append('leaw $SP, %A')         # A = SP
                commands.append('movw %D, (%A)')        # RAM[0] = 257

            elif index == 1:

                # THAT = RAM[4]

                commands.append('leaw $4, %A')          # A = 4
                commands.append('movw (%A), %D')        # D = RAM[4]

                commands.append('leaw $SP, %A')         # A = SP
                commands.append('movw (%A), %A')        # A = RAM[0] = 256
                commands.append('movw %D, (%A)')        # D = RAM[256]
                commands.append('incw %A')              # A = 257
                commands.append('movw %A, %D')          # D = 257

                commands.append('leaw $SP, %A')         # A = SP
                commands.append('movw %D, (%A)')        # RAM[0] = 257



        self.commandsToFile(commands)

    # TODO
    def writeCall(self, funcName, numArgs):
        commands = []
        commands.append(self.writeHead("call") + " " + funcName + " " + str(numArgs))

        # TODO
        # ...

        self.commandsToFile(commands)

    # TODO
    def writeReturn(self):
        commands = []
        commands.append(self.writeHead("return"))

        # TODO
        # ...

        self.commandsToFile(commands)

    # TODO
    def writeFunction(self, funcName, numLocals):
        commands = []
        commands.append(self.writeHead("func") + " " + funcName + " " + str(numLocals))

        # TODO
        # ...

        self.commandsToFile(commands)
