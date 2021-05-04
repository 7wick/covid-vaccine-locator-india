from rest_framework import status, viewsets
from rest_framework.response import Response
from .util import get_centres


class DetailViewset(viewsets.ModelViewSet):
    def get_details(self, request):
        data = request.data
        try:
            date = data['date']
            age = int(data['age'])
            state_name = data['state_name']
            district_name = data['district_name']
        except:
            return Response(data={'message': 'Invalid input(s)'},
                            status=status.HTTP_400_BAD_REQUEST)

        response_msg = get_centres(date, age, state_name, district_name)
        return Response(data=response_msg, status=status.HTTP_200_OK)
