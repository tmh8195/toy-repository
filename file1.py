#This is file1
def include_staging():
    print('This is a different staging table')

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
    include_staging()


if __name__ == '__main__':
    main()
