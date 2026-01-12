# Python App

Einfache Flask-API mit zwei Endpunkten (`/api/v1/details` und `/api/v1/healthz`), die Hostname und Zeit zurückliefert. Unten findest du kurze Schritte für lokalen Start, Docker-Image und Kubernetes-Deployment.

## Voraussetzungen
- Python 3.10+ (Dockerfile nutzt 3.14-alpine)
- pip
- (Optional) Docker & Kubernetes-Cluster (z. B. kind, k3d, Minikube)

## Lokal ausführen
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```
Die API läuft auf `http://localhost:5000`.

Nützliche Calls:
- `curl http://localhost:5000/api/v1/healthz`
- `curl http://localhost:5000/api/v1/details`

## Docker
Image bauen und lokal testen:
```bash
docker build -t python-app:local .
docker run -p 5000:5000 python-app:local
```

## Kubernetes (manifeste)
Im Ordner `k8s/` liegen Deployment, Service und Ingress.
```bash
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
kubectl apply -f k8s/ingress.yml
```
Standardmäßig lauscht das Deployment auf Port 5000, Service auf 80, Ingress auf Host `localhost`.

## Helm Chart
Ein Chart liegt unter `charts/python-app/`. Beispiel-Installation (Namespace optional anpassen):
```bash
helm upgrade --install python-app charts/python-app/ -n python-app --create-namespace
```
Werte können über `values.yaml` oder `--set` überschrieben werden.

## Endpunkte
- `GET /api/v1/healthz` – Healthcheck
- `GET /api/v1/details` – Message, Hostname, Zeitstempel