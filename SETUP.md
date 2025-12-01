# Setup Guide

## Prerequisites

- Docker and Docker Compose
- Kubernetes cluster (for Kubernetes deployment)
- kubectl (for Kubernetes deployment)

## Quick Start with Docker Compose

1. Clone the repository:
   ```
   git clone <repository-url>
   cd monitoring-logging-system
   ```

2. Build and run the services:
   ```
   docker-compose up --build
   ```

3. Access the services:
   - Flask App: http://localhost:5000
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000 (admin/admin)
   - Kibana: http://localhost:5601
   - Elasticsearch: http://localhost:9200

## Kubernetes Deployment

1. Build the Flask app image:
   ```
   docker build -t flask-app:latest ./app
   ```

2. Apply Kubernetes manifests:
   ```
   kubectl apply -f k8s/
   ```

3. Access services via NodePort or LoadBalancer (adjust as needed)

## Testing

1. Visit http://localhost:5000 to generate traffic
2. Visit http://localhost:5000/error to generate error logs
3. Check metrics in Grafana
4. Explore logs in Kibana