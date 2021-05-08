if __name__ == '__main__':
    persons=['Elizabeth','Steven','Sebastian','Margaret','Svetlana','Raphael']

    domain = 'mycomapny.com'

    for person in persons:
        email = person+'@'+domain
        print('Email for\t',person,'\tis\t',email)
    else:
        print('end of the list')
