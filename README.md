# Centralized Monitoring and Logging System

This project demonstrates a complete observability setup for a small Flask application using modern DevOps tools. It includes both Docker Compose and Kubernetes deployment options.

## 🏗️ Architecture

- **Application**: Simple Flask app exposing metrics and logs
- **Metrics**: Prometheus for collection, Grafana for visualization
- **Logs**: FluentBit for shipping, ELK Stack (Elasticsearch, Logstash, Kibana) for aggregation and visualization

## 📦 Components

### Monitoring Stack
- **Prometheus**: Scrapes metrics from the Flask app every 15 seconds
- **Grafana**: Visualizes metrics with pre-configured dashboards

### Logging Stack
- **FluentBit**: Collects container logs and forwards to Logstash
- **Logstash**: Processes and enriches logs, outputs to Elasticsearch
- **Elasticsearch**: Stores and indexes logs
- **Kibana**: Provides UI for log exploration and analysis

## 🚀 Running the System

### Option 1: Docker Compose

1. Ensure Docker and Docker Compose are installed
2. Run `docker-compose up --build`
3. Access the services:
   - App: http://localhost:5000
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000 (admin/admin)
   - Kibana: http://localhost:5601
   - Elasticsearch: http://localhost:9200

### Option 2: Kubernetes

1. Build the Flask app image: `docker build -t flask-app:latest ./app`
2. Apply Kubernetes manifests: `kubectl apply -f k8s/`
3. Access services via NodePort or LoadBalancer (adjust as needed)
   - App: via flask-app-service
   - Prometheus: via prometheus-service
   - Grafana: via grafana-service
   - Kibana: via kibana-service
   - Elasticsearch: via elasticsearch-service

## 🎯 Demonstrated Concepts

### Observability
- Metrics collection and visualization
- Log aggregation and analysis
- Centralized monitoring dashboard

### Metrics Collection
- Custom application metrics (request count, latency)
- Prometheus scraping configuration
- Grafana dashboard creation

### Log Aggregation
- Container log collection
- Log shipping with FluentBit
- Log processing pipeline with Logstash
- Full-text search and filtering with Kibana

### Troubleshooting Pipelines
- Real-time log streaming
- Metrics-based alerting potential
- Correlating logs and metrics for issue diagnosis

## 🧪 Testing the System

1. Visit http://localhost:5000 to generate traffic
2. Visit http://localhost:5000/error to generate error logs
3. Check metrics in Grafana
4. Explore logs in Kibana

## 🔧 Troubleshooting Pipelines Demonstration

- **Metrics-Based Issue Detection**: Use Grafana to monitor request latency and error rates
- **Log Correlation**: When errors occur, check Kibana for detailed stack traces and context
- **Root Cause Analysis**: Combine metrics (e.g., high latency) with logs (e.g., error messages) to diagnose issues
- **Real-Time Monitoring**: Observe live log streaming in Kibana and metric updates in Grafana

## 🔒 Security Notes

This is a development setup. In production:
- Use proper authentication and authorization
- Secure Elasticsearch and Kibana
- Configure TLS/SSL
- Use persistent storage appropriately

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.