#!/bin/bash

nano "uvicorn service_a:app --host 0.0.0.0 --port 8001" > service_a.sh
chmod +x service_a.sh
./service_a.sh

nano "uvicorn service_b:app --host 0.0.0.0 --port 8002" > service_b.sh
chmod +x service_b.sh
./service_b.sh

nano "uvicorn api_gateway:app --host 0.0.0.0 --port 8000" > api_gateway.sh
chmod +x api_gateway.sh
./api_gateway.sh


