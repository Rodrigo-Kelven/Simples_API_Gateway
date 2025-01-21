#!/bin/bash

fastapi dev api_gateway.py --reload --port 8000
fastapi dev service_a.py --reload --port 8001
fastapi dev service_b.py --reload --port 8002