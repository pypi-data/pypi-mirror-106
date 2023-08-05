from encrypter_fernet_dr import *
import filecmp

def test_encrypter_file(orig_file='test.txt', key=None):
    file_enc, key_enc = encrypt_file(orig_file, key)
    file_dec = decrypt_file(file_enc, key_enc)
    assert filecmp.cmp(orig_file, file_dec), "Original and decrypted files are different!"