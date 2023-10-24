Maaş = float(input("Maaşinizi giriniz: "))
ZamOrani = float(input("Zam oranini giriniz (Yüzdelik olarak ÖRN=%30): "))

ZamliMaaş = Maaş + (Maaş / 100 * ZamOrani)
print("Zamli Maaşsiniz:", ZamliMaaş)