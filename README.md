# Tarea 1: Procesamiento de Datos Masivos (IIC2440)

## Estudiantes

- [Matías Fuentes](https://github.com/matifuentes2)
- [Larry Uribe](https://github.com/larryuc)

## Introducción
Este repositorio documenta el trabajo realizado para la Tarea 1 en el marco del curso Procesamiento de Datos Masivos IIC2440 el primer semestre del 2023. El objetivo es identificar pares usuarios similares a partir de una [muestra de tweets](https://drive.google.com/file/d/1QZKOgZ46A_2RRsKhPNOwCTGEXP91H4Td/view), empleando [locality-sensitive hashing (LSH)](https://en.wikipedia.org/wiki/Locality-sensitive_hashing#:~:text=In%20computer%20science%2C%20locality%2Dsensitive,universe%20of%20possible%20input%20items.)para posibilitar la comparación.

Puedes encontrar una [explicación de los supuestos adoptados aquí](https://www.youtube.com/watch?v=videoID).

## Estructura del repositorio

El proyecto tiene la siguiente estructura


- `I. Limpieza de datos.ipynb` - Notebook donde se ejecuta y describe el proceso de limpieza de datos. Se especifican supuestos y cada paso es 100% reproducible. Se debe ejecutar antes que los otros ya que se generan archivos requeridos en pasos posteriores. Requiere que los [datos crudos](https://drive.google.com/file/d/1QZKOgZ46A_2RRsKhPNOwCTGEXP91H4Td/view) estén presentes en el directorio raíz del repositorio.
- `II. Min Hashing.ipynb` - Cómputo de firmas de Hash. Se debe ejecutar antes que el III ya que se generan archivos requeridos en pasos posteriores.
- `III. Pares candidatos y autores similares.ipynb` - Obtención y pode de pares candidatos. Se identifican autores similares a partir de un threshold simple de la cantidad de tweets similares entre autores. 
- `fhs/` - Contiene los pasos intermedios del proceso de construcción de la firma de hash (generado en `II. Min Hashing.ipynb`).
    - `file0.csv`
    - $\vdots$
    - `file9.csv`


