from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)

from contests.models import Gallery, Contest, Photo, CurrentContest

from .serializers import (
    GallerySerializer,
    ContestSerializer,
    PhotoSerializer,
    CurrentContestSerializer,
    ContestGalleriesSerializer
)


class PhotoView(RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class GalleryRetrieveView(RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class ContestRetrieveView(RetrieveAPIView):
    # queryset = Contest.objects.all()
    serializer_class = ContestGalleriesSerializer
    lookup_field = 'year'

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = Contest.objects.filter(year=year)
        print(queryset)
        return queryset


class ContestListView(ListAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer


class CurrentContestView(ListAPIView):
    queryset = CurrentContest.objects.filter(pk=1)
    serializer_class = CurrentContestSerializer