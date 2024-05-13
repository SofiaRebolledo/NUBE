import pandas as pd
from projects.models import INTERNET_MOVIL_CARGO_FIJO_INGRE, INTERNET_MOVIL_DEMANDA_ABONADOS, INTERNET_MOVIL_DEMANDA_TRAFICO, INTERNET_MOVIL_CARGO_FIJO_TRAFI,INTERNET_MOVIL_CARGO_FIJO_SUSCR,INTERNET_MOVIL_DEMANDA_INGRESOS

def handle_uploaded_file(file):
    # Lee todas las hojas del archivo Excel
    print("Procesa Excel")
    xls = pd.ExcelFile(file)
    print(xls)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        
        # Cuenta el número de columnas utilizadas en el DataFrame
        print(sheet_name)

        # Ejecuta diferentes acciones en función del número de columnas utilizadas
        if sheet_name == "INTERNET_MOVIL_CARGO_FIJO_INGRE": #CARGO
            #print("x")
            print("la hoja es INTERNET_MOVIL_CARGO_FIJO_INGRE")
            ingresar_INTERNET_MOVIL_CARGO_FIJO_INGRE(df)

        elif sheet_name == "INTERNET_MOVIL_DEMANDA_ABONADOS": #DEMANDA

            print("la hoja es INTERNET_MOVIL_DEMANDA_ABONADOS") 
            ingresar_INTERNET_MOVIL_DEMANDA_ABONADOS(df)

        elif sheet_name == "INTERNET_MOVIL_CARGO_FIJO_TRAFI": #CARGO
            print("la hoja es INTERNET_MOVIL_CARGO_FIJO_TRAFI")
            ingresar_INTERNET_MOVIL_CARGO_FIJO_TRAFI(df)

        elif sheet_name == "INTERNET_MOVIL_DEMANDA_TRAFICO_": #DEMANDA

            print("la hoja es INTERNET_MOVIL_DEMANDA_TRAFICO_")
            ingresar_INTERNET_MOVIL_DEMANDA_TRAFICO(df)

        elif sheet_name == "INTERNET_MOVIL_CARGO_FIJO_SUSCR": #CARGO
            print("la hoja es INTERNET_MOVIL_CARGO_FIJO_SUSCR")
            ingresar_INTERNET_MOVIL_CARGO_FIJO_SUSCR(df)

        elif sheet_name == "INTERNET_MOVIL_DEMANDA_INGRESOS": #DEMANDA

            print("la hoja es INTERNET_MOVIL_DEMANDA_INGRESOS")
            ingresar_INTERNET_MOVIL_DEMANDA_INGRESOS(df)

        else:
            # Lógica para otros casos
            print(f"El nombre de la hoja esta mal: {sheet_name}")

def ingresar_INTERNET_MOVIL_CARGO_FIJO_INGRE(df):
    # Lógica para procesar el DataFrame cuando hay 6 columnas
    for _, row in df.iterrows():
        # Crea una instancia del modelo INTERNET_MOVIL_CARGO_FIJO_INGRE
        #print(row['ANNO'],row['TRIMESTRE'],row['MES_DEL_TRIMESTRE'],row['ID_EMPRESA'],
              #row['EMPRESA'],row['ID_SEGMENTO'],row['SEGMENTO'],
              #row['ID_TERMINAL'],row['TERMINAL'],row['INGRESOS'])
        INTERNET_MOVIL_CARGO_FIJO_INGRE.objects.create(
            ANNO=int(row['ANNO']),
            TRIMESTRE= int(row['TRIMESTRE']),
            MES_DEL_TRIMESTRE=int(row['MES_DEL_TRIMESTRE']),
            ID_EMPRESA=int(row['ID_EMPRESA']),
            EMPRESA=row['EMPRESA'],
            ID_SEGMENTO=int(row['ID_SEGMENTO']),
            SEGMENTO=row['SEGMENTO'],
            ID_TERMINAL=int(row['ID_TERMINAL']),
            TERMINAL=row['TERMINAL'],
            INGRESOS=row['INGRESOS']
        )    
    print("Completado")

def ingresar_INTERNET_MOVIL_DEMANDA_ABONADOS(df):
    # Lógica para procesar el DataFrame cuando hay 11 columnas
    for _, row in df.iterrows():
        # Crea una instancia del modelo INTERNET_MOVIL_DEMANDA_ABONADOS
        INTERNET_MOVIL_DEMANDA_ABONADOS.objects.create(
            ANNO=row['ANNO'],
            TRIMESTRE=row['TRIMESTRE'],
            MES_DEL_TRIMESTRE=row['MES_DEL_TRIMESTRE'],
            ID_EMPRESA=row['ID_EMPRESA'],
            EMPRESA=row['EMPRESA'],
            ID_MODALIDAD_PAGO=row['ID_MODALIDAD_PAGO'],
            MODALIDAD_PAGO=row['MODALIDAD_PAGO'],
            ID_TERMINAL=row['ID_TERMINAL'],
            TERMINAL=row['TERMINAL'],
            ID_TECNOLOGIA=row['ID_TECNOLOGIA'],
            TECNOLOGIA=row['TECNOLOGIA'],
            CANTIDAD_ABONADOS=row['CANTIDAD_ABONADOS']
        )
    print("Completado")

def ingresar_INTERNET_MOVIL_DEMANDA_TRAFICO(df):
    # Lógica para procesar el DataFrame cuando hay 8 columnas
    for _, row in df.iterrows():
        # Crea una instancia del modelo INTERNET_MOVIL_DEMANDA_TRAFICO
        INTERNET_MOVIL_DEMANDA_TRAFICO.objects.create(
            ANNO=row['ANNO'],
            TRIMESTRE=row['TRIMESTRE'],
            MES_DEL_TRIMESTRE=row['MES_DEL_TRIMESTRE'],
            ID_EMPRESA=row['ID_EMPRESA'],
            EMPRESA=row['EMPRESA'],
            ID_MODALIDAD_PAGO=row['ID_MODALIDAD_PAGO'],
            TRAFICO=row['TRAFICO'],
            MODALIDAD_PAGO=row['MODALIDAD_PAGO']
        )
    print("Completado")

def ingresar_INTERNET_MOVIL_CARGO_FIJO_TRAFI(df):
    # Lógica para procesar el DataFrame cuando hay 7 columnas
    for _, row in df.iterrows():
        # Crea una instancia del modelo INTERNET_MOVIL_CARGO_FIJO_TRAFI
        INTERNET_MOVIL_CARGO_FIJO_TRAFI.objects.create(
            ANNO=row['ANNO'],
            TRIMESTRE=row['TRIMESTRE'],
            MES_DEL_TRIMESTRE=row['MES_DEL_TRIMESTRE'],
            ID_EMPRESA=row['ID_EMPRESA'],
            EMPRESA=row['EMPRESA'],
            TRAFICO=row['TRAFICO']
        )    
    print("Completado")    

def ingresar_INTERNET_MOVIL_CARGO_FIJO_SUSCR(df):
    for _, row in df.iterrows():
        # Crea una instancia del modelo INTERNET_MOVIL_CARGO_FIJO_SUSCR
        INTERNET_MOVIL_CARGO_FIJO_SUSCR.objects.create(
            ANNO=row['ANNO'],
            TRIMESTRE=row['TRIMESTRE'],
            MES_DEL_TRIMESTRE=row['MES_DEL_TRIMESTRE'],
            ID_SEGMENTO = row['ID_SEGMENTO'],
            SEGMENTO = row['SEGMENTO'],
            ID_EMPRESA=row['ID_EMPRESA'],
            EMPRESA=row['EMPRESA'],
            ID_TERMINAL=row['ID_TERMINAL'],
            TERMINAL=row['TERMINAL'],
            ID_TECNOLOGIA = row['ID_TECNOLOGIA'],
            TECNOLOGIA = row['TECNOLOGIA'],
            CANTIDAD_SUSCRIPTORES = row['CANTIDAD_SUSCRIPTORES']
        )
    print("Completado")

def ingresar_INTERNET_MOVIL_DEMANDA_INGRESOS(df):
    for _, row in df.iterrows():
        # Crea una instancia del modelo INTERNET_MOVIL_DEMANDA_INGRESOS
        INTERNET_MOVIL_DEMANDA_INGRESOS.objects.create(
            ANNO=row['ANNO'],
            TRIMESTRE=row['TRIMESTRE'],
            MES_DEL_TRIMESTRE=row['MES_DEL_TRIMESTRE'],
            ID_EMPRESA = row['ID_EMPRESA'],
            EMPRESA = row['EMPRESA'],
            ID_MODALIDAD_PAGO = row['ID_MODALIDAD_PAGO'],
            MODALIDAD_PAGO = row['MODALIDAD_PAGO'],
            ID_TERMINAL=row['ID_TERMINAL'],
            TERMINAL=row['TERMINAL'],
            INGRESOS=int(row['INGRESOS'])
        )
    INTERNET_MOVIL_CARGO_FIJO_INGRE.validate_unique
    print("Completado")