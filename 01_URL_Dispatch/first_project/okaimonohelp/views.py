from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Good Bye</h1>')

#動的なページを作成
def user_page(request,user_name):
    user_name = user_name.upper()#upperは大文字に変換
    return HttpResponse(f'<h1>{user_name} page</h1>')
#user_nameを動的な値としてとる

def number_page(request, user_name, number):
    print(number, type(number))
    return HttpResponse(f'<h1>{user_name}page number = {number}</h1>')