class mahasiwa:
    @staticmethod
    def cetakmhs():
        print("Mahasiswa")
        
class dosen:
    @staticmethod
    def cetakdosen():
        print("Dosen")
        
class projectmhs:
    bnykmhs = 1
    def __init__ (self):
        self.nim = mahasiwa()
        self.nama = mahasiwa()
        self.prodi = mahasiwa()
        self.jenisKelamin = mahasiwa()
        self.noHp = mahasiwa()
        # self.bnykmhs += 1
        
    def get_nim(self):
        self.nim.cetakmhs()
        return "Nim: 211112317"
    def get_nama(self):
        return "Nama: Grace"
    def get_prodi(self):
        return "Jurusan: Teknik Informatika"
    def get_jk(self):
        return "Jenis Kelamin: Perempuan"
    def get_nohp(self):
        return "No HP: 0111111111"   
project = projectmhs()
print(project.get_nim())
print(project.get_nama())
print(project.get_prodi())
print(project.get_jk())
print(project.get_nohp())

print("~"*20)

class projectdosen:
    bnykdosen = 1
    def __init__ (self):
        self.nip = dosen()
        self.nama = dosen()
        self.jabatan = dosen()
        self.jenisKelamin = dosen()
        self.noHp = dosen()
        # self.bnykdosen += 1
        
    def get_nip(self):
        self.nip.cetakdosen()
        return "Nip         : 211111111"
    def get_nama(self):
        return "Nama        : Pak Albert"
    def get_jabatan(self):
        return "Jabatan     : Dosen"
    def get_jk(self):
        return "J. Kelamin  : Laki- Laki"
    def get_nohp(self):
        return "No HP       : 0111111111"
    
project = projectdosen()
print(project.get_nip())
print(project.get_nama())
print(project.get_jabatan())
print(project.get_jk())
print(project.get_nohp())

print(f"\nJumlah Pengunjung pada acara: {projectmhs.bnykmhs + projectdosen.bnykdosen}")