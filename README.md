## My Chosen Role
Back End


# Catatan 
- Menambahkan user.json, dan library.json
- Data frontend untuk library dan buku mengacu pada file json di backend
- Fitur menambahkan library sudah diimplementasikan di sisi frontend

# How to run/test your part
Bagian yang dikerjakan, bisa dikerjakan via postman untuk mengirim request REST API

Bagian bagian yang dikerjakan : 
- /register (POST)
Fitur membuat akun, akun tersebut akan disimpan di user.json

cara pengujian di postman : 
1. Method post
2. URL 'http://localhost:5001/register'
3. body raw isi dengan : 
{
    "Nama" : "nama user",
    "username": "username",
    "password": "password"
}

- /login (POST)
Fitur autentikasi, autentikasi berdasarkan file user.json
cara pengujian di postman : 
1. Method POST
2. URL 'http://localhost:5001/login'
3. body raw isi dengan : 
{
    "username": "username",
    "password": "password"
}

- /api/books/ (GET)
Fitur mencari buku berdasarkan category yang ditentukan
cara pengujian di postman : 
1. Method POST
2. URL 'http://localhost:5001/api/books/'
3. pada bagian URL, tambahkan '?parameter=value', contoh pengujian di postman : 
URL : http://localhost:5001/api/books/?status=read
parameter : 
- title
- genre
- status
- author


- /api/library/<int:book_id> (PUT)
Fitur menambah library ke dalam user, sementara untuk user_idnya masih berupa hardcode
Fitur ini sudah diimplementasikan di Frontend 
1. Method PUT
2. URL '/api/library/<int:book_id>'
Contoh pengujian pada postman
http://localhost:5001/api/library/book_id



