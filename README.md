# PerfMind 🧠

> AI-powered NFR Requirements Generator for Performance Engineers

## The Problem

Performance Testing fails before it begins.

Teams spend weeks gathering NFR requirements manually. Clients don't know what they need. Engineers waste expert time on repetitive discovery. Projects get delayed before a single test runs.

## What PerfMind Does

PerfMind uses AI to automatically generate a structured, professional **Word document (.docx)** containing Non-Functional Requirements (NFR) — from a plain English application description.

In minutes. Not weeks.

## Industries Tested

| Industry | What PerfMind Adds |
|----------|--------------------|
| ✅ E-Commerce | Flash sale spikes, CDN sizing, conversion ratios |
| ✅ Healthcare | HIPAA-aware SLAs, patient safety notices, clinical rationale |
| ✅ Banking | RPO=Zero, RBI/FCA/MAS regulatory citations, fraud ML latency |
| ✅ Telecom | Little's Law applied, incident-driven spike modelling |

## Sample Output

For a hospital patient management system, PerfMind generates:

| Transaction | P50 | P90 | P95 | P99 |
|-------------|-----|-----|-----|-----|
| Appointment Booking | 800ms | 1,500ms | 2,000ms | 3,500ms |
| Medical Records | 1,200ms | 2,500ms | 4,000ms | 6,000ms |
| Lab Results | 900ms | 1,800ms | 2,500ms | 4,000ms |
| Authentication | 400ms | 800ms | 1,200ms | 2,000ms |

> ⚠️ Critical Notice: Performance failures in healthcare are not just technical incidents — they can directly impact patient safety. All NFRs are minimum thresholds.

PerfMind automatically flags HIPAA compliance requirements, defines RTO/RPO targets, sizes infrastructure and generates prioritised test scenarios — all from a plain English description.

## Getting Started

### Prerequisites
- Python 3.9+
- Anthropic API key — get yours at [console.anthropic.com](https://console.anthropic.com)

### Installation

```bash
git clone https://github.com/shivamsinghal1123/perfmind.git
cd perfmind
pip install -r requirements.txt
cp .env.example .env
```

### Configure your `.env` file

Open `.env` and set the following:

```
# Your Anthropic API key
ANTHROPIC_API_KEY=your_api_key_here

# Claude model to use
ANTHROPIC_MODEL=claude-sonnet-4-6

# Where your .docx files will be saved
# Windows: C:\Users\YourName\PerfMind_Outputs
# Mac/Linux: /Users/yourname/PerfMind_Outputs
OUTPUT_DIR=C:\Users\YourName\PerfMind_Outputs
```

### Run PerfMind

```bash
python main.py
```

PerfMind will prompt you for an application description, generate the NFR document and automatically save it as a `.docx` file to your configured `OUTPUT_DIR`.

## Output

Every run produces a timestamped Word document:

```
NFR_Requirements_20260530_143022.docx
```

The document includes:
- Professional title page with metadata
- Performance SLAs (P50/P90/P95/P99) per transaction
- Scalability and infrastructure requirements
- Reliability, RTO and RPO targets
- Prioritised test scenarios
- Risk register and client clarification questions

## Built With

- Python 3.9+
- [Anthropic Claude API](https://console.anthropic.com)
- python-docx

## Roadmap

- [x] NFR Requirements Generator (V0.1)
- [x] Professional .docx export (V0.2)
- [ ] Template-based generation — upload your existing test plan
- [ ] Local SLM support — run fully on-premise (no API required)
- [ ] Web interface

## Status

🚧 Active Development — V0.2

## Author

Shivam Singhal — 11 years in Performance Engineering
[LinkedIn](https://www.linkedin.com/in/shivam-singhal-b287b6147/)

## License

Business Source License (BSL) — Free for personal and community use.
Commercial use requires written permission from the author.
