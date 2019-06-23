
list_jumlah_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def kabisat(tahun):
	return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

def hari_di_bulan(tahun, bulan):

	if not 1 <= bulan <= 12:
		return "Bulan Tidak Valid"

	if bulan == 2 and kabisat(tahun) == True:
		return 29

	return list_jumlah_bulan[bulan]


# print hari_di_bulan(tahun, bulan)

print(hari_di_bulan(1998,2))