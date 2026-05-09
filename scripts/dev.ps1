#requires -Version 7
[CmdletBinding()]
param(
    [ValidateSet('backend', 'frontend', 'all')]
    [string]$Target = 'all'
)

$ErrorActionPreference = 'Stop'

# Resolve repo root regardless of where the script is invoked from.
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..')
$BackendDir  = Join-Path $RepoRoot 'backend'
$FrontendDir = Join-Path $RepoRoot 'frontend'

if ($Target -in @('backend', 'all')) {
    if (-not (Get-Command 'uv' -ErrorAction SilentlyContinue)) {
        throw "uv no está instalado. Instálalo desde https://docs.astral.sh/uv/"
    }
    Write-Host 'Iniciando backend (uv run uvicorn)...' -ForegroundColor Cyan
    Start-Process -NoNewWindow -FilePath 'pwsh' `
        -WorkingDirectory $BackendDir `
        -ArgumentList '-NoExit', '-Command', 'uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload' | Out-Null
}

if ($Target -in @('frontend', 'all')) {
    if (-not (Get-Command 'npm' -ErrorAction SilentlyContinue)) {
        throw "npm no está instalado."
    }
    Write-Host 'Iniciando frontend (Vite)...' -ForegroundColor Green
    Start-Process -NoNewWindow -FilePath 'npm' `
        -WorkingDirectory $FrontendDir `
        -ArgumentList 'run', 'dev'
}
