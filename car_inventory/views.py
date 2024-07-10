from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, CarCategory, Comment
from .forms import CommentForm, AnonymousCommentForm
# Create your views here.
def car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    comments = car.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car = car
                new_comment.user = request.user
                new_comment.save()
                return redirect('details_car', car_id = car.id)
        else:
            comment_form = AnonymousCommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car = car
                new_comment.save()
                return redirect('homepage')
    else:
        comment_form = CommentForm() if request.user.is_authenticated else AnonymousCommentForm()
    context = {
        'car': car,
        'comments': comments,
        'comment_form': comment_form,
    } 
    return render(request, 'car.html', context)