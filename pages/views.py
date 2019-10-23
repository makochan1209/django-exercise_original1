from django.shortcuts import render

# Create your views here.
def toppage(request):
    return render(request, 'pages/index.html', {})    # toppageという属性が呼び出されるとtemplates/index.htmlが出力される


def aboutpage(request):
    return render(request, 'pages/about/index.html', {})    # aboutpageという属性が呼び出されるとtemplates/about/index.htmlが出力される