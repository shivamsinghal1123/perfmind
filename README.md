# PerfMind 🧠

> AI-powered NFR Requirements Generator for Performance Engineers

## The Problem

Performance Testing fails before it begins.

Teams spend weeks gathering NFR requirements manually.
Clients don't know what they need. Engineers waste expert 
time on repetitive discovery. Projects delayed before 
a single test runs.

## What PerfMind Does

PerfMind uses AI to automatically generate structured 
Non-Functional Requirements (NFR) documents from:
- Application descriptions
- User stories  
- Production logs

In minutes. Not weeks.

## Industries Tested

| Industry | Highlights |
|----------|-----------|
| ✅ E-Commerce | Flash sale spikes, CDN sizing, conversion ratios |
| ✅ Healthcare | HIPAA-aware, patient safety SLAs, clinical rationale |
| ✅ Banking | RPO=Zero, RBI/FCA/MAS citations, fraud ML latency |
| ✅ Telecom | Little's Law applied, incident-driven spike modelling |

## Sample Output

For a hospital patient management system, PerfMind generates:

| Transaction | P50 | P90 | P95 | P99 |
|-------------|-----|-----|-----|-----|
| Appointment Booking | 800ms | 1,500ms | 2,000ms | 3,500ms |
| Medical Records | 1,200ms | 2,500ms | 4,000ms | 6,000ms |
| Lab Results | 900ms | 1,800ms | 2,500ms | 4,000ms |
| Authentication | 400ms | 800ms | 1,200ms | 2,000ms |

> ⚠️ Critical Notice: Performance failures in healthcare 
> are not just technical incidents — they can directly 
> impact patient safety. All NFRs are minimum thresholds.

PerfMind automatically flags HIPAA compliance requirements,
defines RTO/RPO targets, sizes infrastructure and generates
prioritised test scenarios — all from a plain English
application description.

## Getting Started

### Prerequisites
- Python 3.9+
- Anthropic API key

### Installation

```bash
git clone https://github.com/shivamsinghal1123/perfmind.git
cd perfmind
pip install -r requirements.txt
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
```

### Run PerfMind

```bash
python main.py
```

## Built With
- Python
- Anthropic Claude API
- FastAPI (coming soon)

## Status
🚧 Active Development — V0.1 Live

## Author
Shivam Singhal — 11 years in Performance Engineering  
[LinkedIn](https://www.linkedin.com/in/shivam-singhal-b287b6147/)

## License
Business Source License (BSL) — Free for personal and 
community use. Commercial use requires permission.