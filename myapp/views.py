from django.shortcuts import render
from .models import Job, JobCategory, Application
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializer import (
    JobSerializer,
    UserSerializer,
    LoginSerializer,
    JobCategorySerializer,
    ApplicationSerializer,
)
from rest_framework import viewsets, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create
class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    # permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Read (List and Detail)
class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # permission_classes = [IsAuthenticated]


class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


# Update
class JobUpdateView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


# Delete
class JobDeleteView(generics.DestroyAPIView):
    queryset = Job.objects.all()
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


class JobCategoryCreateView(generics.CreateAPIView):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer

    # permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Read (List and Detail)
class JobCategoryListView(generics.ListAPIView):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    # permission_classes = [IsAuthenticated]


class JobCategoryDetailView(generics.RetrieveAPIView):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


# Update
class JobCategoryUpdateView(generics.UpdateAPIView):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


# Delete
class JobCategoryDeleteView(generics.DestroyAPIView):
    queryset = JobCategory.objects.all()
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


# Read (List and Detail)
class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    # permission_classes = [IsAuthenticated]


class ApplicationDetailView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


class ApplicationUnderJobsDetailView(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        job_id = self.kwargs["job_id"]
        return Application.objects.filter(job_posting_id=job_id)


# Update
class ApplicationUpdateView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


# Delete
class ApplicationDeleteView(generics.DestroyAPIView):
    queryset = Application.objects.all()
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


##User Views
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


class CurrentUserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    # permission_classes = [IsAuthenticated]
    def get_object(self):
        # The request object is automatically available in the view
        return self.request.user


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "id"
    # permission_classes = [IsAuthenticated]
