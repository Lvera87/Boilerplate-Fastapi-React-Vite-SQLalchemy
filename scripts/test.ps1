param(
    [ValidateSet('backend', 'frontend', 'all')]
    [string]$Target = 'all'
)

switch ($Target) {
    'backend' {
        Write-Host 'Ejecutando pruebas de backend (pytest)...' -ForegroundColor Cyan
        pwsh -Command "cd ..\backend; pytest"
    }
    'frontend' {
        Write-Host 'Ejecutando pruebas de frontend (vitest)...' -ForegroundColor Green
        pwsh -Command "cd ..\frontend; npm run test -- --run"
    }
    'all' {
        Write-Host 'Ejecutando pruebas backend y frontend...' -ForegroundColor Yellow
        pwsh -Command "cd ..\backend; pytest"
        pwsh -Command "cd ..\frontend; npm run test -- --run"
    }
}
