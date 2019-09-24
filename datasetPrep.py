from dsp import load_data as l_d
from dsp import address_col as a_c
from dsp import save_file as s_f

def load_data (fileDir):
    l_d.load_data(fileDir)

def address_col(data, columns):
    a_c.address_col(data, columns)

def save_file(data, fileName, columns):
    s_f.save_file(data, fileName, columns)
