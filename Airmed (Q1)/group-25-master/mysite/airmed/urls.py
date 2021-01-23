from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from users import views as user_views

urlpatterns = [
    path('', PostListView.as_view(), name='main-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('fitness/', views.fitness_page, name='fitness-page'),
    path('fitness/chest', views.chest, name='chest'),
    path('fitness/back', views.back, name='back'),
    path('fitness/legs', views.legs, name='legs'),
    path('fitness/arms', views.arms, name='arms'),
    path('fitness/chest/bench_press', user_views.bench, name='bench_press'),
    path('fitness/chest/inclined_db', user_views.inclined, name='inclined_db'),
    path('fitness/chest/cable_fly', user_views.fly, name='cable_fly'),
    path('fitness/back/bent_over_row', user_views.row, name='bent_over_row'),
    path('fitness/back/deadlift', user_views.dl, name='deadlift'),
    path('fitness/back/pullup', user_views.pulls, name='pullup'),
    path('fitness/legs/back_squat', user_views.squat, name='back_squat'),
    path('fitness/legs/lunge', user_views.lunges, name='lunge'),
    path('fitness/legs/hip_thrust', user_views.hip, name='hip_thrust'),
    path('fitness/arms/tricep_extension', user_views.tricep_e, name='tricep_extension'),
    path('fitness/arms/bicep_curl', user_views.bicep_c, name='bicep_curl'),
    path('fitness/arms/skullcrusher', user_views.skullcrush, name='skullcrusher')

]
