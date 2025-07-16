# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.

# 98 bottles of beer on the wall, 98 bottles of beer.
# Take one down and pass it around, 97 bottles of beer on the wall.

def bottleverse(num):
    for i in range(num, 0, -1):
        print(f"{i} bootles of beer on the wall, {i} bottles of beer \n Take one down and pass it around, {i - 1 if i - 1 > 0 else 'no more'}  bottles of beer on the wall.")
       
bottleverse(5)