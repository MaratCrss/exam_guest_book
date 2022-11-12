from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from webapp.models import GuestBook
from webapp.forms import RecordForm


def index_view(request):
    records = GuestBook.objects.order_by('-created_at').filter(status='active')
    context = {"records": records}
    return render(request, "index.html", context)



def search_record(request):
    if request.method == "GET":
        name = request.GET.get('name')
        record = GuestBook.objects.filter(title__icontains=name)
        return render(request, 'search_by_name.html', {'records': record})

def create_record(request):
    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            email_author = form.cleaned_data.get("email_author")
            content = form.cleaned_data.get("content")
            GuestBook.objects.create(title=title, email_author=email_author, content=content)
            return redirect("index")
    return render(request, "create_record.html", {'form': form})