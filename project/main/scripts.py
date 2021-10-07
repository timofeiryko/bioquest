def quicksave(form):
        if form.is_valid():
            object = form.save()
            return object
        return False
