# E-Commerce Project Runner Script

Write-Host "Starting E-Commerce Sales Performance Project Pipeline..." -ForegroundColor Cyan

# 1. Data Cleaning
Write-Host "`n[1/5] Running Data Cleaning & Date Simulation..." -ForegroundColor Yellow
python "notebooks/02_data_cleaning.py"
if ($LASTEXITCODE -ne 0) { Write-Error "Data Cleaning Failed"; exit 1 }

# 2. EDA
Write-Host "`n[2/5] Running Exploratory Data Analysis (EDA)..." -ForegroundColor Yellow
python "notebooks/03_eda.py"
if ($LASTEXITCODE -ne 0) { Write-Error "EDA Failed"; exit 1 }

# 3. SQL Verification
Write-Host "`n[3/5] Verifying SQL Queries..." -ForegroundColor Yellow
python "notebooks/04_sql_verification.py"
if ($LASTEXITCODE -ne 0) { Write-Error "SQL Verification Failed"; exit 1 }

# 4. Funnel Analysis
Write-Host "`n[4/5] Running Funnel Analysis..." -ForegroundColor Yellow
python "notebooks/05_funnel_analysis.py"
if ($LASTEXITCODE -ne 0) { Write-Error "Funnel Analysis Failed"; exit 1 }

# 5. Excel Preparation
Write-Host "`n[5/5] Preparing Excel Dashboard File..." -ForegroundColor Yellow
python "notebooks/06_excel_prep.py"
if ($LASTEXITCODE -ne 0) { Write-Error "Excel Prep Failed"; exit 1 }

Write-Host "`nSUCCESS! All project scripts have been executed." -ForegroundColor Green
Write-Host "Outputs available in:"
Write-Host " - Cleaned Data: data/cleaned/"
Write-Host " - Images/Charts: images/"
Write-Host " - Excel File: excel/analysis.xlsx"
