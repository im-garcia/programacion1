# Ignacio Miguel García, DNI: 42469590
from funciones import generar_array, plot_histograma

array_1 = generar_array(20, "gaussian")
plot_histograma(array_1)

array_2 = generar_array(2000,"gaussian")
plot_histograma(array_2)

array_1 = generar_array(20, "uniform")
plot_histograma(array_1)

array_2 = generar_array(2000,"uniform")
plot_histograma(array_2)

array_1 = generar_array(20, "poisson")
plot_histograma(array_1)

array_2 = generar_array(2000,"poisson")
plot_histograma(array_2)
