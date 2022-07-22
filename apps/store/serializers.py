from rest_framework import serializers
# from rest_framework.response import Response

from apps.store.models import *

class FilterReviewSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data=data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer=self.parent.parent.__class__(value,context=self.context)
        return serializer.data

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields=['id','text','rating','time_pub','children','product']
        read_only_fields=('auth',)

class ReviewSerializer(serializers.ModelSerializer):

    children=RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class=FilterReviewSerializer
        model=Reviews
        fields=['id','text','rating','time_pub','children']
        read_only_fields=('auth',)


class TStoreCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Characteristics
        fields='__all__'


class TStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model=Technology
        fields=['date','name','category','brand','country','price','image','video','description','user','characteristics','reviews','slug']
        read_only_fields=('user',)

    characteristics=TStoreCharacteristicsSerializer(many=True, read_only=True)
    reviews=ReviewSerializer(many=True,read_only=True)

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields='__all__'

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields=['rating']

    
    # def create(self, validated_data):
        # rating=Reviews.objects.filter(rating=validated_data.get('rating'))
        # rs=0
        # coun=0
        # for i in rating:
        #     if i==int(i):
        #         rs+=i
        #         coun+=1
        #     res=rs/coun
        #     return res 
            
        # return Reviews.objects.create(res)


#         #   def create(self, validated_data):
# #         f = Follower.objects.filter(from_user = validated_data.get('from_user'), to_user = validated_data.get('to_user'))
# #         if len(f) == 0:
# #             if validated_data.get('from_user') != validated_data.get('to_user'):
# #                 return Follower.objects.create(**validated_data)
# #         else:
# #             return f[0]





# https://django.fun/qa/16172/