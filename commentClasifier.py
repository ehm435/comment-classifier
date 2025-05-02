import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Leer CSV correctamente
df = pd.read_csv('comments.csv', sep=';', names=["comment", "review"], engine="python", on_bad_lines='skip')

# Separar variables
x = df['comment']
y = df['review']

# Vectorizar texto
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(x)

# Entrenar el modelo con todo el dataset
model = MultinomialNB()
model.fit(X_vectorized, y)

# Probar comentarios manualmente
while True:
    comment = input("Escribe un comentario (o 'salir' para terminar): ")
    if comment.lower() == 'salir':
        break
    comment_vector = vectorizer.transform([comment])
    prediction = model.predict(comment_vector)
    print(f"Predicción: {prediction[0]}")