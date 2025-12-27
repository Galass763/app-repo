# Multi-stage build pour une image plus légère
FROM python:3.9-slim as builder

WORKDIR /app

# Copier les requirements et installer les dépendances
COPY src/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage final
FROM python:3.9-slim

WORKDIR /app

# Créer un utilisateur non-root
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app

# Copier les dépendances depuis le builder
COPY --from=builder /root/.local /home/appuser/.local

# Copier le code source
COPY --chown=appuser:appuser src/ .

# Variables d'environnement
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Changer vers l'utilisateur non-root
USER appuser

# Exposer le port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

# Commande de démarrage
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "60", "main:app"]
