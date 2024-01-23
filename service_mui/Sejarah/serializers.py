from rest_framework.serializers import ModelSerializer
from .models import Sejarah


class SejarahSerializer(ModelSerializer):
    class Meta:
        model = Sejarah
        fields = ['isi_sejarah']