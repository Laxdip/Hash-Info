#!/usr/bin/env python3
# encoding: utf-8
# ============================================================
#   Hash Info - Advanced Hash Identifier
#   By Prasad  |  v2.0
# ============================================================

import sys
import os
import re
import argparse
from builtins import input

version = "2.0"

# ──────────────────────────────────────────────
#  ANSI Color Codes
# ──────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"

# Disable colors if output is piped / redirected
if not sys.stdout.isatty():
    for attr in vars(C):
        if not attr.startswith("_"):
            setattr(C, attr, "")

# ──────────────────────────────────────────────
#  Logo
# ──────────────────────────────────────────────
logo = f"""
{C.CYAN}{C.BOLD}
  ██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██╗███╗   ██╗███████╗ ██████╗
  ██║  ██║██╔══██╗██╔════╝██║  ██║    ██║████╗  ██║██╔════╝██╔═══██╗
  ███████║███████║███████╗███████║    ██║██╔██╗ ██║█████╗  ██║   ██║
  ██╔══██║██╔══██║╚════██║██╔══██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
  ██║  ██║██║  ██║███████║██║  ██║    ██║██║ ╚████║██║     ╚██████╔╝
  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝
{C.RESET}{C.GRAY}  Advanced Hash Identifier  |  v{version}  |  By Prasad{C.RESET}
  {C.DIM}{'─' * 62}{C.RESET}
"""
