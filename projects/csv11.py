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

def abrir_csv_stenback_ingresos():
    new_df = pd.read_csv('Stenbacka_ingresos.csv')  
    return new_df

def abrir_csv_stenback_Abonados():
    new_df = pd.read_csv('Stenbacka_ABONADOS.csv')  
    return new_df

def abrir_csv_stenback_trafico():
    new_df = pd.read_csv('Stenbacka_Trafico.csv')  
    return new_df
