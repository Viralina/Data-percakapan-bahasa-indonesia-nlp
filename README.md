# Data-percakapan-bahasa-indonesia-nlp

## melakukan perubahan pada file eliana.json , tz.py
 
- edit data percakapannya pada file eliana.json 
- gunakan tz.py untuk membuat tokenizer.json dari eliana.json 
- tokenizer dibuat dengan library tokenizers 
- ketika ingin menambahkan percakapan baru pada eliana.json dan ingin membuat tokenizer nya

 ### untuk memperbarui tz.py jika memiliki input baru dalam data percakapan 
```python
 def load_conservations =(file_path)
try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        conversations = [(entry.get('YOU', ''), entry.get('ELIANA', ''), entry.get('VIRALINA', '')) for entry in data]
        print("Percakapan berhasil dimuat dari file.")
```
 pada kode diatas silahkan tambahkan input dari percakapan yang ditambahkan setelah ('VIRALINA', ' ') , ('input baru' , ' ')

### jika ada yang mau di diskusikan silahkan masuk
- grup wa https://chat.whatsapp.com/CT2bYuDHYJv1I46Ce7CcSL
- [Chat dengan saya di WhatsApp](https://wa.me/6281378066587)


untuk sekarang data percakapannya segini dulu, data percakapannya akan ditambah secara berkala .

