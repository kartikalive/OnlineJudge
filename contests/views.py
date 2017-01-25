from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import AllowAny
from contests.models import Contest, ContestProblem
from contests.serializers import ContestListSerializer, ContestDetailSerializer, ContestProblemDetailSerializer

from django.shortcuts import get_object_or_404


class ContestListAPIView(generics.ListAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestListSerializer


class ContestDetailAPIView(generics.RetrieveAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestDetailSerializer


class ContestProblemDetailAPIView(generics.RetrieveAPIView):
    queryset = ContestProblem.objects.all()
    serializer_class = ContestProblemDetailSerializer
    lookup_fields = (('contest__id', 'contest_id'), ('sort', 'problem_sort'))

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {x[0]: self.kwargs[x[1]] for x in self.lookup_fields}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj