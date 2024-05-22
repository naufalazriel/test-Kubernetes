from django.core.management.base import BaseCommand
from apps.divisi.models import Divisi
from apps.divisi.serializers import DivisiSerializer

class Command(BaseCommand):
    help = 'Seed divisi data'

    def handle(self, *args, **kwargs):
        data_to_add = [
            {'nama_divisi': 'Divisi Teknologi dan Informasi', 'short_name': 'DivTek', 'kode_divisi': 'TEK'},
            {'nama_divisi': 'Divisi Operasional', 'short_name': 'DivOps', 'kode_divisi': 'OPS'},
            {'nama_divisi': 'Divisi Keuangan ', 'short_name': 'DivKeu', 'kode_divisi': 'FIN'},
            {'nama_divisi': 'Divisi Sumber Daya Manusia', 'short_name': 'DivSDM', 'kode_divisi': 'SDM'},
            {'nama_divisi': 'Divisi Hukum dan Kepatuhan', 'short_name': 'DivHK', 'kode_divisi': 'HK'},
        ]

        serializer = DivisiSerializer(data=data_to_add, many=True)
        if serializer.is_valid():
            Divisi.objects.bulk_create([Divisi(**item) for item in serializer.validated_data])
            self.stdout.write(self.style.SUCCESS('Data Divisi berhasil ditambahkan secara massal.'))
        else:
            self.stdout.write(self.style.ERROR(f"Error: {serializer.errors}"))