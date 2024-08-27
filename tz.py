import json
from tokenizers import SentencePieceBPETokenizer

# Parameter
max_sequence_len = 30
vocab_size = 10000

# Membuat dan melatih tokenizer
def create_tokenizer(texts, vocab_size=vocab_size):
    tokenizer = SentencePieceBPETokenizer()
    try:
        # Melatih tokenizer
        tokenizer.train_from_iterator(texts, vocab_size=vocab_size, min_frequency=2)
        tokenizer.enable_padding(length=max_sequence_len)
        # Menyimpan tokenizer ke file
        tokenizer.save("tokenizer.json")
        print("Tokenizer berhasil dilatih dan disimpan sebagai tokenizer.json")
    except Exception as e:
        print(f"Terjadi kesalahan saat melatih atau menyimpan tokenizer: {e}")
    return tokenizer

# Memuat percakapan dari file JSON
def load_conversations(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        conversations = [(entry.get('YOU', ''), entry.get('ELIANA', ''), entry.get('VIRALINA', '')) for entry in data]
        print("Percakapan berhasil dimuat dari file.")
        return conversations
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
        return []
    except json.JSONDecodeError as e:
        print(f"Terjadi kesalahan saat membaca file JSON: {e}")
        return []
    except KeyError as e:
        print(f"Key yang diharapkan tidak ditemukan: {e}")
        return []

# Fungsi utama
def main():
    conversations_file = 'eliana.json'
    
    # Memuat percakapan
    conversations = load_conversations(conversations_file)
    
    if not conversations:
        print("Tidak ada percakapan yang dimuat. Pastikan file JSON berisi data yang valid.")
        return
    
    # Menggabungkan semua teks dari percakapan
    texts = [text for conv in conversations for text in conv if text]  # Mengabaikan teks kosong
    
    # Membuat dan menyimpan tokenizer
    create_tokenizer(texts)

if __name__ == "__main__":
    main()
