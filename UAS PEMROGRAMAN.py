import json

letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if letter in letters:
            index = letters.find(letter)
            new_index = index + key
            if new_index >= num_letters:
                new_index -= num_letters
            elif new_index < 0:
                new_index += num_letters
            result += letters[new_index]
        else:
            result += letter

    return result

def save_to_json(data, filename="File 1.json"):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"kunci sudah berhasil disimpan {filename}.")
    except Exception as e:
        print(f" File tidak ada: {e}")

def load_from_json(filename="File 1.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data sudah di muat {filename}:")
        print(json.dumps(data, indent=4))
        return data
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
    except Exception as e:
        print(f"File tidak ada! silahkan masukan nama file yang sudah ada: {e}")

print('')
print('Program Enkripsi Pesan Metode Caesar Cipher')
print('Pilih opsi dekripsi, enkripsi, atau muat file yang disimpan')

user_input = input('e/d/m: ').lower()
if user_input == 'e':
    print('Mode enkripsi')
    key = int(input('angka untuk di enkripsi (1 - 26): '))
    text = input('teks untuk di enkripsi: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'Teks terenkripsi: {ciphertext}')
    save_option = input('Simpan hasil ke file JSON? (y/n): ').lower()
    if save_option == 'y':
        data_to_save = {"mode": "enkripsi", "key": key, "result": ciphertext}
        save_to_json(data_to_save)

elif user_input == 'd':
    print('Mode dekripsi')
    key = int(input('angka untuk dekripsi (1 - 26): '))
    text = input('Teks untuk di dekripsi: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'Teks terdekripsi: {plaintext}')
    save_option = input('Simpan hasil ke file JSON? (y/n): ').lower()
    if save_option == 'y':
        data_to_save = {"mode": "dekripsi", "key": key, "result": plaintext}
        save_to_json(data_to_save)

elif user_input == 'm':
    print('Memuat file JSON yang disimpan...')
    loaded_data = load_from_json()
    if loaded_data:
        print(f"Mode: {loaded_data['mode']}")
        print(f"Kunci: {loaded_data['key']}")
        print(f"Hasil: {loaded_data['result']}")

else:
    print("Hanya pilih e, d, atau l!")
