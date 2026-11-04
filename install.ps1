<#
============================================================
 YONG-NIAN-V1 — PowerShell Installer (Windows)
============================================================
#>

[CmdletBinding()]
param(
    [switch]$SkipSystemDeps,
    [switch]$UseConda
)

$ErrorActionPreference = "Stop"

$AppDir   = Split-Path -Parent $MyInvocation.MyCommand.Definition
$VenvDir  = Join-Path $AppDir ".venv"
$PyFile   = Join-Path $AppDir "yong_nian_v1.py"
$ReqFile  = Join-Path $AppDir "requirements.txt"
$VenvPy   = Join-Path $VenvDir "Scripts\python.exe"

function Write-Log  ($msg) { Write-Host "[*] $msg" -ForegroundColor Cyan }
function Write-Ok   ($msg) { Write-Host "[+] $msg" -ForegroundColor Green }
function Write-Warn ($msg) { Write-Host "[!] $msg" -ForegroundColor Yellow }
function Write-Err  ($msg) { Write-Host "[x] $msg" -ForegroundColor Red }

Write-Host @"
============================================================
   YONG-NIAN-V1  -  PowerShell Installer
   Ultimate Multi-Platform Pentest Platform
============================================================
"@ -ForegroundColor Cyan

# ---- Check Python ----
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Err "Python not found on PATH. Install from https://www.python.org/downloads/"
    exit 1
}
$pyVer = & python --version 2>&1
Write-Ok "Detected $pyVer"

# ---- Optional: Chocolatey system deps ----
if (-not $SkipSystemDeps) {
    $choco = Get-Command choco -ErrorAction SilentlyContinue
    if ($choco) {
        Write-Log "Installing system tools via Chocolatey..."
        choco install -y nmap curl wget netcat traceroute whois openssh 2>$null
    } else {
        Write-Warn "Chocolatey not installed. Skipping system tools."
        Write-Warn "Install manually: nmap, curl, wget, netcat, traceroute, whois"
    }
}

# ---- Create venv ----
if (-not (Test-Path $VenvDir)) {
    Write-Log "Creating virtual environment at $VenvDir"
    python -m venv $VenvDir
}

# ---- Activate ----
$activate = Join-Path $VenvDir "Scripts\Activate.ps1"
if (Test-Path $activate) {
    . $activate
} else {
    Write-Err "Activation script not found."
    exit 1
}

# ---- Upgrade pip ----
Write-Log "Upgrading pip / wheel / setuptools..."
& $VenvPy -m pip install --upgrade pip wheel setuptools

# ---- Install deps ----
if (-not (Test-Path $ReqFile)) {
    Write-Err "requirements.txt not found at $ReqFile"
    exit 1
}
Write-Log "Installing Python dependencies..."
& $VenvPy -m pip install -r $ReqFile

# ---- Verify ----
if (-not (Test-Path $PyFile)) {
    Write-Err "yong_nian_v1.py not found at $PyFile"
    exit 1
}

Write-Ok "Installation complete!"
Write-Host ""
Write-Host "  Launch:" -ForegroundColor Green
Write-Host "    .\$VenvDir\Scripts\Activate.ps1"
Write-Host "    python $PyFile"
Write-Host ""
Write-Host "  Web dashboard: http://localhost:5000" -ForegroundColor Green
Write-Host ""
Write-Warn "Run PowerShell as Administrator for full network capabilities."
Write-Warn "For authorized security testing only."
