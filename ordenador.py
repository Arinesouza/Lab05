class Sorter:
    def __init__(self):
        pass

    def ordene_selection(self, valores):
        n = len(valores)
        for i in range(n - 1):
          min = i
          for j in range(i + 1, n):
           if valores[j] < valores[min]:
                min = j

          if min != i:
                aux = valores[i]
                valores[i] = valores[min]
                valores[min] = aux
        return valores
        

    def ordene_insertion(self, valores):
        n = len(valores)
        for i in range(1,n):
           j=i
           while j>0 and valores[j-1]>valores[j]:
             aux = valores[j]
             valores[j] = valores[j-1]
             valores[j-1] = aux
             j = j-1
        return valores 