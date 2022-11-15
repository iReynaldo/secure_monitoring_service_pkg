#!/bin/sh

PYTHONHASHSEED=0
cd ..
pytest --cov=secure_monitoring_service_pkg secure_monitoring_service_pkg/tests/engine_tests
rm report_graph_targe_asn_*.png
