if __name__ == '__main__':

    cargo=[40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
    cargo.sort()
    cargo.reverse()

    print(cargo)
    boxCapacity=90
    box=[]
    i=0

  #  while sum(box) +cargo[i] <boxCapacity and i<len(cargo):
  #      box.append(cargo[i])
  #      i+=1

    while  i<len(cargo) and (boxCapacity - sum(box) >=min(cargo)):
        if boxCapacity-sum(box) >= cargo[i]:
            box.append(cargo[i])
        i+=1



    print("the colleted item sum is:", sum(box))
    print("the elements are:", box)