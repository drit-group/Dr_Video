from django.db.models import fields


class formMixin():
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.writer = self.request.user
        # self.object.save()
        return super().form_valid(form)
class Status_access():
    def dispatch(self,request,pk=None):
        if (request.user.is_admin):
            self.fields = ['title','slug','thumbnail','description','status','category']
        elif (request.user.is_writer):
            self.fields = ['title','slug','thumbnail','description','category']
        return super().dispatch(request)