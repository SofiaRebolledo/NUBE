import pandas as pd
import numpy as np
import openpyxl
from types import CellType


def abrir_excel_tabla_accesos():
    new_df = pd.read_csv('tabla_accesos.csv')  
    return new_df

def abrir_excel_tabla_trafico():
    new_df = pd.read_csv('tabla_trafico.csv')  
    return new_df

def abrir_excel_tabla_ingresos():
    new_df = pd.read_csv('tabla_ingresos.csv')  
    return new_df

