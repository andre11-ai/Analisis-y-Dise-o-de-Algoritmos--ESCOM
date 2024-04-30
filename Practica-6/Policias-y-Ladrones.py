def policeCatchThieves(arr, n, k):
    i = 0
    l = 0
    r = 0
    res = 0
    thieves = []
    police = []

    # Store indices in lists
    while i < n:
        if arr[i] == 'P':
            police.append(i)
        elif arr[i] == 'T':
            thieves.append(i)
        i += 1

    # Track the current minimum indices of
    # thieves: thieves[l], police: police[r]
    while l < len(thieves) and r < len(police):

        # Can be caught
        if (abs(thieves[l] - police[r]) <= k):
            res += 1
            l += 1
            r += 1

        # Increment the minimum index
        elif thieves[l] < police[r]:
            l += 1
        else:
            r += 1
    # Devuelve el número de ladrones capturados
    return res


# Programa principal
if __name__ == '__main__':
    arr1 = ['P', 'T', 'T', 'P', 'T','P', 'T', 'T', 'P', 'T']
    k = 2
    n = len(arr1)
    print(("Máximo número de ladrones capturados: {}".
        format(policeCatchThieves(arr1, n, k))))

    arr2 = ['T', 'T', 'P', 'P', 'T', 'P','T', 'T', 'P', 'P', 'T', 'P']
    k = 2
    n = len(arr2)
    print(("Máximo número de ladrones capturados: {}".
        format(policeCatchThieves(arr2, n, k))))

    arr3 = ['P', 'T', 'P', 'T', 'T', 'P','T', 'T', 'P', 'P', 'T', 'P']
    k = 3
    n = len(arr3)
    print(("Máximo número de ladrones capturados: {}".
        format(policeCatchThieves(arr3, n, k))))

