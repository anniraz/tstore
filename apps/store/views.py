from rest_framework import viewsets ,generics,filters,permissions
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import *
from .serializers import *
from .service import Paginations, ProductFilter
from .permissions import *
from apps.store.serializers import TStoreSerializer




class TStoreViewSet(viewsets.ModelViewSet):

    queryset=Technology.objects.all()
    serializer_class=TStoreSerializer
    filter_backends=(DjangoFilterBackend,filters.OrderingFilter)
    filterset_class=ProductFilter
    search_fields = ['category__title', 'name']
    # permission_classes=[IsOwnerOrReadOnly]
    # pagination_class=Paginations

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



class TStoreCharacteristics(viewsets.ModelViewSet):
    queryset=Characteristics.objects.all()
    serializer_class=TStoreCharacteristicsSerializer
    # permission_classes=[IsOwnerOrReadOnly]
    # permission_classes=[permissions.IsAuthenticated]



class ReviewCreateView(viewsets.ModelViewSet):
    queryset=Reviews.objects.all()
    serializer_class=ReviewCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(auth=self.request.user)
    
 
    # permission_classes=[permissions.IsAuthenticated]

class CategoryCreateView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers
    # permission_classes=[permissions.IsAuthenticated]
    # permission_classes=[IsOwnerOrReadOnly]
    
# def google(request):
#     return render(request,'google.html')
class RatingApiViewSet(generics.ListAPIView):
    # queryset=Reviews.objects.all()
    serializer_class=RatingSerializers

    def get_queryset(self):
        a=Reviews.objects.all()
        rating=self.kwargs['rating']
        rating1=Reviews.objects.filter(rating=rating)
        res=[]
        for i in rating1:
            if i==int(i):
                res.append(i)
            reslt=sum(res)/len(res)
            return Response({'rating':reslt})


        # return super().get_queryset()

    # def create(self, request, *args, **kwargs):
    #     rating=Reviews.objects.filter('rating')
    #     rs=0
    #     coun=0
    #     for i in rating:
    #             if i==int(i):
    #                 rs+=i
    #                 coun+=1
    #             res=rs/coun
    #             return res 
                
    #     # return Reviews.objects.create(res)

    #     return super().create(request, *args, **kwargs)

    





# class FollowerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Follower
#         fields = "__all__"
#         read_only_fields = ("id", 'from_user',)
    
#     def create(self, validated_data):
#         f = Follower.objects.filter(from_user = validated_data.get('from_user'), to_user = validated_data.get('to_user'))
#         if len(f) == 0:
#             if validated_data.get('from_user') != validated_data.get('to_user'):
#                 return Follower.objects.create(**validated_data)
#         else:
#             return f[0]


# class FollowerApiViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = Follower.objects.all()
#     serializer_class = FollowerSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             headers = self.get_success_headers(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#         except:
#             return Response({'error':'You can\'t follow yourself!'})
