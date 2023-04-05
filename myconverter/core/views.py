from django.shortcuts import render, HttpResponse
# import img2pdf
# from PIL import Image
# Create your views here.





def home(request):
    if request.method == 'POST':
        img = request.FILES['img']
        pdf = img2pdf.convert(img)

        return HttpResponse(pdf, content_type='application/pdf')
    return render(request, 'home.html', {})

def j2p(request):
    if request.method == 'POST':
        img = request.FILES['img']
        im = Image.open(img)
        # im.save('Foto.png')
        response = HttpResponse(content_type="image/png")
        im.save(response, "PNG")
        return response
    return render(request, 'jpg2png.html', {})
