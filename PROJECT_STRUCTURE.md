# Project Structure

```
.
├── app/                    # Flask application
│   ├── app.py             # Main Flask application with Prometheus metrics
│   ├── Dockerfile         # Docker configuration for the Flask app
│   └── requirements.txt   # Python dependencies
├── elk/                   # ELK Stack configurations
│   ├── elasticsearch.yml  # Elasticsearch configuration
│   ├── kibana.yml         # Kibana configuration
│   └── logstash.conf      # Logstash pipeline configuration
├── fluentbit/             # FluentBit configuration
│   └── fluent-bit.conf    # FluentBit configuration file
├── grafana/               # Grafana configurations
│   └── provisioning/      # Grafana provisioning configurations
│       ├── dashboards/    # Dashboard configurations
│       │   ├── dashboard.yml
│       │   └── flask-dashboard.json
│       └── datasources/   # Datasource configurations
│           └── datasource.yml
├── k8s/                   # Kubernetes manifests
│   ├── app-deployment.yaml
│   ├── app-service.yaml
│   ├── elasticsearch-deployment.yaml
│   ├── elasticsearch-service.yaml
│   ├── fluentbit-configmap.yaml
│   ├── fluentbit-daemonset.yaml
│   ├── grafana-configmap.yaml
│   ├── grafana-deployment.yaml
│   ├── grafana-service.yaml
│   ├── kibana-deployment.yaml
│   ├── kibana-service.yaml
│   ├── logstash-configmap.yaml
│   ├── logstash-deployment.yaml
│   ├── logstash-service.yaml
│   ├── prometheus-configmap.yaml
│   ├── prometheus-deployment.yaml
│   └── prometheus-service.yaml
├── prometheus/            # Prometheus configurations
│   ├── alerting_rules.yml # Alerting rules
│   └── prometheus.yml     # Prometheus configuration
├── .gitignore             # Git ignore file
├── docker-compose.yml     # Docker Compose configuration
├── LICENSE                # License file
├── README.md              # Project documentation
├── SETUP.md               # Setup guide
└── requirements.txt       # Python dependencies
```