import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    #print(graph)
    #print(image_png)
    graph = graph.decode('utf-8')
    #print(graph)
    buffer.close()
    return graph

def get_plot_cargo_abonados(df,operador):
    emp_tel= pd.DataFrame(df)
    plt.switch_backend('AGG')
    ax=emp_tel.plot.bar("MES", str(operador))
    ax.set_title("ABONADOS")
    ax.margins(x=0, y=0)
    ax.xaxis.set_ticks([6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126])
    ax.xaxis.set_ticklabels(['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    plt.ylabel('Número de accesos')
    plt.xlabel('Años')
    plt.show()
    #plt.legend()
    graph = get_graph()
    return graph

def get_plot_cargo_trafico(df,operador):
    col_mov = pd.DataFrame(df)
    ax=col_mov.plot.bar("MES", str(operador))
    ax.set_title("Tráfico")
    ax.margins(x=0, y=0)
    ax.xaxis.set_ticks([6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126])
    ax.xaxis.set_ticklabels(['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    plt.ylabel('Tráfico(Megabytes)')
    plt.xlabel('Años')
    plt.show()
    graph = get_graph()
    return graph

def get_plot_cargo_ingresos(df,operador):
    col_tel = pd.DataFrame(df)
    ax=col_tel.plot.bar("MES", str(operador))
    ax.set_title("Ingresos")
    ax.margins(x=0, y=0)
    ax.xaxis.set_ticks([6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126])
    ax.xaxis.set_ticklabels(['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    plt.ylabel('Ingresos(Pesos)')
    plt.xlabel('Años')
    plt.show()
    graph = get_graph()
    return graph

def get_plot_stenback_Ingresos(df):
    plt.switch_backend('AGG')
    Stenbacka_incomes = pd.DataFrame(df)
    ax=Stenbacka_incomes.plot.bar("MES", "Stenbacka")
    ax.margins(x=0, y=0)
    ax.xaxis.set_ticks([6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126])
    ax.xaxis.set_ticklabels(['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    plt.ylabel('Stenbacka incomes')
    plt.xlabel('Years')
    plt.show()
    graph = get_graph()
    return graph

def get_plot_stenback_abonados(df):
    plt.switch_backend('AGG')
    Stenbacka_incomes = pd.DataFrame(df)
    ax=Stenbacka_incomes.plot.bar("MES", "Stenbacka")
    ax.margins(x=0, y=0)
    ax.xaxis.set_ticks([6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126])
    ax.xaxis.set_ticklabels(['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    plt.ylabel('Stenbacka accesses')
    plt.xlabel('Years')
    plt.show()
    graph = get_graph()
    return graph

def get_plot_stenback_trafico(df):
    plt.switch_backend('AGG')
    Stenbacka_traffic = pd.DataFrame(df)
    ax=Stenbacka_traffic.plot.bar("MES", "Stenbacka")
    ax.margins(x=0, y=0)
    ax.xaxis.set_ticks([6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126])
    ax.xaxis.set_ticklabels(['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
    plt.ylabel('Stenbacka Traffic')
    plt.xlabel('Years')
    plt.show()
    graph = get_graph()
    return graph
