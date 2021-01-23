from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CalorieForm, WeightForm, ExerciseForm
from django.contrib.auth.decorators import login_required

from .models import calorie_counter, weight_counter, exercise, cable_fly, inclined_db, bent_over_row, bicep_curl, tricep_extension, skullcrushers

from .models import calorie_counter, weight_counter, exercise, cable_fly, inclined_db, bent_over_row, deadlift, pullup, back_squat, lunge, hip_thrust


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login and update your profile!')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,

    }
    return render(request, 'users/profile.html', context)

@login_required
def calories(request):
    if request.method == "POST":
        cal_form = CalorieForm(request.POST)
        if cal_form.is_valid():
            new_calorie = cal_form.save(commit=False)
            new_calorie.user = request.user
            new_calorie.save()
            messages.success(request, f'Your daily calorie count has been updated!')
            return redirect('calorie-tracker')
    else:
        cal_form = CalorieForm(instance=request.user.profile)
        calorie_data = calorie_counter.objects.filter(user=request.user)
        day_data = []
        cal_data = []

        for data in calorie_data:
            cal_data.append(data.cal_amount)
            day_data.append(data.datepublished())
        calorie_dictionary = {}
        for count in range(len(day_data)):
            if day_data[count] in calorie_dictionary:
                calorie_dictionary[day_data[count]] += cal_data[count]
            else:
                calorie_dictionary[day_data[count]] = cal_data[count]

        day = list(calorie_dictionary.keys())
        calorie_per_day = list(calorie_dictionary.values())
        context = {
            'cal_form': cal_form,
            'calorie_dictionary': calorie_dictionary,
            'day': day,
            'calorie_per_day': calorie_per_day,
        }
    return render(request, 'users/calorie_counter.html', context)


@login_required
def weight(request):
    if request.method == "POST":
        weight_form = WeightForm(request.POST)
        if weight_form.is_valid():
            new_weight = weight_form.save(commit=False)
            new_weight.user = request.user
            new_weight.save()
            messages.success(request, f'Your daily weight count has been updated!')
            return redirect('weight-tracker')
    else:
        weight_form = WeightForm(instance=request.user.profile)
        wght_data = weight_counter.objects.filter(user=request.user)
        day_data = []
        weight_data = []

        for data in wght_data:
            weight_data.append(data.weight_amount)
            day_data.append(data.datepublished())
        weight_dictionary = {}
        for count in range(len(day_data)):
            if day_data[count] in weight_dictionary:
                weight_dictionary[day_data[count]] = weight_data[count]
            else:
                weight_dictionary[day_data[count]] = weight_data[count]

        day = list(weight_dictionary.keys())
        weight_per_day = list(weight_dictionary.values())
        context = {
            'weight_form': weight_form,
            'weight_dictionary': weight_dictionary,
            'day': day,
            'weight_per_day': weight_per_day,
        }
    return render(request, 'users/weight_tracker.html', context)

def bench(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = exercise.objects.filter(user=request.user)
        exercise_data_last = exercise.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0 
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())
        
        
        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/bench_press.html', context)


def fly(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = cable_fly.objects.filter(user=request.user)
        exercise_data_last = cable_fly.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0 
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())
        
        
        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/cable_fly.html', context)

def inclined(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = inclined_db.objects.filter(user=request.user)
        exercise_data_last = inclined_db.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0 
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())
        
        
        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/inclined_db.html', context)


def row(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = bent_over_row.objects.filter(user=request.user)
        exercise_data_last = bent_over_row.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())


        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/bent_over_row.html', context)


def bicep_c(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = bicep_curl.objects.filter(user=request.user)
        exercise_data_last = bicep_curl.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())

        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/bicep_curl.html', context)

def tricep_e(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = tricep_extension.objects.filter(user=request.user)
        exercise_data_last = tricep_extension.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())

        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/tricep_extension.html', context)

def skullcrush(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = skullcrushers.objects.filter(user=request.user)
        exercise_data_last = skullcrushers.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())

        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/skullcrusher.html', context)


def dl(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = deadlift.objects.filter(user=request.user)
        exercise_data_last = deadlift.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0 
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())
        
        
        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/deadlift.html', context)

def pulls(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = pullup.objects.filter(user=request.user)
        exercise_data_last = pullup.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0 
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())
        
        
        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/pullups.html', context)

def squat(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = back_squat.objects.filter(user=request.user)
        exercise_data_last = back_squat.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0 
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())
        
        
        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/back_squat.html', context)

def lunges(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = lunge.objects.filter(user=request.user)
        exercise_data_last = lunge.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0 
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())
        
        
        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/lunge.html', context)

def hip(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            new_exercise = exercise_form.save(commit=False)
            new_exercise.user = request.user
            new_exercise.save()
            messages.success(request, f'Your daily exercise count has been updated!')
            return redirect('fitness-page')
    else:
        exercise_form = ExerciseForm(instance=request.user.profile)
        exercise_data = hip_thrust.objects.filter(user=request.user)
        exercise_data_last = hip_thrust.objects.filter(user=request.user).last()
        if exercise_data_last is not None:
            last_set = exercise_data_last.sets
            last_rep = exercise_data_last.reps
            lastDay = exercise_data_last.datepublished()
        else:
            last_set = 0
            last_rep = 0 
            lastDay = 0
        onerepmax = []
        day = []
        for data in exercise_data:
            onerepmax.append(data.one_rep_max)
            day.append(data.datepublished())
        
        
        context = {
            'exercise_form': exercise_form,
            'day': day,
            'last_set': last_set,
            'last_rep': last_rep,
            'onerepmax': onerepmax,
            'lastDay': lastDay

        }
    return render(request, 'airmed/hip_thrust.html', context)

