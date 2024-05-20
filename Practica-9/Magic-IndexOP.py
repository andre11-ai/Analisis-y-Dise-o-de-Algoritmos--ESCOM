#Solucion Optimizada
def indice_magico(A, start, end):
    if start <= end:
        mid = (start + end) // 2
        if mid == A[mid]: 
            return mid
        if mid > A[mid]:  
            return indice_magico(A, mid + 1, end)
        else: 
            return indice_magico(A, start, mid - 1)
    return -1

if __name__ == "__main__":
    A = [-1, 0, 1, 2, 4, 10]
    print("Magic index", indice_magico(A, 0, len(A) - 1))