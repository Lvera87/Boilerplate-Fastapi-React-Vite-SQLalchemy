#requires -Version 7
[CmdletBinding()]
param(
    [ValidateSet('backend', 'frontend', 'all')]
    [string]$Target = 'all'
)

$ErrorActionPreference = 'Stop'

$RepoRoot    = Resolve-Path (Join-Path $PSScriptRoot '..')
$BackendDir  = Join-Path $RepoRoot 'backend'
$FrontendDir = Join-Path $RepoRoot 'frontend'

function Invoke-BackendTests {
    Write-Host 'Ejecutando pruebas de backend (uv run pytest)...' -ForegroundColor Cyan
    Push-Location $BackendDir
    try {
        uv run pytest
        if ($LASTEXITCODE -ne 0) { throw "pytest falló (exit $LASTEXITCODE)" }
    } finally { Pop-Location }
}

function Invoke-FrontendTests {
    Write-Host 'Ejecutando pruebas de frontend (vitest)...' -ForegroundColor Green
    Push-Location $FrontendDir
    try {
        npm run test:ci
        if ($LASTEXITCODE -ne 0) { throw "vitest falló (exit $LASTEXITCODE)" }
    } finally { Pop-Location }
}

switch ($Target) {
    'backend'  { Invoke-BackendTests }
    'frontend' { Invoke-FrontendTests }
    'all'      {
        Write-Host 'Ejecutando pruebas backend y frontend...' -ForegroundColor Yellow
        Invoke-BackendTests
        Invoke-FrontendTests
    }
}
