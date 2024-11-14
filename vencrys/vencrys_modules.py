import pandas as pd
import re

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


class Data():
    def __init__(self, filename):
        self.filename = filename
        self.filetype = re.search(r"\..*", self.filename).group()
        self.df = self.__ingest__(self.filename, self.filetype)

    def __ingest__(self, filename, filetype):
        if filetype == ".csv":
            return pd.read_csv(filename)

    def list_columns(self):
        col_list = self.df.columns.tolist()
        return col_list

    def display(self):
        print(self.df)

class Encryptor():
    def __init__(self):
        aes_key = get_random_bytes(16)
        self.cipher = AES.new(aes_key, AES.MODE_OCB)

    def encrypt(self, data):
        

    def __encrypt_all__(self, data):

    def __save__(self, filename):
        pass

class Decryptor():
    def __init__(self):
        pass

    def decrypt(self, data):
        pass

    def __save__(self, filename):
        pass
