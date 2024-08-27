# Data-percakapan-bahasa-indonesia-nlp

## melakukan perubahan pada file eliana.json , tz.py
 
- edit data percakapannya berada pada eliana.json 
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
 pada kode diatas silahkan tambahkan input dari percakapan yang ditambahkan setelah ('VIRALINA', '') , ('input baru' , '')
