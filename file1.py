#This is file1

def add_ppr_feature():
    print("Pat's feature is featuring along")

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
    add_ppr_feature()


if __name__ == '__main__':
    main()
