def merge(arr, lf, mid, rg):
    result = []
    left = arr[lf : mid]
    right = arr[mid : rg]
    #print(left, right, lf, mid, rg)
  # сливаем результаты
    l, r = 0, 0
    while l < len(left) and r < len(right): 
  # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
   # print(f'result_1: {result}, l: {l}, r: {r}', {right[r]})
  # Если один массив закончился раньше, чем второй, то
  # переносим оставшиеся элементы второго массива в результирующий
    #print(f'left_2: {left}')
    #print(f'right_2: {right}')
    while l < len(left): 
        result.append(left[l]) # перенеси оставшиеся элементы left в result
        l += 1 
    while r < len(right): 
        result.append(right[r]) # перенеси оставшиеся элементы right в result
        r += 1
    #print(f'result_2: {result}')
    arr[lf:rg] = result
    return arr   

def merge_sort(arr, lf, rg):
    #arr = arr[lf:rg]
    #print(f'output_1: {arr}, {lf}, {rg}')
    if rg - lf == 1:
        return arr
    mid = (rg + lf) // 2
    merge_sort(arr, lf, mid)
    #print(f'output_2: {arr}, {lf}, {rg}')
    merge_sort(arr, mid, rg)
    #print(f'output_3: {arr}, {lf}, {rg}')
    merge(arr, lf, mid, rg)

def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0 , 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
