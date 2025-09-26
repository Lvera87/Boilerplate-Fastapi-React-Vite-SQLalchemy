param(
    [ValidateSet('backend', 'frontend', 'all')]
    [string]$Target = 'all'
)

if ($Target -eq 'backend' -or $Target -eq 'all') {
    Write-Host 'Iniciando backend (uvicorn)...' -ForegroundColor Cyan
    Start-Process -NoNewWindow -FilePath "pwsh" -ArgumentList "-NoExit", "-Command", "cd ..\backend; $env:UVICORN_RELOAD='True'; uvicorn app.main:app --host 0.0.0.0 --port 8000" | Out-Null
}

if ($Target -eq 'frontend' -or $Target -eq 'all') {
    Write-Host 'Iniciando frontend (Vite)...' -ForegroundColor Green
    Start-Process -NoNewWindow -FilePath "npm" -WorkingDirectory "..\frontend" -ArgumentList "run", "dev"
}
