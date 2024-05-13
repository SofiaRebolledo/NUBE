import matplotlib.pyplot as plt
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

def get_plot_cargo_ingresos(x,y):
    #print(x,y)
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title("Titulo")
    plt.bar(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('x_label')
    plt.ylabel("y_label")
    plt.tight_layout()
    plt.grid(True)
    #plt.legend()
    graph = get_graph()
    return graph

def get_plot_cargo_trafico(x,y):
    #print(x,y)
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title("Titulo")
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('x_label')
    plt.ylabel("y_label")
    plt.tight_layout()
    plt.grid(True)
    #plt.legend()
    graph = get_graph()
    return graph
