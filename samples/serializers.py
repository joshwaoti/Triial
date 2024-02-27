from rest_framework import serializers
from .models import CustomerComplaints , ScheduledDirectors,MobileInformation
# from django.db.models import QuerySet
# from drf_queryfields import QueryFieldsMixin

class CustomerComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model =CustomerComplaints
        fields = '__all__'

        # paths = serializers.SerializerMethodField()

        # def get_paths(self, obj: CustomerComplaints) -> QuerySet:
        #     paths: QuerySet = SkillTreePaths.objects.filter(skill_tree_id=obj.skill_tree_id).values()
        #     return paths


class ScheduledDirectorsSerializer(serializers.ModelSerializer):
      
 class Meta:
        model =ScheduledDirectors
        fields = '__all__'

class MobileInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileInformation
        fields = '__all__'
