# from django.http import HttpResponse
# def placeholder(request): return HttpResponse("portfolio home (임시)")

# portfolio/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from .forms import AccountForm

@login_required
def account_list(request):
    accounts = Account.objects.filter(user=request.user)
    return render(request, "portfolio/account_list.html", {"accounts": accounts})

@login_required
def account_create(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            acc = form.save(commit=False)
            acc.user = request.user
            acc.save()
            return redirect("portfolio:account_list")
    else:
        form = AccountForm()
    return render(request, "portfolio/account_form.html", {"form": form, "title":"계좌 추가"})

@login_required
def account_update(request, account_id):
    acc = get_object_or_404(Account, id=account_id, user=request.user)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect("portfolio:account_list")
    else:
        form = AccountForm(instance=acc)
    return render(request, "portfolio/account_form.html", {"form": form, "title":"계좌 수정"})

@login_required
def account_delete(request, account_id):
    acc = get_object_or_404(Account, id=account_id, user=request.user)
    if request.method == "POST":
        acc.delete()
        return redirect("portfolio:account_list")
    return render(request, "portfolio/account_confirm_delete.html", {"acc": acc})
