from zorya.models import StellarObject, BugTracker, ContactApplet, ObjectPhotos, ReletedType
from zorya.serializer import StellarObjectSerializer, BugTrackerSerializer, ContactAppletSerializer,\
    PhotoPutSerializer, ReletedTypePutSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from DjangoSettings.settings import BASE_DIR

import json
__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'

#Only host is updating db so only him knows secrete key, therefore csrf is not necessary
with open(BASE_DIR + '/zorya/appviews/supersecret.code','r') as s:
    sk = s.read()
    s.close()

@api_view(['POST','GET'])
def UpdateAPI(request, pk):
    if 'sk' in request.GET and request.GET['sk'] == str(sk):
        print 'SK OK!'
        serializer = StellarObjectSerializer(StellarObject.objects.get(pk=pk), data=request.data, partial=True, context={'request': request})
        print pk
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class BugTrackerViewAPI(generics.CreateAPIView):
    queryset = BugTracker
    serializer_class = BugTrackerSerializer

class ContactAppletViewAPI(generics.CreateAPIView):
    queryset = ContactApplet
    serializer_class = ContactAppletSerializer

@api_view(['POST','GET'])
def PhotoCreate(request):
    if "sk" in request.data and request.data["sk"] == str(sk):
        del request.data["sk"]
        serializer = PhotoPutSerializer(ObjectPhotos(),data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(request.data, status=status.HTTP_200_OK)
    else:
        return Response(status.HTTP_401_UNAUTHORIZED)

@api_view(['POST','GET'])
def TypeCreate(request):
    if "sk" in request.data and request.data["sk"] == str(sk):
        del request.data["sk"]
        serializer = ReletedTypePutSerializer(ReletedType(),data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(request.data, status=status.HTTP_200_OK)
    else:
        return Response(status.HTTP_401_UNAUTHORIZED)