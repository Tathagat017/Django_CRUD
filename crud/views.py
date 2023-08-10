from django.shortcuts import render


data = {}

def create(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        data[key] = value
    return render(request, 'crud/create.html')

def read(request):
    return render(request, 'crud/read.html', {'data': data})

def update(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        if key in data:
            data[key] = value
    return render(request, 'crud/update.html')

def delete(request):
    if request.method == 'POST':
        key = request.POST['key']
        if key in data:
            del data[key]
    return render(request, 'crud/delete.html')
