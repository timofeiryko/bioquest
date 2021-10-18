def quicksave(form):
        if form.is_valid():
            object = form.save()
            return object
        print('ERRORS!!!')
        print(form.errors)
        print('FINISHED!!!')
        return False
