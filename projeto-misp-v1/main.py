import json
import os
from commum import (
#generate_instruction_s17,
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
generate_instruction_s28,
generate_instruction_s29,
generate_instruction_pc,
get_name_file,
generate_dict_regs,
)



# Le o arquivo json de input e salva os dados na variavel para ser utilizada no for
diretories = os.listdir('input/')
for path_file in diretories:
    name_file = get_name_file(path_file)
    data_input = read_file_json(f'input/{path_file}')




    # inicialização de variaveis auxiliares
    data = []
    text = {}
    type = {}
    regs = {}
    conf = data_input.get('config')
    cont = 0
    value_pc = conf.get('regs').get('pc')

    # Pega cada valor hex dos dados que estavam no arquivo e faz o processamento
    for hex_string in data_input.get('text'):
        trat_hex_string = hex_string[2:]

        #converte de hexa para binário => exemplo de resultado: '00000010000100010100000000100000'
        binary = ''.join(bin(int(c, 16))[2:].zfill(4) for c in trat_hex_string)
        
        #passa o valor em binário para as funções que descobrem qual o tipo de instrução
        aux_r = type_instruction_r(binary, conf)
        aux_i = type_instruction_i(binary, conf)
        aux_j = type_instruction_j(binary)

        #passa o valor de pc
        #pc = getPc(conf)
        
        # de acordo com o tipo chama o gerador de instruções
        if aux_r.get('type') == True:
            text = generate_instruction_r(aux_r)
           
            #regs['rs'] = value_rs
            aux = aux_r
            type_aux = 'aux_r'
            regs = generate_dict_regs(conf, value_pc, cont, aux, type_aux)
            
            #s28 = generate_instruction_s28(conf)
            #s29 = generate_instruction_s29(conf)
            #pc = generate_instruction_pc(value_pc, cont)
            #regs['rs'] = value_rs
            
                #regs = "{" + f'"{rs}":{value_rs}, ' +  text_regs + ', $28: ' + f'{s28}' + ', $29: ' + f'{s29}' + ', pc: ' + f'{pc}' + "}"
            #regs.update(text_regs)
            #regs['pc'] = pc
            print(regs)
            type = 'R'
        elif aux_i.get('type') == True:
            text = generate_instruction_i(aux_i)
            aux = aux_i
            type_aux = 'aux_i'
            regs = generate_dict_regs(conf, value_pc, cont, aux, type_aux)

            #rs = generate_instruction_i2(aux_i)
            #rs_value = generate_instruction_i3(aux_i)
            #aux = aux_i
            #text_regs = generate_dict_regs(conf, value_pc, cont, aux)
            #s28 = generate_instruction_s28(conf)
            #s29 = generate_instruction_s29(conf)
            #pc = generate_instruction_pc(value_pc, cont)
            #regs = "{" + f'"{rs}":{rs_value}, ' + text_regs + ', $28: ' + f'{s28}' + ', $29: ' + f'{s29}' + ', pc: ' + f'{pc}' + "}"
            type= 'I'
        elif aux_j.get('type') == True:
            text = generate_instruction_j(aux_j)
            aux = aux_j
            #text_regs = generate_dict_regs(conf, value_pc, cont, aux)
            s28 = generate_instruction_s28(conf)
            s29 = generate_instruction_s29(conf)
            pc = generate_instruction_pc(value_pc, cont)
            #regs = "{" + "f'{rs}:{rs_value}, ' + text_regs + ', $28: ' + f'{s28}' + ', $29: ' + f'{s29}' + ', pc: ' + f'{pc}' + "}"
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
        print(f"Terminei: {hex_string}")
        cont += 1
        #value_pc = pc
        data.append(result)


    # exibe no terminal/prompt os dados
    # clprint(data)  

    # escreve os dados no arquivo
    write_file_json(data, name_file)

