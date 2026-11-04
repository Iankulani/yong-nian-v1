#!/usr/bin/env python3
"""
setup.py — YONG-NIAN-V1
"""

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
readme = ""
if os.path.exists(os.path.join(here, "README.md")):
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        readme = f.read()

setup(
    name="yong-nian-v1",
    version="1.0.0",
    author="Ian Carter Kulani",
    description="Ultimate Multi-Platform Penetration Testing Command & Control Platform",
    long_description=readme,
    long_description_content_type="text/markdown",
    py_modules=["yong_nian_v1"],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "psutil>=5.9.0",
        "colorama>=0.4.6",
    ],
    extras_require={
        "full": [
            "cryptography>=41.0.0",
            "paramiko>=3.3.0",
            "scapy>=2.5.0",
            "python-whois>=0.9.4",
            "shodan>=1.28.0",
            "dnspython>=2.4.2",
            "qrcode>=7.4.2",
            "pyshorteners>=1.0.1",
            "flask>=3.0.0",
            "flask-socketio>=5.3.0",
            "flask-cors>=4.0.0",
            "beautifulsoup4>=4.12.0",
            "discord.py>=2.3.0",
            "telethon>=1.34.0",
            "slack-sdk>=3.26.0",
            "selenium>=4.15.0",
            "webdriver-manager>=4.0.1",
            "google-auth>=2.23.0",
            "google-api-python-client>=2.108.0",
            "pynput>=1.7.6",
            "pillow>=10.1.0",
            "pyperclip>=1.8.2",
            "pefile>=2023.2.7",
            "capstone>=5.0.0",
            "pyelftools>=0.30",
            "matplotlib>=3.8.0",
            "numpy>=1.26.0",
            "reportlab>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "yong-nian=yong_nian_v1:main",
            "yongnian=yong_nian_v1:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
)
