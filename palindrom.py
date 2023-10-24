def is_palindrome(sayi):
    return str(sayi) == str(sayi)[::-1]

sayi = input("Bir sayi girin: ")

if is_palindrome(sayi):
    print("Girdiğiniz sayi bir palindromdur.")
else:
    print("Girdiğiniz sayi bir palindrom değildir.")