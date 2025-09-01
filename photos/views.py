# from django.shortcuts import render
# from django.http import HttpResponse

# def photo_list(request):
#     # 아직 모델/업로드 안 붙였어도 빈 리스트로 렌더링
#     return render(request, "photos/photo_list.html", {"photos": []})

# def photo_upload(request):
#     return HttpResponse("사진 업로드 페이지(임시)")
# # Create your views here.

# photos/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm

@login_required
def photo_list(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, "photos/photo_list.html", {"photos": photos})

@login_required
def photo_upload(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            return redirect("photos:list")
    else:
        form = PhotoForm()
    return render(request, "photos/photo_form.html", {"form": form, "title":"사진 업로드"})

@login_required
def photo_delete(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id, user=request.user)
    if request.method == "POST":
        photo.delete()
        return redirect("photos:list")
    return render(request, "photos/photo_confirm_delete.html", {"photo": photo})
