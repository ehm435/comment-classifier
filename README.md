# 🇬🇧 English Version

# Product Comment Classifier

This project is a sentiment classifier for product comments in Spanish. Given a user-provided comment, the script predicts whether it is **positive**, **negative**, or **neutral**. It uses basic natural language processing (TF-IDF) and a **Multinomial Naive Bayes** classifier, all implemented in Python.

## 📚 Description

The program trains a model using a CSV dataset (separated by `;`) containing pre-labeled comments. Once trained, it allows manual comment input via console to classify them automatically.

## 🧰 Technologies Used

- Python 3.x
- scikit-learn
- pandas
- numpy

## 📦 Installation and Usage

1. **Clone this repository**:
   ```bash
   git clone https://github.com/ehm435/comment-classifier.git
   cd comment-classifier
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the dataset**:
   - Ensure you have a CSV file (default: `comments.csv`) formatted like this:
     ```
     comentario;sentimiento
     Me encantó el producto;bueno
     No me gustó nada;malo
     Está bien, sin más;neutro
     ```

4. **Run the script**:
   ```bash
   python clasificador.py
   ```

## 💡 Example Usage

Upon execution:

```
Loading data and training model...
Model successfully trained.

Enter a comment to classify:
> It didn't work as expected, very disappointed

Prediction: malo
```

## 🚀 Possible Improvements

- Add GUI (web or desktop)
- Save the trained model to avoid retraining
- Support more languages
- Expand dataset with real examples
- Use more advanced models like SVM or transformers (BERT, etc.)

---

This project is a basic NLP practice focused on text classification. Ideal for reinforcing supervised machine learning concepts.


---

# 🇪🇸 Versión en Español

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

