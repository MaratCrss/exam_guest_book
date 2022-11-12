from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from webapp.models import GuestBook


def index_view(request):
    records = GuestBook.objects.order_by('-created_at').filter(status='active')
    context = {"records": records}
    return render(request, "index.html", context)



def search_record(request):
    if request.method == "GET":
        name = request.GET.get('name')
        record = GuestBook.objects.filter(title__icontains=name)
        return render(request, 'search_by_name.html', {'records': record})