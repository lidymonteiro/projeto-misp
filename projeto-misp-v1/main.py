import json
from commum import (
read_file_json, 
write_file_json, 
type_instruction_r, 
generate_instruction_r,
type_instruction_i,
generate_instruction_i,
type_instruction_j,
generate_instruction_j,
)


# Le o arquivo json de input e salva os dados na variavel para ser utilizada no for
data_input = read_file_json('data/input.json')

# inicialização de variaveis auxiliares
data = []
text = {}
type = {}

# Pega cada valor hex dos dados que estavam no arquivo e faz o processamento
for hex_string in data_input.get('text'):
    trat_hex_string = hex_string[2:]

    #converte de hexa para binário => exemplo de resultado: '00000010000100010100000000100000'
    binary = ''.join(bin(int(c, 16))[2:].zfill(4) for c in trat_hex_string)
    
    #passa o valor em binário para as funções que descobrem qual o tipo de instrução
    aux_r = type_instruction_r(binary)
    aux_i = type_instruction_i(binary)
    aux_j = type_instruction_j(binary)
    
    # de acordo com o tipo chama o gerador de instruções
    if aux_r.get('type') == True:
        text = generate_instruction_r(aux_r)
        type = 'R'
    elif aux_i.get('type') == True:
        text = generate_instruction_i(aux_i)
        type= 'I'
    elif aux_j.get('type') == True:
        text = generate_instruction_j(aux_j)
        type= 'J'
    else:
        text = {}
        type = {}
    
    result =  {
        "type": type,
        "hex": hex_string,
        "text": text,
        "regs": {},
        "mem": {},
        "stdout": {}
    }
    
    data.append(result)


# exibe no terminal/prompt os dados
print(data)  

# escreve os dados no arquivo
write_file_json(data)

