from django.core.paginator import Paginator
from django.shortcuts import render

def index(request):
    x_data = [x * 1 for x in range(-2500, 2500)]
    y_data = [y * y for y in range(-2500, 2500)]
    z_data = [z * z * z for z in range(-2500, 2500)]

    data = {'x': x_data, 'y': y_data, 'z': z_data}
    return render(request, 'pybo/test_graph.html', data)