# Job Search Agent - Auto-Apply Feature

This branch adds **Auto-Apply functionality** to the Job Search Agent dashboard.

## What's New

✨ **Auto-Apply Mode**: Automatically apply to jobs matching your criteria without manual clicking.

Features:
- Toggle auto-apply on/off in the Search Configuration
- Set match score threshold (50-100%)
- Auto-applies jobs above threshold when agent finds them
- Tracks all applications with timestamps
- Staggered applications (500ms delay) to avoid blocking
- Backend API integration for application logging

## Setup Instructions

### 1. Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Backend Server (Port 5000)
```bash
python app.py
```

The backend will:
- Listen on `http://localhost:5000`
- Provide `/api/apply` endpoint for auto-apply submissions
- Log all applications to `applications.json`
- Provide `/api/applications` to retrieve application history

### 3. Run Frontend Server (Port 8000)
In a separate terminal:
```bash
python -m http.server 8000
```

Access dashboard: `http://localhost:8000`

## How to Use

1. **Enable Auto-Apply**: Toggle "Auto-Apply Mode" in Search Configuration
2. **Set Threshold**: Adjust match score slider (default: 75%)
3. **Configure Search**: Set job title, location, experience level
4. **Select Sources**: Choose job portals to search
5. **Run Agent**: Click "▶ Run Agent"
   - Agent finds jobs
   - Auto-applies to jobs matching threshold
   - Shows application log in real-time

## API Endpoints

- `POST /api/apply` - Submit auto-application
- `GET /api/applications` - Get all submitted applications
- `DELETE /api/applications/<job_id>` - Remove application record
- `GET /health` - Health check

## Files Changed

- `index.html` - Added auto-apply UI and logic
- `app.py` - New Flask backend server
- `requirements.txt` - Backend dependencies

## Next Steps

When ready to merge to `main`:
```bash
git add .
git commit -m "feat: Add auto-apply functionality with threshold control"
git push origin feature/auto-apply
# Create Pull Request on GitHub
```
