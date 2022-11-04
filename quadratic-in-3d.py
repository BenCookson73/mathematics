import cmath
import numpy as np
import plotly.graph_objects as go
import numpy as np
import plotly.express as px


#3x^2 + 2x + 12
a = 3
b = 2
c = 12

def get_y(x):
    a*(x**2) + b*x + c
def get_x(y):
    return (-b + cmath.sqrt(b**2 - (4*a*(c-y))))/(a*2), (-b - cmath.sqrt(b**2 - (4*a*(c-y))))/(a*2)

def generate_data(min, max):
    data = []
    temp = [0, 0, 0, 0]

    for yi in range(min, max):
        for y in range(min, max):
            #temp  = [x, y, xi, yi]
            x1, x2 = get_x(complex(y, yi))
            data.append([x1.real, y, x1.imag, yi])
            data.append([x2.real, y, x2.imag, yi])
    return data

def plot(x, y, z, i, xlabel='x', ylabel='y', zlabel='z', ilabel='i', name='test'):
    fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=5,
        color=i,                # set color to an array/list of desired values
        colorscale='spectral',   # choose a colorscale
        opacity=1
        )
    )])
    fig.update_layout(
    margin=dict(l=20, r=20, b=20, t=20)
    )
    fig.update_scenes(
    xaxis_title_text = xlabel,
    yaxis_title_text = ylabel,
    zaxis_title_text = zlabel)
    with open('quadratic.html', 'a') as file:
        file.write(f'{fig.to_html(full_html=False, include_plotlyjs="cdn")}<hr>') #Modifiy the html file


if __name__ == '__main__':
    data = generate_data(-100,100)
    #print(data)
    x, y, xi, yi = [], [], [], []
    #print(data[:100:5])
    for dataset in data:
        x.append(dataset[0])
        y.append(dataset[1])
        xi.append(dataset[2])
        yi.append(dataset[3])
    x = np.array(x)
    y = np.array(y)
    xi = np.array(xi)
    yi = np.array(yi)
    with open('quadratic.html', 'w') as file:
        file.write('<head>\n<style>body { font-family: Verdana, sans-serif;}</style></head>')
        file.write('<h1>quadratic with complex numbers- 3x<sup>2</sup> + 2x + 12</h1><br>')
        file.write('x is the real value of the x<br>y is the real value of y<br>')
        file.write('xi is the imaginary value of x<br>yi is the imaginary value of y<hr>')

    plot(x, y, xi, yi, 'x', 'y', 'xi', 'yi', 'fig1')
    plot(x, y, yi, xi, 'x', 'y', 'yi', 'xi', 'fig2')
    plot(xi, yi, x, y, 'xi', 'yi', 'x', 'y', 'fig3')
    plot(xi, yi, y, x, 'xi', 'yi', 'y', 'x', 'fig4')
