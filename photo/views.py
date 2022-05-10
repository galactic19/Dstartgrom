from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo, PhotoComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})



class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    success_url = '/'
    template_name = 'photo/update.html'
    
    
# class PhotoDetailView(DetailView):
#     model = Photo
#     template_name = 'photo/detail.html'


def detailView(request, pk):
    content = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        content.photocomment_set.create(comment=request.POST.get('comments'), author_id=request.user.id, photo_id=pk)
        content.photocomment_set.order_by('-created')

    context = {'object': content}
    return render(request, 'photo/detail.html', context)