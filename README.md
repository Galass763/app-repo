# MyApp - Application Flask

Application Flask simple pour démonstration GitOps avec ArgoCD, Tekton et OPA Gatekeeper.

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.9+
- Docker (pour build)

### Installation Locale
```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate   # Windows

# Installer les dépendances
pip install -r src/requirements.txt

# Lancer l'application
python src/main.py
```

L'application sera accessible sur `http://localhost:8080`

### Tests
```bash
# Lancer les tests
python -m pytest tests/

# Ou avec unittest
python -m unittest discover tests/
```

## 🐳 Docker

### Build
```bash
docker build -t myapp:1.0.0 .
```

### Run
```bash
docker run -p 8080:8080 \
  -e ENVIRONMENT=development \
  -e VERSION=1.0.0 \
  myapp:1.0.0
```

## 📡 Endpoints

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/` | GET | Page d'accueil |
| `/health` | GET | Health check (liveness) |
| `/ready` | GET | Readiness check |
| `/api/info` | GET | Informations application |
| `/api/echo/<message>` | GET | Echo test |

### Exemples
```bash
# Health check
curl http://localhost:8080/health

# Info
curl http://localhost:8080/api/info

# Echo
curl http://localhost:8080/api/echo/hello
```

## 🔧 Variables d'Environnement

| Variable | Défaut | Description |
|----------|--------|-------------|
| `PORT` | 8080 | Port d'écoute |
| `ENVIRONMENT` | unknown | Environnement (dev/staging/prod) |
| `VERSION` | 1.0.0 | Version de l'application |

## 📦 Structure
```
app-repo/
├── src/                # Code source
│   ├── main.py
│   └── requirements.txt
├── tests/              # Tests unitaires
│   └── test_app.py
├── Dockerfile          # Image Docker
└── README.md
```

## 🚀 CI/CD avec Tekton

Ce repository est intégré avec Tekton Pipeline pour:
1. Build de l'image Docker
2. Tests automatisés
3. Push vers le registry
4. Mise à jour des manifests Kubernetes

## 🛡️ Sécurité

- ✅ Image Docker multi-stage
- ✅ Utilisateur non-root (UID 1000)
- ✅ Health checks configurés
- ✅ Dépendances à jour

## 📄 Licence

MIT
# app-repo
