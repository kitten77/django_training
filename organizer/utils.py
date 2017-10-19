from django.shortcuts import render, redirect

class ObjectCreateMixing:
    form_class = None
    template_name = ''

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(request, self.template_name, {'form': bound_form})
