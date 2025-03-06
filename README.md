Berikut adalah **panduan menjalankan Streamlit** untuk dashboard penyewaan sepeda. Kamu bisa menambahkan ini ke dalam `README.md`.  

---

## **📌 Cara Menjalankan Dashboard Penyewaan Sepeda dengan Streamlit**  

### **1️⃣ Pastikan Semua Dependensi Terinstal**  
Sebelum menjalankan dashboard, pastikan kamu sudah menginstal semua paket yang dibutuhkan. Jika menggunakan **file `requirements.txt`**, jalankan perintah berikut di terminal atau command prompt:  

```bash
pip install -r requirements.txt
```

Jika belum ada `requirements.txt`, kamu bisa menginstal paket secara manual:  

```bash
pip install streamlit pandas matplotlib seaborn scikit-learn
```

---

### **2️⃣ Navigasi ke Folder Proyek**  
Pastikan kamu berada di dalam folder proyek sebelum menjalankan Streamlit. Gunakan perintah berikut di terminal atau command prompt:  

```bash
cd path/ke/folder/proyek
```

Jika folder proyek berada di `C:\Users\elsa\Documents\submission\`, jalankan:  

```bash
cd C:\Users\elsa\Documents\submission\
```

---

### **3️⃣ Jalankan Streamlit**  
Setelah berada di folder proyek, jalankan aplikasi Streamlit dengan perintah berikut:  

```bash
streamlit run dashboard/dashboard.py
```

Setelah dijalankan, Streamlit akan otomatis membuka browser dengan dashboard yang sudah dibuat.

---

### **4️⃣ Jika Ingin Menghentikan Streamlit**  
Jika ingin menghentikan Streamlit, cukup tekan **`CTRL + C`** di terminal atau command prompt.  

---

Dengan mengikuti langkah-langkah di atas, kamu bisa menjalankan dashboard analisis penyewaan sepeda dengan mudah! 🚀  

> **Tambahan:** Pastikan file `dashboard.py` sudah mengarah ke lokasi `all_df.csv` yang benar (`dashboard/all_df.csv`). Jika ada error, coba cek path file yang di-load.