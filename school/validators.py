from validate_docbr import CPF
import re

def invalidCpf(num_cpf):
    cpf = CPF()
    valid = cpf.validate(num_cpf)
    return not valid

def invalidName(name):
    return not name.isalpha()

def invalidPhone(phone):
    default = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    rest = re.findall(default, phone)
    return not rest