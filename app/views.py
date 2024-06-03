from django.shortcuts import render
from .forms import ImageForm
from .utils import download_image
from django.conf import settings

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image_url = form.cleaned_data['image_url']
            image_path = download_image(image_url)
            if image_path:
                # Construct the URL of the downloaded image
                image_url = settings.MEDIA_URL + image_path
                # Get all previously downloaded image URLs from the session
                downloaded_images = request.session.get('downloaded_images', [])
                # Add the new image URL to the list
                downloaded_images.append(image_url)
                # Save the updated list back to the session
                request.session['downloaded_images'] = downloaded_images
                return render(request, 'app/download.html', {'downloaded_images': downloaded_images})
            else:
                return render(request, 'app/home.html', {'form': form, 'error_message': 'Failed to download image.'})
    else:
        form = ImageForm()
    return render(request, 'app/home.html', {'form': form})
def delete_image(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        if image_url:
            downloaded_images = request.session.get('downloaded_images', [])
            if image_url in downloaded_images:
                downloaded_images.remove(image_url)
                request.session['downloaded_images'] = downloaded_images
                # Redirect back to the download.html page after deleting the image
                return render(request, 'app/download.html', {'downloaded_images': downloaded_images})
            else:
                return HttpResponseForbidden("Image not found in downloaded images.")
        else:
            return HttpResponseForbidden("Invalid request.")
    # If the request method is not POST, render the download.html page with current downloaded images
    downloaded_images = request.session.get('downloaded_images', [])
    return render(request, 'app/download.html', {'downloaded_images': downloaded_images})
 