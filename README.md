## SecureTask — Demonstrasi Pipeline DevSecOps
Aplikasi manajemen tugas berbasis Command-Line Interface (CLI) sederhana yang dibangun menggunakan Python. Repositori ini mendemonstrasikan penerapan pipeline DevSecOps dasar menggunakan GitHub Actions, pytest, Bandit SAST, dan aturan Quality Gate kustom.

## Fitur Utama
- Menambahkan tugas dengan validasi input
- Menampilkan daftar tugas
- Menandai tugas yang telah selesai
- Menolak judul tugas yang kosong
- Memisahkan logika aplikasi dari interaksi CLI 

## Persyaratan Sistem
- Python 3.11 atau versi yang lebih baru
- pip

## Menjalankan Aplikasi Secara Lokal

python -m venv .venv

# Windows PowerShell:
.\\.venv\\Scripts\\Activate.ps1

# macOS/Linux:
source .venv/bin/activate

python -m pip install -r requirements.txt
python -m securetask

## Menjalankan Unit Test

python -m pytest -v

## Menjalankan SAST Scan dan Quality Gate Secara Lokal

python -m pip install -r requirements-dev.txt
python -m bandit -r securetask -f json -o bandit-report.json
python scripts/quality\_gate.py bandit-report.json

## Bandit dapat mengembalikan exit code non-nol jika ditemukan potensi kerentanan. Untuk memastikan laporan JSON tetap dievaluasi oleh Quality Gate, gunakan perintah berikut di Bash/Linux:

python -m bandit -r securetask -f json -o bandit-report.json || true
python scripts/quality\_gate.py bandit-report.json

## Pada lingkungan PowerShell, jalankan perintah Bandit dan skrip Quality Gate secara terpisah.

## Pengujian Simulasi Pemblokiran Quality Gate
Aturan Quality Gate dikonfigurasi untuk memblokir proses build jika terdapat temuan dengan kriteria HIGH severity dan HIGH confidence. Untuk menguji mekanisme ini secara lokal:
Buat file laporan simulasi:

## powershell
   Set-Content -Path gate-test.json -Value '{"results":\[{"issue\_severity":"HIGH","issue\_confidence":"HIGH","issue\_text":"Simulated finding for Quality Gate test","filename":"test\_simulation.py","line\_number":1}]}' -Encoding Ascii
  
## Jalankan skrip Quality Gate:
powershell
   python scripts/quality\_gate.py gate-test.json
   
## Periksa kode keluar (exit code):
powershell
   $LASTEXITCODE
   # Mengembalikan nilai 1 (menandakan Quality Gate gagal/FAILED)
   
## Hapus file simulasi:
powershell
   Remove-Item gate-test.json
   

## Struktur Repositori
text
securetask/
  \_\_init\_\_.py
  \_\_main\_\_.py
  cli.py
  models.py
  service.py
  validators.py
tests/
  test\_service.py
scripts/
  quality\_gate.py
.github/workflows/
  devsecops.yml
requirements.txt
requirements-dev.txt
README.md


Informasi Repositori
Repositori GitHub: [text](https://github.com/4nip/devsecops-p5-0110225074)