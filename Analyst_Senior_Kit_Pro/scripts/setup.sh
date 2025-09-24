#!/usr/bin/env bash
python3 -m venv venv || python -m venv venv
if [ -f requirements.txt ]; then venv/bin/python -m pip install -r requirements.txt; fi
