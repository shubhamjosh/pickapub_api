from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Restaurants
from .serializers import RestaurantsSerializer


# Create your views here.

# List all stocks and create
# stocks/
class RestaurantsList(APIView):
    def get(self, request):
        restaurants = Restaurants.objects.all()
        # Now serialize stocks
        serializer = RestaurantsSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self):
        pass
