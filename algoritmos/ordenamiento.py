def ordenar(array):
	longitud_array=len(array) - 1
	for i in range(0, longitud_array):
		for j in range(0, longitud_array):
			if array[j]>array[j+1]:
				a=array[j]
				array[j]=array[j+1]
				array[j+1]=a

	return array

lista=[70, 10, 80, 40, 50, 90]
print(ordenar(lista))
