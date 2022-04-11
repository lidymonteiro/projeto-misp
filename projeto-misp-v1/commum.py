import json
from operator import xor
import random

# função que le arquivo json
def read_file_json(path):
    with open(path) as file:
        data = json.load(file)
    return data

# funcao que escreve no arquivo json
def write_file_json(data):
    json_objeto = json.dumps(data, indent=5)
    file = open("output.json", "w")
    file.write(json_objeto)



# Variável para armazenar o valor num registrador 
#rs_value2 = 0

# funcao que recebe o binario do registrador e verifica qual o source ele corresponde         
def get_source_r(bin):
    
    sources = {
        '00000': '$0',
        '00001': '$1',
        '00010': '$2',
        '00011': '$3',
        '00100': '$4',
        '00101': '$5',
        '00110': '$6',
        '00111': '$7',
        '01000': '$8',
        '01001': '$9',
        '01010': '$10',
        '01011': '$11',
        '01100': '$12',
        '01101': '$13',
        '01110': '$14',
        '01111': '$15',
        '10000': '$16',
        '10001': '$17',
        '10010': '$18',
        '10011': '$19',
        '10100': '$20',
        '10101': '$21',
        '10110': '$22',
        '10111': '$23',
        '11000': '$24',
        '11001': '$25',
        '11010': '$26',
        '11011': '$27',
        '11100': '$28',
        '11101': '$29',
        '11110': '$30',
        '11111': '$31',
    }
    
    source = sources.get(bin, None)
    
    return source
            
# função que verifica se é do tipo r        
def type_instruction_r(bin):
    rs_value = 0
    type1 = False
    command = None
    text = {}
    aux_fn = len(bin) - 6      
    
    opcode = bin[0:6]    # 6 bits
    rs = bin[6:11]      # 5 bits
    rt = bin[11:16]     # 5 bits
    rd = bin[16:21]     # 5 bits
    #sh = 0             # 5 bits
    fn = bin[aux_fn:]   # 6 bits
    
    if opcode == '000000' and fn == '100000':
        command = 'add'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '100001':
        command = 'addu'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '100100':
        command = 'and'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value and rd_value  
    elif opcode == '000000' and fn == '011010':
        command = 'div'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value / rd_value  
    elif opcode == '000000' and fn == '011011':
        command = 'divu'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value / rd_value  
    elif opcode == '000000' and fn == '001000':
        command = 'jr'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value
    elif opcode == '000000' and fn == '010000':
        command = 'mfhi'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '010010':
        command = 'mflo'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '011000':
        command = 'mult'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value * rd_value  
    elif opcode == '000000' and fn == '011001':
        command = 'multu'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value * rd_value
    elif opcode == '000000' and fn == '100111':
        command = 'nor'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = not (rt_value  or rd_value ) 
    elif opcode == '000000' and fn == '100101':
        command = 'or'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value or rd_value  
    elif opcode == '000000' and fn == '000000':
        command = 'sll'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '000100':
        command = 'sllv'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '101010':
        command = 'slt'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '000011':
        command = 'sra'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '000111':
        command = 'srav'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '000010':
        command = 'srl'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '000110':
        command = 'srlv'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value + rd_value  
    elif opcode == '000000' and fn == '100010':
        command = 'sub'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value - rd_value  
    elif opcode == '000000' and fn == '100011':
        command = 'subu'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value = rt_value - rd_value  
    #elif opcode == '000000' and fn == '001100':
        #command = 'syscall'
        #type1 = True
    elif opcode == '000000' and fn == '100110':
        command = 'xor'
        type1 = True
        rt_value = randomNumber()  
        rd_value = randomNumber()
        rs_value =  xor(rt_value, rd_value)   
    else:
        command = {}
    
    result = {
        'type': type1,
        'command': command,
        'rs': rs,
        'rt': rt,
        'rd': rd,
        'rs_value': rs_value,
    }
    
    return result
    
# função que gera a instrução misp para o tipo r 
def generate_instruction_r(data_instruction):
    command = data_instruction.get('command')
    rs = data_instruction.get('rs')
    rt = data_instruction.get('rt')
    rd = data_instruction.get('rd')
    
    source_rs = get_source_r(rs)
    source_rt = get_source_r(rt)
    source_rd = get_source_r(rd)
    
    text = f'{command} {source_rs} {source_rt} {source_rd}'
        
    return text

def generate_instruction_r2(data_instruction):
    rs2 = data_instruction.get('rs')    
    source_rs2 = get_source_r(rs2)
    return source_rs2

def generate_instruction_r3(data_instruction):
    rs2 =  data_instruction.get('rs_value')  
    return rs2

# exemplo de codigo
def type_instruction_i(bin):
    rs_value = 0
    type2 = False
    command = None
    text = {}
    #aux_offset = len(bin) - 16      
    
    opcode = bin[:6]    # 6 bits
    rs = bin[6:11]      # 5 bits
    rt = bin[11:16]     # 5 bits
    #offset = bin[aux_offset:]   # 16 bits
    
    if opcode == '001000' :
        command = 'addi'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato  
    elif opcode == '001001':
        command = 'addiu'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato  
    elif opcode == '001100':
        command = 'andi'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value and imediato 
    elif opcode == '000111':
        command = 'bgtz'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato  
    elif opcode == '000100':
        command = 'beq'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato  
    elif opcode == '000001':
        command = 'bltz'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato  
    elif opcode == '000110':
        command = 'blez'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '000101':
        command = 'bne'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '100000':
        command = 'lb'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '100100':
        command = 'lbu'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '001111':
        command = 'lui'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '100011':
        command = 'lw'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '001101':
        command = 'ori'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '101000':
        command = 'sb'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '001010':
        command = 'slti'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '101011':
        command = 'sw'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    elif opcode == '001110':
        command = 'xori'
        type2 = True
        rt_value = randomNumber()  
        imediato = randomNumber()
        rs_value = rt_value + imediato
    else:
        command = {}
    
    result = {
        'type': type2,
        'command': command,
        'rs': rs,
        'rt': rt,
        'rs_value': rs_value,
    }

    return result

# exemplo de codigo
def generate_instruction_i(data_instruction):
    command = data_instruction.get('command')
    rs = data_instruction.get('rs')
    rt = data_instruction.get('rt')
    
    source_rs = get_source_r(rs)
    source_rt = get_source_r(rt)

    
    text = f'{command} {source_rs} {source_rt}'
        
    return text


def generate_instruction_i2(data_instruction):
    rs2 = data_instruction.get('rs')    
    source_rs2 = get_source_r(rs2)
    return source_rs2

def generate_instruction_i3(data_instruction):
    rs2 =  data_instruction.get('rs_value')  
    return rs2

# exemplo de codigo
def type_instruction_j(bin):
    type3 = False
    command = None
    text = {}
    #aux_jmp = len(bin) - 26      
    
    opcode = bin[:6]    # 6 bits
    #rs = bin[6:11]      # 5 bits
    #rt = bin[11:16]     # 5 bits
    #rd = bin[16:21]     # 5 bits
    #sh = 0             # 5 bits
    #jmp = bin[aux_jmp:]   # 6 bits
    
    if opcode == '000010' :
        command = 'j'
        type3 = True
    elif opcode == '000011':
        command = 'jal'
        type3 = True
    else:
        command = {}
    
    result = {
        'type': type3,
        'command': command,
    }

    return result

# exemplo de codigo
def generate_instruction_j(data_instruction):
    command = data_instruction.get('command')
    #rs = data_instruction.get('rs')
    
    #source_rs = get_source_r(rs)
    
    text = f'{command}'
        
    return text

def randomNumber():
        
    number = random.randrange(1, 100)
    return number
    
def getPc(conf):
    s4 = conf.get('regs').get('$4')
    s16 = conf.get('regs').get('$16')
    s17 = conf.get('regs').get('$17')
    s28 = conf.get('regs').get('$28')
    s29 = conf.get('regs').get('$29')
    pc = conf.get('regs').get('pc')

    

def generate_instruction_s16(conf):
    s16 = conf.get('regs').get('$16')  
    return s16

def generate_instruction_s17(conf):
    s17 = conf.get('regs').get('$17')  
    return s17

def generate_instruction_s28(conf):
    s28 = conf.get('regs').get('$28')  
    return s28

def generate_instruction_s29(conf):
    s29 = conf.get('regs').get('$29')  
    return s29

def generate_instruction_pc(conf):
    pc = conf.get('regs').get('pc')  + 4
    return pc