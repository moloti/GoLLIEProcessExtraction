#!/bin/bash

CONFIG_DIR="configs/data_configs"
OUTPUT_DIR="data/processed_w_examples"

python -m src.generate_data \
     --configs \
        ${CONFIG_DIR}/medical_guideline_config.json \
     --output ${OUTPUT_DIR} \
     --overwrite_output_dir \
     --include_examples