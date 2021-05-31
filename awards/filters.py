import django_filters
from .models import Project
from django_filters import DateFilter, CharFilter
class ProjectFilter(django_filters.FilterSet):
  title = CharFilter(field_name='title', lookup_expr='icontains')
  class Meta:
    model = Project
    fields = 'title','user', 'pub_date'