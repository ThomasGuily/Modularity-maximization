def readfile(chemin):
  f=open(chemin, 'r')
  fl=f.readlines()
  matrix = []
  tmp = []
  for x in fl:
    #print(x)
    x=list(map(int, x.split())) #séparer les instances quand on rencontre un espace
    matrix.append(x)
    # print(type(x.rstrip()))
  return(matrix[0], matrix [1], matrix[2], matrix[3])

def main():
    print("python main function")
    a = readfile ("./graph1.txt")
    print (a)


if __name__ == '__main__':
    main()
