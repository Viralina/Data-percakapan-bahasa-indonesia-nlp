import json
import re
from tokenizers import SentencePieceBPETokenizer

# Parameter
max_sequence_len = 30
vocab_size = 6000

# <PAD> wajib pertama supaya ID 0 benar-benar padding
special_tokens = ["<PAD>", "<UNK>", "<YOU>", "<BOT>", "<EOS>"]

# Membuat dan melatih tokenizer
def create_tokenizer(texts, vocab_size=vocab_size):
    tokenizer = SentencePieceBPETokenizer(unk_token="<UNK>")
    try:
        tokenizer.train_from_iterator(
            texts,
            vocab_size=vocab_size,
            min_frequency=2,
            special_tokens=special_tokens
        )

        # Boleh diaktifkan, tapi harus pakai <PAD>, bukan [PAD]
        tokenizer.enable_padding(
            pad_id=tokenizer.token_to_id("<PAD>"),
            pad_token="<PAD>",
            length=max_sequence_len
        )

        tokenizer.save("tokenizer.json")
        print("Tokenizer berhasil dilatih dan disimpan sebagai tokenizer.json")

        print("PAD ID:", tokenizer.token_to_id("<PAD>"))
        print("UNK ID:", tokenizer.token_to_id("<UNK>"))
        print("YOU ID:", tokenizer.token_to_id("<YOU>"))
        print("BOT ID:", tokenizer.token_to_id("<BOT>"))
        print("EOS ID:", tokenizer.token_to_id("<EOS>"))

    except Exception as e:
        print(f"Terjadi kesalahan saat melatih atau menyimpan tokenizer: {e}")

    return tokenizer

# Memuat percakapan dari file JSON
def load_conversations(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        conversations = [
            (
                entry.get('YOU', ''),
                entry.get('ELIANA', ''),
                entry.get('VIRALINA', '')
            )
            for entry in data
        ]

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

# Membuat format:
# <YOU> input <BOT> jawaban_eliana <EOS>
# <YOU> input <BOT> jawaban_viralina <EOS>
def build_training_texts(conversations):
    texts = []

    for conv in conversations:
        you, eliana, viralina = conv

        if you and eliana:
            texts.append(f"<YOU> {you} <BOT> {eliana} <EOS>")

        if you and viralina:
            texts.append(f"<YOU> {you} <BOT> {viralina} <EOS>")

    return texts

# Fungsi utama
def main():
    conversations_file = 'eliana.json'

    conversations = load_conversations(conversations_file)

    if not conversations:
        print("Tidak ada percakapan yang dimuat. Pastikan file JSON berisi data yang valid.")
        return

    texts = build_training_texts(conversations)

    create_tokenizer(texts)

if __name__ == "__main__":
    main()
