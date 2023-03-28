from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .imageToDetail import image_to_detail

def upload(request):
    '''
    Upload image and return result.html

    Args:
        request (HttpRequest): Django request object

    Returns:
        HttpResponse: Django response object
    '''
    if request.method == 'POST' and request.FILES['image']:
        # Handle uploaded image
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        # Call image_to_detail function
        detail = image_to_detail(uploaded_file_url)
        # Pass data to template
        return render(request, 'result.html', {
            'uploaded_file_url': uploaded_file_url,
            'detail': detail,
        })
    return render(request, 'upload.html')