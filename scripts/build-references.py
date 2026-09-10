#!/usr/bin/env python3
# Kept for old callers. The builder is build.py in this folder.
import os, runpy, sys
sys.argv = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "build.py")] + sys.argv[1:]
runpy.run_path(sys.argv[0], run_name="__main__")
