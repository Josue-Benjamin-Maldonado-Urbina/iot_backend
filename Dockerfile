# Usa imagen base oficial de Python
FROM python:3.11

# Establece directorio de trabajo
WORKDIR /app

# Copia todo el código
COPY . .

# Instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto de Gunicorn
EXPOSE 8000

# Comando de inicio (ajústalo si es necesario)
CMD ["gunicorn", "invernadero_project.invernadero_project.wsgi", "--bind", "0.0.0.0:8000"]

ENV PYTHONPATH="${PYTHONPATH}:/app/backend"

