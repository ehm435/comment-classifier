# Clasificador de Comentarios de Producto

Este proyecto es un clasificador de sentimientos de comentarios de productos en español. A partir de un comentario introducido por el usuario, el script predice si es **positivo**, **negativo** o **neutro**. Utiliza técnicas básicas de procesamiento de lenguaje natural (TF-IDF) y un clasificador **Naive Bayes Multinomial**, todo implementado en Python.

## 📚 Descripción

El programa entrena un modelo con un conjunto de datos en formato CSV (separado por `;`) que contiene comentarios ya clasificados. Una vez entrenado, permite introducir comentarios manualmente desde consola para clasificarlos automáticamente.

## 🧰 Tecnologías utilizadas

- Python 3.x
- scikit-learn
- pandas
- numpy

## 📦 Instalación y uso

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/ehm435/comment-classifier.git
   cd comment-classifier
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepara el dataset**:
   - Asegúrate de tener un archivo CSV (por defecto llamado `comments.csv`) con el siguiente formato:
     ```
     comentario;sentimiento
     Me encantó el producto;bueno
     No me gustó nada;malo
     Está bien, sin más;neutro
     ```

4. **Ejecuta el script**:
   ```bash
   python clasificador.py
   ```

## 💡 Ejemplo de uso

Al ejecutar el programa:

```
Cargando datos y entrenando el modelo...
Modelo entrenado con éxito.

Introduce un comentario para clasificar:
> No funciona como esperaba, muy decepcionado

Predicción: malo
```

## 🚀 Posibles mejoras

- Añadir interfaz gráfica (GUI o web)
- Guardar el modelo entrenado para no entrenar cada vez
- Soporte para otros idiomas
- Expandir el dataset con más ejemplos reales
- Usar modelos más avanzados como SVM o transformers (BERT, etc.)

---

Este proyecto es una práctica básica de NLP orientada a clasificación de texto. Ideal para reforzar conceptos de aprendizaje automático supervisado.
