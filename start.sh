#!/bin/bash

ENVIRONMENT=${1:-dev}

export ENVIRONMENT=$ENVIRONMENT

echo $ENVIRONMENT

poetry run python -m src.main
