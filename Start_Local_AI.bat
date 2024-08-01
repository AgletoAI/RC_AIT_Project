@echo off
cd C:\HarryAITime\RC_AIT_Project
call myenv\Scripts\activate
start "" python server.py
timeout /t 5 /nobreak >nul
start "" firefox -new-window http://127.0.0.1:5000/
pause
