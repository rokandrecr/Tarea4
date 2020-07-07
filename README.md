# Tarea4
Universidad de Costa Rica
Modelos Probabilísticos de Señales y Sistemas
Tarea 4 
Roger Castro 
B61725

Nota: Primero es importante aclarar como el archivo fue alterado levemente en la primera fila para poder ser manejando con la librería de python "pandas". Este cambio fue simplemente correr todas las filas 1 fila hacia abajo y poner una letra arriba en la primera fila por el tipo de lectura en los archivos CSV que hace pandas, donde obvia la primera fila pensando que es "texto"

1. El primer resultado que se grafica es la imagen "portadora.png" la cual es una sinuidal normal, con la frecuencia de 5kHz y un rango de variables muestreadas. Esta onda sinuidal es como se esperaba.
Luego se genera en el archivo "concatenación" se observa la señal modulada concatenada con la comparación en los mismos puntos donde los bits recibidos fluctúan, donde se ve que cuando se presentan 1´s la señal toma una forma sinuidal y con los 0´s una sinuidal inversa, emulando correctamente la modulación BPSK unitaria pedida.
2. La potencia promedio de la señal modulada generada


3-4. En las gráficas de Densidad espectral se refleja su Densidad espectral y el error correspondiente a cada SNR. Como es de esperar, los errores siempre varían debido a que el ruido no es una constante por lo que siempre genera cantidades de errores diferentes.
Es más común que los errores se presenten en los valor de SNR=-2, SNR=-1 y SNR=0 por lo que se deduce que entre más alto el valor del SNR, menos ruido presenta. Esto se debe a la forma logarítmica que presenta la potencia de la señal, por lo que cuando el SNR es negativo la relación entre la potencia del ruido y la potencia de la señal es mayor la potencia del ruido por lo que existe mayor distorsión en la señal y genera más errores
También se observa como las gráficas de las densidades espectrales siempre es tiene una forma similar, sin importar el valor del SNR. Esto tiene sentido ya que la señal es la misma, lo que cambia a esta es el ruido que presenta por lo que la onda se ve alterada

5.Al final en la gráfica BERvsSNR se muestra lo plasmado anteriormente de como los errores disminuyen conforme el BER se vuelve positivo
