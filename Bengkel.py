from datetime import date
import numpy
import sys
import os


class Kendaraan:
    def __init__(self, merk, jenis, tipe, tahun_pembuatan):
        self.merk = merk
        self.jenis = jenis
        self.__tipe = tipe
        self.__tahun_pembuatan = tahun_pembuatan

    def get_tipe(self):
        return self.__tipe

    def get_tahun(self):
        return self.__tahun_pembuatan


class Motor(Kendaraan):
    def __init__(self, merk, tipe, tahun_pembuatan, tgl, keluhan):
        super().__init__(merk, "Motor", tipe, tahun_pembuatan)
        self.__tgl = tgl
        self.__keluhan = keluhan

    def get_tgl(self):
        return self.__tgl

    def get_keluhan(self):
        return self.__keluhan

    def layanan(self):
        print("=== Layanan Service Motor ===")
        print("1. Ganti Oli     Rp. 50.000")
        print("2. Service Rutin Rp. 150.000 ")
        print("3. Keluhan Lain  Rp. 35000 (Biaya Jasa)")
        print("0. Kembali")


class Mobil(Kendaraan):
    def __init__(self, merk, tipe, tahun_pembuatan, tgl, keluhan):
        super().__init__(merk, "Mobil", tipe, tahun_pembuatan)
        self.__tgl = tgl
        self.__keluhan = keluhan

    def get_tgl(self):
        return self.__tgl

    def get_keluhan(self):
        return self.__keluhan

    def layanan(self):
        print("=== Layanan Service Motor ===")
        print("1. Ganti Oli     Rp. 200.000")
        print("2. Service Rutin Rp. 500.000 ")
        print("3. Keluhan Lain  Rp. 100.000 (Biaya Jasa)")
        print("0. Kembali")


class Customer:
    def __init__(self, nama, alamat, nohp):
        self.nama = nama
        self.__alamat = alamat
        self.__nohhp = nohp

    def get_alamat(self):
        return self.__alamat

    def get_nohp(self):
        return self.__nohhp


class Bengkel:
    def __init__(self, nama_bengkel):
        self.nama_bengkel = nama_bengkel
        self.antrian_motor = {}
        self.antrian_mobil = {}

    def print_motor(self):
        if len(self.antrian_motor) == 0:
            print("\nTidak Ada Antrian Motor.")

        else:
            print("Atas Nama     : ", self.antrian_motor['nama'])
            print("Tipe Kendaraan: ", self.antrian_motor['tipe'])
            print("Tanggal Masuk : ", self.antrian_motor['tangal masuk'])
            print("Keluhan       : ", self.antrian_motor['keluhan'])
            print("Total Bayar   : ", f"Rp. {self.antrian_motor['bayar']}")

    def print_mobil(self):
        if len(self.antrian_mobil) == 0:
            print("\nTidak Ada Antrian Mobil.")

        else:
            print("Atas Nama     : ", self.antrian_mobil['nama'])
            print("Tipe Kendaraan: ", self.antrian_mobil['tipe'])
            print("Tanggal Masuk : ", self.antrian_mobil['tangal masuk'])
            print("Keluhan       : ", self.antrian_mobil['keluhan'])
            print("Total Bayar   : ", f"Rp. {self.antrian_mobil['bayar']}")

    def menu(self):
        while True:
            print("=== Bengkel Otofast ===")
            print("1. Daftar Service Kendaraan")
            print("2. Cek Kendaraan")
            print("0. Keluar")
            mn = int(input("Pilihan : "))

            if mn == 1:
                print("=== Masukan Data Diri dan Data Kendaraan ===")
                nama = str(input("Nama    : "))
                nama = nama.upper()
                alamat = str(input("Alamat  : "))
                nohp = str(input("No Hp   : "))
                print("="*10)
                jenis = int(input("Kendaraan (1 = Motor | 2 = Mobil): "))
                merk = str(input("Merk Kendaraan  : "))
                tipe = str(input("Tipe Kendaraan  : "))
                tgl = date.today()
                thn = str(input("Tahun Pembuatan : "))

                if jenis == 1:
                    a = 1
                    bayar_motor = []
                    while a == 1:
                        data = Customer(nama, alamat, nohp)
                        motor = Motor(merk, tipe, thn, tgl, "None")
                        motor.layanan()
                        layanan = int(input("Jasa yg di inginkan : "))
                        if layanan == 1:
                            motor = motor = Motor(
                                merk, tipe, thn, tgl, "Ganti Oli")
                            keluhan = "Ganti Oli"
                            bayar1 = 50000
                            ulang = str(input("Apaka Ada Tambahan ?(y/n) : "))
                            if ulang == "y" or "Y":
                                bayar_motor.append(bayar1)
                                continue

                            elif ulang == "n" or "N":
                                a = 0
                                break

                        elif layanan == 2:
                            motor = motor = Motor(
                                merk, tipe, thn, tgl, "Service Rutin")
                            keluhan = "Service Rutin"
                            bayar2 = 150000
                            ulang = str(input("Apaka Ada Tambahan ?(y/n) : "))
                            if ulang == "y" or "Y":
                                bayar_motor.append(bayar2)
                                continue
                            elif ulang == "n" or "N":
                                a = 0
                                break

                        elif layanan == 3:
                            keluhan = str(input("Masukan Keluhan"))
                            motor = motor = Motor(
                                merk, tipe, thn, tgl, keluhan)
                            bayar3 = 35000
                            ulang = str(input("Apaka Ada Tambahan ?(y/n) : "))
                            if ulang == "y" or "Y":
                                bayar_motor.append(bayar3)
                                continue
                            elif ulang == "n" or "N":
                                a = 0
                                break

                        elif layanan == 0:
                            break

                        else:
                            print("Input Salah! Silakan Ulangi.")
                            continue

                    total = numpy.sum(bayar_motor)
                    keys = ['nama', 'tipe', 'tangal masuk', 'keluhan', 'bayar']
                    values = [nama, tipe, tgl, keluhan, total]
                    self.antrian_motor = dict(zip(keys, values))
                    bayar_motor.clear()
                    os.system('cls')

                if jenis == 2:
                    a = 1
                    while a == 1:
                        data = Customer(nama, alamat, nohp)
                        motor = Mobil(merk, tipe, thn, tgl, "None")
                        motor.layanan()
                        layanan = int(input("Jasa yg di iginkan : "))
                        bayar_mobil = []
                        if layanan == 1:
                            motor = motor = Mobil(
                                merk, tipe, thn, tgl, "Ganti Oli")
                            keluhan = "Ganti Oli"
                            bayar1 = 200000
                            ulang = str(input("Apaka Ada Tambahan ?(y/n)"))
                            if ulang == "y" or "Y":
                                bayar_mobil.apend(bayar1)
                                continue

                            elif ulang == "n" or "N":
                                a = a + 1
                                break

                        elif layanan == 2:
                            motor = motor = Mobil(
                                merk, tipe, thn, tgl, "Service Rutin")
                            keluhan = "Service Rutin"
                            bayar2 = 500000
                            ulang = str(input("Apaka Ada Tambahan ?(y/n)"))
                            if ulang == "y" or "Y":
                                bayar_mobil.apend(bayar2)
                                continue
                            elif ulang == "n" or "N":
                                a = a + 1
                                break

                        elif layanan == 3:
                            keluhan = str(input("Masukan Keluhan"))
                            motor = motor = Mobil(
                                merk, tipe, thn, tgl, keluhan)
                            bayar3 = 100000
                            ulang = str(input("Apaka Ada Tambahan ?(y/n)"))
                            if ulang == "y" or "Y":
                                bayar_mobil.apend(bayar3)
                                continue
                            elif ulang == "n" or "N":
                                a = a + 1
                                break

                        elif layanan == 0:
                            break

                        else:
                            print("Input Salah! Silakan Ulangi.")
                            continue

                    total = numpy.sum(bayar_mobil)
                    keys = ['nama', 'tipe', 'tangal masuk', 'keluhan', 'bayar']
                    values = [nama, tipe, tgl, keluhan, total]
                    self.antrian_mobil = dict(zip(keys, values))
                    bayar_mobil.clear()
                    os.system('cls')

            elif mn == 2:
                print("=== Cek Kendaraan")
                nama = str(input("Atas Nama : "))
                nama = nama.upper()
                jenis = int(input("Kendaraan (1 = Motor | 2 = Mobil): "))
                if jenis == 1 and nama == self.antrian_motor['nama']:
                    self.print_motor()

                elif jenis == 2 and nama == self.antrian_mobil['nama']:
                    self.print_mobil()

            elif mn == 0:
                sys.exit()


bengkel = Bengkel("Otofast")
bengkel.menu()
