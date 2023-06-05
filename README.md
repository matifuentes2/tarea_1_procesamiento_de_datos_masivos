# Tarea 1: Procesamiento de Datos Masivos (IIC2440)

## Estudiantes

- [Matías Fuentes](https://github.com/matifuentes2)
- [Larry Uribe](https://github.com/larryuc)

## Introducción
Este repositorio documenta el trabajo realizado para la Tarea 1 en el marco del curso Procesamiento de Datos Masivos IIC2440 el primer semestre del 2023. El objetivo es identificar pares usuarios similares a partir de una [muestra de tweets](https://drive.google.com/file/d/1QZKOgZ46A_2RRsKhPNOwCTGEXP91H4Td/view), empleando [locality-sensitive hashing (LSH)](https://en.wikipedia.org/wiki/Locality-sensitive_hashing#:~:text=In%20computer%20science%2C%20locality%2Dsensitive,universe%20of%20possible%20input%20items.)para posibilitar la comparación.

Puedes encontrar una [explicación de los supuestos adoptados aquí](https://youtu.be/6UTvZlb94nA).

## Estructura del repositorio

El proyecto tiene la siguiente estructura


- `tarea.ipynb` - Notebook donde se ejecuta y describe el proceso completo. Se especifican supuestos y cada paso es 100% reproducible. Se debe ejecutar antes que los otros ya que se generan archivos requeridos en pasos posteriores. Requiere que los [datos crudos](https://drive.google.com/file/d/1QZKOgZ46A_2RRsKhPNOwCTGEXP91H4Td/view) estén presentes en el directorio raíz del repositorio.

- `hashing.py` - Contiene la implementación de SuperMinHash

- `pre_procesamiento.py` - funciones de manipulación de strings empleadas para pre procesar los datos.

- `fhs/` - Contiene los pasos intermedios del proceso de construcción de la firma de hash (generado en `tarea.ipynb`). Si el notebook no ha sido corrido el directorio estará vacío.
    - `file0.obj`
    - $\vdots$
    - `file3.obj`
- `processed_tweets/` - Contiene los pasos intermedios del proceso de pre-procesamiento de los datos (generado en `tarea.ipynb`). Si el notebook no ha sido corrido el directorio estará vacío.
    - `resumen0.obj`
    - `resumen1.obj`


