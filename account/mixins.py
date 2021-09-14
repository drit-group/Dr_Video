class formMixin():
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.writer = self.request.user
        # self.object.save()
        return super().form_valid(form)