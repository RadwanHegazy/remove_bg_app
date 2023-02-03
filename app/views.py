from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rembg import remove
from PIL import Image
from random import randint
import os
# Create your views here.


def index (reuqest) :
    return render(reuqest,'index.html')




def create_url (user) :
    return f'static/users/{user}.png'




@csrf_exempt
def img_process (request) :
    
    img = request.FILES['image']

    open_image = Image.open(img)

    bg_removeer = remove(open_image)


    user = request.COOKIES.get('user')
    
    if user is None :

        
        user = ''
        
        for i in range(10):user += f'{randint(0,20)}'
        
        url = create_url(user)
        
        response = HttpResponse(url)
        response.set_cookie('user',user)
    
    else :
        url = create_url(user)
        response = HttpResponse(url)

    bg_removeer.save(f"static/users/{user}.png")

    return response