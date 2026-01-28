# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
def agaga(*nums):
    coolnumber = 0
    for lala in nums:
        coolnumber += lala**2
    print(coolnumber)

agaga(123,321,321,123,231,23,213,231,231,321,213,132,12,32,312,231,12,312,1,212,999999999999999)

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def okyay(*args):
    zillion = 0
    for numyay in args:
        zillion += abs(numyay)
    print(zillion)

okyay(-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -98132130011)
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

def Ok(pers, *args):
    print(pers + str(args))
    num = 0
    for i in args:
        num = num + i
        print(num)
Ok("Ahhhh",43,32,3,2,342,342,324,43,324,234,342,3,3,324324,3333,323,2,432,234,23,342,111111111111111111111111111111)


def googly(**kwargs):
    print("ok")
    for key, value in kwargs.items():
        print(key, key, key, key, key, key, key, key, key, key, key, key)
        print(value, value, value, value, value, value, value, value, value, value, value, value, value, value, value, value, value, value, value, value, )

googly(ok="Hi", Lala="Hi", o="Hi", k="Hi", okoo="Hi", okerf="Hi", oerfek="Hi", okeerfefr="Hi", oerererfk="Hi", okererfedfr="Hi", oererfk="Hi", okerferfrf="Hi")