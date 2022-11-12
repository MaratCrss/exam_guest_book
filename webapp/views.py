from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.forms import RecordForm
from webapp.models import GuestBook


def index_view(request):
    records = GuestBook.objects.order_by('-created_at').filter(status='active')
    context = {"records": records}
    return render(request, "index.html", context)


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


def update_record(request, **kwargs):
    pk = kwargs['pk']
    record = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = RecordForm(initial={
            'title': record.title,
            'email_author': record.email_author,
            'content': record.content
        })
        return render(request, "update_record.html", {'form': form})
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record.title = form.cleaned_data.get("title")
            record.email_author = form.cleaned_data.get("email_author")
            record.content = form.cleaned_data.get("content")
            record.save()
            return redirect("index")
        return render(request, "update_record.html", {'form': form})


def delete_record(request, **kwargs):
    pk = kwargs['pk']
    record = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_record.html', {'record': record})
    else:
        record.delete()
        return redirect('index')


def search_record(request):
    if request.method == "GET":
        name = request.GET.get('name')
        record = GuestBook.objects.filter(title__icontains=name)
        return render(request, 'search_by_name.html', {'records': record})