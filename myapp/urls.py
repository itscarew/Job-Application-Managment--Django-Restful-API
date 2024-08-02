from django.urls import path, include
from .views import (
    JobCreateView,
    JobListView,
    JobDetailView,
    JobUpdateView,
    JobDeleteView,
    JobCategoryCreateView,
    JobCategoryListView,
    JobCategoryDetailView,
    JobCategoryUpdateView,
    JobCategoryDeleteView,
    CreateUserView,
    UserLoginView,
    UserDetailView,
    UserListView,
    UserDeleteView,
    UserUpdateView,
    CurrentUserDetailView,
    ApplicationCreateView,
    ApplicationDeleteView,
    ApplicationDetailView,
    ApplicationListView,
    ApplicationUpdateView,
    ApplicationUnderJobsDetailView,
)
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Job Application Management",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    ## job routes
    path("jobs/", JobListView.as_view(), name="job-list"),  # Read: List all Jobs
    path("jobs/create", JobCreateView.as_view(), name="job-create"),  # Create a new Job
    path(
        "jobs/<int:id>", JobDetailView.as_view(), name="job-detail"
    ),  # Read: Get details of a specific Job
    path(
        "jobs/<int:id>/update", JobUpdateView.as_view(), name="job-update"
    ),  # Update a specific Job
    path(
        "jobs/<int:id>/delete", JobDeleteView.as_view(), name="job-delete"
    ),  # Delete a specific Job
    ## job-category routes
    path("jobs-category/", JobCategoryListView.as_view(), name="job-category-list"),
    path(
        "jobs-category/create",
        JobCategoryCreateView.as_view(),
        name="job-category-create",
    ),
    path(
        "jobs-category/<int:id>",
        JobCategoryDetailView.as_view(),
        name="job-category-detail",
    ),
    path(
        "jobs-category/<int:id>/update",
        JobCategoryUpdateView.as_view(),
        name="job-category-update",
    ),
    path(
        "jobs-category/<int:id>/delete",
        JobCategoryDeleteView.as_view(),
        name="job-category-delete",
    ),
    ##Application routes
    path("jobs-application/", ApplicationListView.as_view(), name="job-application"),
    path(
        "jobs-application/create",
        ApplicationCreateView.as_view(),
        name="job-application-create",
    ),
    path(
        "jobs-application/<int:id>",
        ApplicationDetailView.as_view(),
        name="job-application-detail",
    ),
    path(
        "jobs-application/jobs/<int:job_id>",
        ApplicationUnderJobsDetailView.as_view(),
        name="job-application-jobs-detail",
    ),
    path(
        "jobs-application/<int:id>/update",
        ApplicationUpdateView.as_view(),
        name="job-application-update",
    ),
    path(
        "jobs-application/<int:id>/delete",
        ApplicationDeleteView.as_view(),
        name="job-application-delete",
    ),
    ##user routes
    path(
        "register/", CreateUserView.as_view(), name="register-user"
    ),  # register a user
    path("login/", UserLoginView.as_view(), name="login-user"),  # login a user
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:id>", UserDetailView.as_view(), name="user-detail"),
    path("users/<int:id>/update", UserUpdateView.as_view(), name="user-update"),
    path("users/<int:id>/delete", UserDeleteView.as_view(), name="user-delete"),
    path("me/", CurrentUserDetailView.as_view(), name="current-user-detail"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
