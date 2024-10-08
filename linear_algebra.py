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
                
                for numero in listMult:
                    if aux == 0:
                        aux += 1
                        resultado = numero
                    else:
                        resultado -= numero

                listResult.append(resultado)
                j += 1

            listAux = []
            for i in listResult:
                listAux.append(i ** 2)

            return sum(listAux) ** 0.5

        except ValueError:
            print("Error: The function expects a list.")
        
        
    def norm(self, vector):
        try:
            listResult = []
            for i in vector:
                listResult.append(i ** 2)

            return sum(listResult) ** 0.5
        except ValueError:
            print("Error: The function expects a list.")


    def product_matrix(self, A, B):
        num_linhas_a, num_colunas_a = len(A), len(A[0])
        num_linhas_b, num_colunas_b = len(B), len(B[0])
        try:
            assert num_colunas_a == num_linhas_b
        except TypeError:
            print("The matrices must be the same size")
        result = []

        for linha in range(num_linhas_a):
            result.append([])

            for coluna in range(num_colunas_b):
                result[linha].append(0)

                for k in range(num_colunas_a):
                    result[linha][coluna] += A[linha][k] * B[k][coluna]

        return result
            
        
    def scalar_matrix(self, K, A):
        C = []
        try:
            for i in A:
                result = []
                for j in i:
                    result.append(K * j)
                C.append(result)

            return(C)
        except:
            print("Error when calculating matrix results") 

    def subtract_matrix(self, A, B):
        try:
            C = []
            num_linhas_a, num_colunas_a = len(A), len(A[0])
            num_linhas_b, num_colunas_b = len(B), len(B[0])

            for linha in range(num_linhas_a):
                result = []
                for value in range(0, len(A[linha])):
                    result.append(A[linha][value] - B[linha][value])

                C.append(result)
            
            return C
        except TypeError:
            print("Error when calculating matrix results")

    def sum_matrix(self, A, B):
        try:
            C = []
            num_linhas_a, num_colunas_a = len(A), len(A[0])
            num_linhas_b, num_colunas_b = len(B), len(B[0])

            for linha in range(num_linhas_a):
                result = []
                for value in range(0, len(A[linha])):
                    result.append(A[linha][value] + B[linha][value])

                C.append(result)
            
            return C
        except TypeError:
            print("Error when calculating matrix results")


    def det(self, matrix):
        num_linhas_a, num_colunas_a = len(matrix), len(matrix[0])

        try:
            assert num_linhas_a == num_colunas_a
        except TypeError:
            print("The matrices must be the same size")
        
        if num_linhas_a == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        else:
            for i in range(0, num_linhas_a):
                aux = matrix[i][:-1]

                for value in aux:
                    matrix[i].append(value)

        cont = 0
        list_Soma = []
        while cont != num_colunas_a:
            aux = cont
            value = 1
            for i in range(0, len(matrix)):
                x = matrix[i][aux]
                value = value * x
                aux += 1

            list_Soma.append(value)
            cont += 1

        cont = 0
        len_linha = len(matrix[0]) - 1
        while cont != num_colunas_a:
            aux = len_linha
            value = 1
            for i in range(0, len(matrix)):
                x = matrix[i][aux]
                value = value * x
                aux -= 1

            list_Soma.append(value * (-1))
            len_linha -= 1
            cont += 1


        valor = 0
        for i in list_Soma:
            valor = valor + i

        return valor

    def inverse_matrix(self, matrix):
        matriz_b = matrix


# Vector sum test
algebra = linear_alg()
soma = algebra.sum_vector([2, 1], [3, 1], [4, 2])
multiplicacao = algebra.product([2, 1], [3, 1], [4, -2])
escalar = algebra.scalar([2, -5, 7, 2, -1], 2)
distancia = algebra.RN([2, -4, 1], [3, 2, -5])
norma = algebra.norm([4, 2])

soma_matriz = algebra.product_matrix([[1, 2], [2, 1]], [[2, 4], [4, 4]])
escalar_matriz = algebra.scalar_matrix(2, [[1, 2], [1, 3]])
soma_matriz = algebra.sum_matrix([[1, 2], [2, 1], [2, 5]], [[2, 4], [4, 4], [2, 7]])
sub_matriz = algebra.subtract_matrix([[1, 2], [2, 1], [2, 5]], [[2, 4], [4, 4], [2, 7]])


determinante = algebra.det([[1, 3, 2, 5], [4, 2, 4, 2], [3, 1, 5, 1], [3, 4, 1, 9]])
print(determinante)

matriz_inversa = algebra.inverse_matrix([[1, 3], [4, 2]])