from django.shortcuts import render

def mainpage(request):
    return render(request, 'main_page.html')

def support(request):
    return render(request, 'support.html')

def welcomepage(request):
    return render(request, 'welcome.html')