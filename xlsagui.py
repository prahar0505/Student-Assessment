#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rprenamer.py

"""This module provides the RP Renamer entry-point script."""

import os
os.environ['TRANSFORMERS_CACHE'] = './huggingface_cache'

from xlsagui.app import main

if __name__ == "__main__":
    main()
