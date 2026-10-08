# Tugas 1 – Review Matrix Multiplication

> **Mata Kuliah:** Pengolahan Citra Digital  
> **Nama:** Ridho Ahmad Irawan  
> **NIM:** F1G124049  
> **Kelas:** A

---

## 📖 Deskripsi

Tugas ini merupakan review konsep **perkalian matriks (matrix multiplication)** menggunakan Python dan library NumPy. Fokus utama tugas adalah melakukan perkalian dua buah **array 3-dimensi (3D)** dengan metode *batch matrix multiplication* menggunakan operator `@`.

Perkalian matriks adalah operasi fundamental dalam pengolahan citra digital, antara lain digunakan dalam:
- Transformasi geometri (rotasi, scaling, translasi)
- Filter konvolusi
- Komputasi jaringan saraf tiruan (CNN)

---

## 📁 Struktur File

```
Tugas 1_ Review Matrix Multiplication/
│
└── MatrixMultiplication.py   # Script utama perkalian matriks 3D
```

---

## 🧮 Penjelasan Kode

### Matriks A dan B

Dua buah array 3D berukuran `(2, 3, 3)` didefinisikan — masing-masing memiliki **2 lembar (slice)** matriks berukuran **3×3**.

**Matriks A:**
```
Lembar 1:          Lembar 2:
[1, 2, 3]          [9, 8, 7]
[4, 5, 6]          [6, 5, 4]
[7, 8, 9]          [3, 2, 1]
```

**Matriks B:**
```
Lembar 1:          Lembar 2:
[1, 3, 5]          [2, 4, 6]
[7, 9, 1]          [8, 2, 4]
[3, 5, 7]          [6, 8, 2]
```

### Operasi Perkalian

```python
C = A @ B
```

Operator `@` pada array 3D bekerja secara **per lembar (batch-wise)**:
- `C[0]` = `A[0] @ B[0]` → perkalian matriks lembar ke-1
- `C[1]` = `A[1] @ B[1]` → perkalian matriks lembar ke-2

### Hasil Perkalian

**C[0] = A[0] @ B[0]:**

| | Col 1 | Col 2 | Col 3 |
|---|---|---|---|
| **Row 1** | 24 | 36 | 28 |
| **Row 2** | 57 | 87 | 67 |
| **Row 3** | 90 | 138 | 106 |

**C[1] = A[1] @ B[1]:**

| | Col 1 | Col 2 | Col 3 |
|---|---|---|---|
| **Row 1** | 112 | 92 | 82 |
| **Row 2** | 76 | 66 | 60 |
| **Row 3** | 40 | 24 | 34 |

---

## 🛠️ Cara Menjalankan

### Prasyarat

Pastikan sudah menginstal Python dan NumPy:

```bash
pip install numpy
```

### Eksekusi

```bash
python MatrixMultiplication.py
```

### Output yang Diharapkan

```
PROSES PER LEMBAR
Lembar 1 (A[0] @ B[0]):
[[ 24  36  28]
 [ 57  87  67]
 [ 90 138 106]]

Lembar 2 (A[1] @ B[1]):
[[112  92  82]
 [ 76  66  60]
 [ 40  24  34]]

HASIL LENGKAP ARRAY 3D
[[[ 24  36  28]
  [ 57  87  67]
  [ 90 138 106]]

 [[112  92  82]
  [ 76  66  60]
  [ 40  24  34]]]
```

---

## 📚 Konsep yang Dipelajari

| Konsep | Keterangan |
|--------|-----------|
| **Matrix Multiplication** | Perkalian dua matriks menghasilkan matriks baru dengan baris dari matriks kiri dan kolom dari matriks kanan |
| **Array 3D (NumPy)** | Array multidimensi dengan tiga sumbu: lembar (depth), baris (row), dan kolom (column) |
| **Batch Matrix Multiply** | Operator `@` pada array 3D secara otomatis melakukan perkalian per lembar tanpa perlu perulangan eksplisit |
| **NumPy `np.array`** | Fungsi untuk mendefinisikan array multidimensi di Python |

---

## 🔗 Referensi

- [NumPy Documentation – numpy.matmul](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)
- [NumPy Documentation – Array indexing](https://numpy.org/doc/stable/user/basics.indexing.html)

---

<div align="center">
  <sub>Universitas Halu Oleo · Semester Ganjil 2026/2027</sub>
</div>
