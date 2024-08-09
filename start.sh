#!/bin/bash

cd "$(dirname "$(realpath "$0")")"
source my_env/bin/activate

streamlit run app.py --server.port 8502 &
streamlit run depositreturn.py --server.port 8503
