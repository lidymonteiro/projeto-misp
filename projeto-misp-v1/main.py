import json
from commum import (
generate_instruction_s17,
randomNumber,
read_file_json, 
write_file_json, 
type_instruction_r, 
generate_instruction_r,
generate_instruction_r2,
generate_instruction_r3,
type_instruction_i,
generate_instruction_i,
generate_instruction_i2,
generate_instruction_i3,
type_instruction_j,
generate_instruction_j,
getPc,
generate_instruction_s16,
generate_instruction_s17,
generate_instruction_s28,
generate_instruction_s29,
generate_instruction_pc
)


# Le o arquivo json de input e salva os dados na variavel para ser utilizada no for
data_input = read_file_json('data/input.json')

# inicialização de variaveis auxiliares
data = []
text = {}
type = {}
conf = data_input.get('config')

# Pega cada valor hex dos dados que estavam no arquivo e faz o processamento
for hex_string in data_input.get('text'):
    trat_hex_string = hex_string[2:]

    #converte de hexa para binário => exemplo de resultado: '00000010000100010100000000100000'
    binary = ''.join(bin(int(c, 16))[2:].zfill(4) for c in trat_hex_string)
    
    #passa o valor em binário para as funções que descobrem qual o tipo de instrução
    aux_r = type_instruction_r(binary)
    aux_i = type_instruction_i(binary)
    aux_j = type_instruction_j(binary)

    #passa o valor de pc
    pc = getPc(conf)
    
    # de acordo com o tipo chama o gerador de instruções
    if aux_r.get('type') == True:
        text = generate_instruction_r(aux_r)
        text2 = generate_instruction_r2(aux_r)
        text3 = generate_instruction_r3(aux_r)
        s16 = generate_instruction_s16(conf)
        s17 = generate_instruction_s17(conf)
        s28 = generate_instruction_s28(conf)
        s29 = generate_instruction_s29(conf)
        pc = generate_instruction_pc(conf)
        regs = "{" + f'{text2}:{text3}' +  ', $16: ' + f'{s16}' + ', $17: ' + f'{s17}' + ', $28: ' + f'{s28}' + ', $29: ' + f'{s29}' + ', pc: ' + f'{pc}'
        type = 'R'
    elif aux_i.get('type') == True:
        text = generate_instruction_i(aux_i)
        text2 = generate_instruction_i2(aux_i)
        text3 = generate_instruction_i3(aux_i)
        s16 = generate_instruction_s16(conf)
        s17 = generate_instruction_s17(conf)
        s28 = generate_instruction_s28(conf)
        s29 = generate_instruction_s29(conf)
        pc = generate_instruction_pc(conf)
        regs = "{" + f'{text2}:{text3}' +  ', $16: ' + f'{s16}' + ', $17: ' + f'{s17}' + ', $28: ' + f'{s28}' + ', $29: ' + f'{s29}' + ', pc: ' + f'{pc}'
        type= 'I'
    elif aux_j.get('type') == True:
        text = generate_instruction_j(aux_j)
        s16 = generate_instruction_s16(conf)
        s17 = generate_instruction_s17(conf)
        s28 = generate_instruction_s28(conf)
        s29 = generate_instruction_s29(conf)
        pc = generate_instruction_pc(conf)
        regs = "{" + f'{text2}:{text3}' +  ', $16: ' + f'{s16}' + ', $17: ' + f'{s17}' + ', $28: ' + f'{s28}' + ', $29: ' + f'{s29}' + ', pc: ' + f'{pc}'
        type= 'J'
    else:
        text = {}
        regs = {}
        type = {}
    
    result =  {
        "type": type,
        "hex": hex_string,
        "text": text,
        "regs": regs,
        "mem": {},
        "stdout": {}
    }
    
    data.append(result)


# exibe no terminal/prompt os dados
print(data)  

# escreve os dados no arquivo
write_file_json(data)

