for i in $(seq 1 10)
do
	echo | awk -v n=$i '{print n, n*n}'
done

