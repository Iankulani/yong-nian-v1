#!/usr/bin/env bash
# ============================================================
# YONG-NIAN-V1 — Bash Installer (Linux / macOS / WSL)
# ============================================================
set -euo pipefail

APP_NAME="YONG-NIAN-V1"
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$APP_DIR/.venv"
PY_FILE="$APP_DIR/yong_nian_v1.py"
REQ_FILE="$APP_DIR/requirements.txt"

COLOR_CYAN="\033[1;36m"
COLOR_GREEN="\033[1;32m"
COLOR_YELLOW="\033[1;33m"
COLOR_RED="\033[1;31m"
COLOR_RESET="\033[0m"

log()  { echo -e "${COLOR_CYAN}[*]${COLOR_RESET} $*"; }
ok()   { echo -e "${COLOR_GREEN}[+]${COLOR_RESET} $*"; }
warn() { echo -e "${COLOR_YELLOW}[!]${COLOR_RESET} $*"; }
err()  { echo -e "${COLOR_RED}[x]${COLOR_RESET} $*" >&2; }

banner() {
cat <<'EOF'
╔═══════════════════════════════════════════════════════════════╗
║       YONG-NIAN-V1  —  Bash Installer                        ║
║       Ultimate Multi-Platform Pentest Platform              ║
╚═══════════════════════════════════════════════════════════════╝
EOF
}

detect_os() {
    case "$(uname -s)" in
        Linux*)   OS="linux" ;;
        Darwin*)  OS="macos" ;;
        *)        OS="unknown" ;;
    esac
    log "Detected OS: $OS"
}

install_system_deps_linux() {
    log "Installing system packages (apt/dnf/pacman)..."
    if command -v apt-get >/dev/null; then
        sudo apt-get update -y
        sudo apt-get install -y --no-install-recommends \
            python3 python3-pip python3-venv python3-dev \
            build-essential libffi-dev libssl-dev libjpeg-dev zlib1g-dev \
            libfreetype6-dev libpng-dev nmap curl wget netcat-openbsd \
            traceroute dnsutils whois openssh-client git tcpdump \
            iputils-ping mtr-tiny
    elif command -v dnf >/dev/null; then
        sudo dnf install -y python3 python3-pip python3-devel \
            gcc gcc-c++ make libffi-devel openssl-devel libjpeg-turbo-devel \
            zlib-devel freetype-devel libpng-devel nmap curl wget nmap-ncat \
            traceroute bind-utils whois openssh-clients git tcpdump iputils mtr
    elif command -v pacman >/dev/null; then
        sudo pacman -Sy --noconfirm python python-pip base-devel \
            libffi openssl libjpeg-turbo zlib freetype2 libpng \
            nmap curl wget gnu-netcat traceroute bind whois openssh git tcpdump iputils mtr
    else
        warn "Unknown package manager — install system deps manually."
    fi
}

install_system_deps_macos() {
    log "Installing Homebrew dependencies..."
    if ! command -v brew >/dev/null; then
        err "Homebrew not found. Install from https://brew.sh"
        exit 1
    fi
    brew update
    brew install python@3.11 nmap curl wget netcat traceroute bind whois openssh mtr || true
}

setup_venv() {
    log "Creating Python virtual environment at $VENV_DIR"
    python3 -m venv "$VENV_DIR"
    # shellcheck disable=SC1091
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip wheel setuptools
}

install_python_deps() {
    log "Installing Python dependencies..."
    if [ -f "$REQ_FILE" ]; then
        pip install -r "$REQ_FILE"
    else
        err "requirements.txt not found at $REQ_FILE"
        exit 1
    fi
}

finalize() {
    if [ ! -f "$PY_FILE" ]; then
        err "yong_nian_v1.py not found at $PY_FILE"
        exit 1
    fi
    chmod +x "$PY_FILE"
    ok "Installation complete!"
    echo
    echo -e "${COLOR_GREEN}Launch:${COLOR_RESET}"
    echo "  source $VENV_DIR/bin/activate"
    echo "  python3 $PY_FILE"
    echo
    echo -e "${COLOR_GREEN}Web dashboard:${COLOR_RESET}  http://localhost:5000"
    echo -e "${COLOR_YELLOW}⚠  For authorized security testing only.${COLOR_RESET}"
}

main() {
    banner
    detect_os
    case "$OS" in
        linux)   install_system_deps_linux ;;
        macos)   install_system_deps_macos ;;
        *)       warn "Unsupported OS; continuing with Python-only setup." ;;
    esac
    setup_venv
    install_python_deps
    finalize
}

main "$@"
