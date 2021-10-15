from django.http import Http404
class formMixin():
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        # self.object.save()
        return super().form_valid(form)
class Status_access():
    def dispatch(self,request,pk=None):
        if (request.user.is_superuser or request.user.is_admin):
            self.fields = ['title','slug','thumbnail','description','status','category','source']
        elif (request.user.is_writer):
            self.fields = ['title','slug','thumbnail','description','category','source']
        else:
            raise Http404
        return super().dispatch(request)