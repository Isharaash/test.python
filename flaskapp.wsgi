#!/usr/bin/python3
import sys
import logging

sys.path.insert(0, '/home/ubuntu/actions-runner/actions-runner/mydemo/test.python/test.python')

from app import app as application

logging.basicConfig(stream=sys.stderr)
