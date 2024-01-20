from rest_framework.serializers import ModelSerializer
from .models import Sejarah


class SejarahSerializer(ModelSerializer):
    class Meta:
        model = Sejarah
        fields = ['id_sejarah', 'isi_sejarah', 'created at']