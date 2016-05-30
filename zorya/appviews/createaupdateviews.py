# coding=utf-8
from zorya.models import StellarObject, BugTracker, ContactApplet, ObjectPhotos, ReletedType, Objects_list, Catalogues, BibCode, Source
from zorya.serializer import StellarObjectSerializer, BugTrackerSerializer, ContactAppletSerializer,\
    PhotoPutSerializer, ReletedTypePutSerializer, StellarObjectSerializer2, CatalogueSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from DjangoSettings.settings import BASE_DIR

import pdb
__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'

#Only host is updating db so only him knows secrete key, therefore csrf is not necessary
with open(BASE_DIR + '/zorya/appviews/supersecret.code','r') as s:
    sk = s.read()
    s.close()

@api_view(['POST','GET'])
def UpdateAPI(request, pk):
    if 'sk' in request.GET and request.GET['sk'] == str(sk):
        serializer = StellarObjectSerializer(StellarObject.objects.get(pk=pk), data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST','GET','PUT'])
def CreateUpdateAPI(request):
    '''
    To api sprawdza czy konkretny obiekt już istnieje,
    Każdy obiekt może znajdować się w wielu katalogach, ale każdy ma unikalne koordynaty
    W ten sposób można sprawdzać czy dany obiekt istnieje już w bazie
    Ogarnia sprawy katalogów
    Ogarnia sprawy zdjęć
    :param request:
    :return:
    '''
    # Sprawdzamy czy dane zostały przysłane
    try:
        #Prosty słownik z odpowiedziami
        response = {}
        if request.data.has_key('data'):
            data = request.data['data']
            #Sprawdzamy czy sa wystarczaj aco kompletne
            try:
                declination = data['declination']
                rightAsc = data['rightAsc']
            except:
                return Response(status=status.HTTP_412_PRECONDITION_FAILED)

            query = StellarObject.objects.all()
            SingleObject= query.filter(declination=declination,rightAsc=rightAsc)
            if SingleObject:
                # Jeśli obiekt o takich koordynatach już istnieje to powinniśmy uaktualnić dane na jego temat jeśli nie stworzyć nowy
                serializer = StellarObjectSerializer2(StellarObject.objects.get(pk=SingleObject[0].pk), data=data, partial=True, context={'request': request},)
                if serializer.is_valid():
                    serializer.save()
                    pk =  SingleObject[0].pk

                    response['data'] = 'Updated'
            else:
                serializer = StellarObjectSerializer2(StellarObject(),data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    pk = serializer.data['id']
                    response['data'] = 'Created'

            #Sprawdzamy czy zostały przesłane dane o katalogu
            if request.data.has_key('catalogue'):
                catalogue = request.data['catalogue']
                # Sprawdzamy czy obiekt jest katalogu i czy się nie powtarza
                cataloguequery = Objects_list.objects.filter(single_object=pk)
                if cataloguequery:
                    #Jeśli jest to sprawdzamy po przefiltrowanych obiektach czy jest w danym katalogue
                    if not cataloguequery.filter(object_catalogue__name=catalogue['catalogue']):
                        #Jeśli nie to tworzymy nowy wpis
                        Objects_list(object_number=catalogue['number'],single_object=SingleObject[0],object_catalogue=Catalogues.objects.get(name=catalogue['catalogue'])).save()
                        response['catalogue'] = 'Appended'
                    else:
                        #Jeśli jest to aktualizujemy jego numer
                        updatedCat = cataloguequery.get(object_catalogue__name=catalogue['catalogue'])
                        updatedCat.object_number = catalogue['number']
                        updatedCat.save()
                        response['catalogue'] = 'Updated'

                else:
                    #Jeśli nie ma to dodajemy go
                    Objects_list(object_number=catalogue['number'],single_object=SingleObject[0],object_catalogue=Catalogues.objects.get(name=catalogue['catalogue'])).save()
                    response['catalogue'] = 'Created'

            else:
                response['catalogue'] = False

            if request.data.has_key('photo'):
                photo = request.data['photo']
                # Każdy obiekt może mieć wiele zdjęć, przesyłane są w liście i musimy sprawdzić czy się nie powtarzają
                # Nie musimy, jeśli obiekt był już stworzony to api próbowało mu dopisać wcześniej zdjęcia.
                counter = 0
                for p in photo:
                    if not (ObjectPhotos.objects.filter(photo=p['photo'],ngc_object=SingleObject[0]) or  ObjectPhotos.objects.filter(photo_url=p['photo_url'],ngc_object=SingleObject[0])):
                        counter +=1
                        ObjectPhotos(name=p['name'],photo=p['photo'],photo_url=p['photo_url'],
                                     photo_thumbnail=p['photo_thumbnail'],ngc_object=SingleObject[0]).save()
                response['photo'] = 'Created %s photos' % (counter)
            else:
                response['photo'] = False

            if request.data.has_key('bibcode'):
                bibcode = request.data['bibcode']
                counter = 0
                for bib in bibcode:
                    if not SingleObject[0].bibcode.filter(name=bib):
                        BibCode(StellarObject=SingleObject[0],name=bib).save()
                        counter +=1
                response['bibcode'] = 'Added %s identifiers' % (counter)
            else:
                response['bibcode'] = False

            if request.data.has_key('source'):
                sources = request.data['source']
                counter = 0
                for source in sources:
                    if not SingleObject[0].source.filter(name=source):
                        Source(StellarObject=SingleObject[0],name=source).save()
                        counter +=1
                response['source'] = 'Added %s sources' % (counter)
            else:
                response['source'] = False

        else:
            response['data'] = False
        return Response(data=response,status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



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


class PhotoList(generics.ListAPIView):
    queryset = ObjectPhotos.objects.all()
    serializer_class = PhotoPutSerializer


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