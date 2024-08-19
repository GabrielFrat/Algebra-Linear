import numpy as np

class linear_alg():
    def __init__(self) -> None:
        pass

    def sum_vector(self, *args):
        v = 0
        try:
            for i in args:
                v = v + np.array(i)
            return v
        except ValueError:
            print("Error: The function expects a list.")


    def product(self, *args):
        listResult = []
        j = 0
        
        try:
            for i in range(0, len(args[0])):
                listMult= []
                product = 1
                for i in args:
                    listMult.append(i[j])
                
                for number in listMult:
                    product *= number

                listResult.append(product)
                j += 1

            return sum(listResult)
        except ValueError:
            print("Error: The function expects a list.")
        
    def scalar(self, vector, number_scalar):
        listResult = []
        for i in range(0, len(vector)):
            listResult.append(number_scalar * vector[i])

        return listResult
    
    def RN(self, *args):
        listResult = []
        j = 0
        
        try:
            j = 0
            for i in range(0, len(args[0])):
                listMult= []
                resultado = 0
                aux = 0
                for i in args:
                    listMult.append(i[j])
                
                print(listMult)
                for numero in listMult:
                    print(numero)
                    if aux == 0:
                        aux += 1
                        resultado = numero
                    else:
                        resultado -= numero

                print(resultado)
                listResult.append(resultado)
                j += 1

            listAux = []
            for i in listResult:
                listAux.append(i ** 2)

            return sum(listAux) ** 0.5

        except ValueError:
            print("Error: The function expects a list.")
        
        
    def norm(self, vector):
        pass

# Vector sum test
algebra = linear_alg()
soma = algebra.sum_vector([2, 1], [3, 1], [4, 2])
multiplicacao = algebra.product([2, 1], [3, 1], [4, -2])
escalar = algebra.scalar([2, -5, 7, 2, -1], 2)

distancia = algebra.RN([2, -4, 1], [3, 2, -5])
print(distancia)
