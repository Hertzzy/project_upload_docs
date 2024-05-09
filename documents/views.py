from django.http import JsonResponse

def documentos(request):
    if request.method == 'GET':
        documento = {'id': 1, 'nome': 'Guilherme'}
        return JsonResponse(documento)