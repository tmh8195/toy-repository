#This is file1
def tell_joke():
    print('donald trump')

def add_staging():
    print('I am adding a staging table')

def karokee(song):
    print("I am singing")

def dance(move):
    print("look at me do the {}".format(move))
    print("I'm still shaking!")
    print("Your Turn!")


def main():
    print('Data Science is awesome')
    dance("Shuffle")
    karokee('Hello good bye')
    add_staging()
    tell_joke()

if __name__ == '__main__':
    main()
