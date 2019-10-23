from django.shortcuts import render

# Create your views here.
def toppage(request):
    return render(request, 'pages/index.html', {})    # toppageという属性が呼び出されるとtemplates/index.htmlが出力される