# notes/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

@login_required
def note_list(request):
    note_qs = Note.objects.filter(user=request.user)  # ← 변수명 충돌 피하려고 note_qs로 사용
    return render(request, "notes/note_list.html", {"notes": note_qs})

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            n = form.save(commit=False)
            n.user = request.user
            n.save()
            from django.contrib import messages
            messages.success(request, "메모를 저장했습니다.")   # ✅ 추가
            return redirect("notes:list")
            
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form, "title": "메모 작성"})

@login_required
def note_update(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            from django.contrib import messages
            messages.success(request, "메모를 수정했습니다.")   # ✅ 추가
            return redirect("notes:list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form, "title": "메모 수정"})

@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == "POST":
        note.delete()
        from django.contrib import messages
        messages.success(request, "메모를 삭제했습니다.")   # ✅ 추가
        return redirect("notes:list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})

