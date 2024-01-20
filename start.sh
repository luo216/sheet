#!/bin/bash

source ./venv/bin/activate
# 在生产环境下使用wsgi,如果是测试调试环境下，使用flask (-debug true)即可
gunicorn wsgi:app
