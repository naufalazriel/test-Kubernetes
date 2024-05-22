from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.profile.models import Profile
from apps.departemen.models import Departemen
from apps.jabatan.models import Jabatan
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer
from apps.divisi.models import Divisi
from apps.divisi.serializers import DivisiSerializer
from apps.jabatan.models import Jabatan
from apps.jabatan.serializers import JabatanSerializer

class Command(BaseCommand):
    help = 'Seed user data'

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

        data_to_add = [
            {'nama_jabatan': 'Direktur Pemasaran'},
            {'nama_jabatan': 'DIrektur Teknologi'},
            {'nama_jabatan': 'Direktur Keuangan'},
        ]

        serializer = JabatanSerializer(data=data_to_add, many=True)
        if serializer.is_valid():
            Jabatan.objects.bulk_create([Jabatan(**item) for item in serializer.validated_data])
            self.stdout.write(self.style.SUCCESS('Data Jabatan berhasil ditambahkan secara massal.'))
        else:
            self.stdout.write(self.style.ERROR(f"Error: {serializer.errors}"))

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
        


        data_to_add = [
            {'username': 'nadip','password': 'nadip123','email': 'nadip@gmail.com'},
            {'username': 'nopal','password': 'nopal123','email': 'nopal@gmail.com'},
            {'username': 'jalu','password': 'jalu123','email': 'jalu@gmail.com'},
        ]
        for data in data_to_add:
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            user = User.objects.create_user(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f"User '{username}' berhasil ditambahkan"))

        data_to_add = [
            {'user':1 ,'nama_lengkap': 'nadip abcd','alamat': 'Jl Tikus no 1','kota': 'Kota Bandung','phone_number': '081274712','nik_group': '52512','nik_lokal': '95827','organisasi': 'Telkom Indonesia','is_first_login': True,'departemen': 1,'jabatan': 1},
            {'user':2 ,'nama_lengkap': 'nopal alga','alamat': 'Jl Kelinci no 2','kota': 'Kota Padang','phone_number': '081277264','nik_group': '56274','nik_lokal': '67242','organisasi': 'Pertamina','is_first_login': True,'departemen': 4,'jabatan': 2},
            {'user':3 ,'nama_lengkap': 'jalu kawani','alamat': 'Jl Harimau no 3','kota': 'Kab. Ciwidey','phone_number': '081270285','nik_group': '12631','nik_lokal': '19582','organisasi': 'PT POS Indonesia','is_first_login': True,'departemen': 7,'jabatan': 3},
        ]

        for data in data_to_add:
            user = data.get('user')
            nama_lengkap = data.get('nama_lengkap')
            alamat = data.get('alamat')
            kota = data.get('kota')
            phone_number = data.get('phone_number')
            nik_group = data.get('nik_group')
            nik_lokal = data.get('nik_lokal')
            organisasi = data.get('organisasi')
            is_first_login = data.get('is_first_login')
            departemen = data.get('departemen')
            jabatan = data.get('jabatan')

            user_obj = User.objects.get(id=user)
            departemen_obj = Departemen.objects.get(id=departemen)
            jabatan_obj = Jabatan.objects.get(id=jabatan)

            profile = Profile.objects.create(user=user_obj, nama_lengkap=nama_lengkap, alamat=alamat, kota=kota, phone_number=phone_number, nik_group=nik_group, nik_lokal=nik_lokal, organisasi=organisasi, is_first_login=is_first_login, departemen=departemen_obj, jabatan=jabatan_obj)

            self.stdout.write(self.style.SUCCESS(f"Profile '{nama_lengkap}' berhasil ditambahkan"))