from django.core.management.base import BaseCommand
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer

class Command(BaseCommand):
    help = 'Seed departemen data'
 
    def handle(self, *args, **kwargs):
        data_to_add = [
            {'nama_departemen': 'Departemen Pengembangan Perangkat Lunak', 'short_name': 'DepPPL', 'kode_departemen': 'TEKPL', 'divisi':1},
            {'nama_departemen': 'Departemen Infrastruktur TI ', 'short_name': 'DepInTI', 'kode_departemen': 'TEKIT', 'divisi':1},
            {'nama_departemen': 'Departemen Keamanan Siber', 'short_name': 'DepKS', 'kode_departemen': 'TEKKS', 'divisi':1},
            {'nama_departemen': 'Departemen Layanan Pelanggan', 'short_name': 'DepLP', 'kode_departemen': 'OPSLP', 'divisi':2},
            {'nama_departemen': 'Departemen Penjualan dan Pemasaran', 'short_name': 'DepSP', 'kode_departemen': 'OPSSP', 'divisi':2},
            {'nama_departemen': 'Departemen Operasional Lapangan', 'short_name': 'DepOL', 'kode_departemen': 'OPSOL', 'divisi':2},
            {'nama_departemen': 'Departemen Akuntansi dan Keuangan', 'short_name': 'DepAK', 'kode_departemen': 'FINAK', 'divisi':3},
            {'nama_departemen': 'Departemen Perencanaan dan Anggaran', 'short_name': 'DepPA', 'kode_departemen': 'FINPA', 'divisi':3},
            {'nama_departemen': 'Departemen Pajak dan Regulasi', 'short_name': 'DepPR', 'kode_departemen': 'FINPR', 'divisi':3},
            {'nama_departemen': 'Departemen Rekrutmen dan Penempatan', 'short_name': 'DepRek', 'kode_departemen': 'SDMR', 'divisi':4},
            {'nama_departemen': 'Departemen Pengembangan dan Pelatihan', 'short_name': 'DepPel', 'kode_departemen': 'SDMP', 'divisi':4},
            {'nama_departemen': 'Departemen Kompensasi dan Manfaat', 'short_name': 'DepKom', 'kode_departemen': 'SDMK', 'divisi':4},
            {'nama_departemen': 'Departemen Hukum Perusahaan', 'short_name': 'DepHP', 'kode_departemen': 'HKHP', 'divisi':5},
            {'nama_departemen': 'Departemen Kepatuhan Regulasi', 'short_name': 'DepKR', 'kode_departemen': 'HKKR', 'divisi':5},
            {'nama_departemen': 'Departemen Kekayaan Intelektual', 'short_name': 'DepKI', 'kode_departemen': 'HKKI', 'divisi':5},
        ]

        serializer = DepartemenSerializer(data=data_to_add, many=True)
        if serializer.is_valid():
            Departemen.objects.bulk_create([Departemen(**item) for item in serializer.validated_data])
            self.stdout.write(self.style.SUCCESS('Data Divisi berhasil ditambahkan secara massal.'))
        else:
            self.stdout.write(self.style.ERROR(f"Error: {serializer.errors}"))