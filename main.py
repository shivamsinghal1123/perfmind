"""
PerfMind 🧠
AI-powered NFR Requirements Generator for Performance Engineers

Author: Shivam Singhal
GitHub: https://github.com/shivamsinghal1123/perfmind
"""

import time

from perfmind.generator import NFRGenerator
from perfmind.utils import print_banner
from perfmind.exporter import NFRDocumentExporter


def main():
    print_banner()

    print("Welcome to PerfMind — AI-powered NFR Requirements Generator\n")
    print("=" * 60)

    # ── Step 1: Collect application description ──────────────────
    step1_start = time.perf_counter()

    print("\nDescribe your application (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    app_description = "\n".join(lines).strip()

    step1_duration = time.perf_counter() - step1_start

    if not app_description:
        print("No description provided. Exiting.")
        return

    print(f"\n⏱  Input collected in {step1_duration:.2f}s")

    # ── Step 2: Generate NFR requirements via Claude API ─────────
    print("\n⏳ PerfMind is analysing your application and generating NFR requirements...\n")

    step2_start = time.perf_counter()

    generator = NFRGenerator()
    result = generator.generate(app_description=app_description)

    step2_duration = time.perf_counter() - step2_start

    if not result:
        print("❌ Failed to generate requirements. Please check your API key and try again.")
        return

    print("\n" + "=" * 60)
    print("✅ NFR REQUIREMENTS GENERATED SUCCESSFULLY")
    print("=" * 60 + "\n")
    print(result)
    print(f"\n⏱  API call completed in {step2_duration:.2f}s")

    # ── Step 3: Export to .docx ───────────────────────────────────
    step3_start = time.perf_counter()

    exporter = NFRDocumentExporter()
    output_path = exporter.export(result, app_description)

    step3_duration = time.perf_counter() - step3_start

    print(f"\n💾 Word document saved to: {output_path}")
    print(f"⏱  Export completed in {step3_duration:.2f}s")

    # ── Timing Summary ────────────────────────────────────────────
    total = step1_duration + step2_duration + step3_duration
    print("\n" + "─" * 60)
    print("📊 TIMING SUMMARY")
    print("─" * 60)
    print(f"  Step 1 — Input collection : {step1_duration:>8.2f}s")
    print(f"  Step 2 — Claude API call  : {step2_duration:>8.2f}s")
    print(f"  Step 3 — .docx export     : {step3_duration:>8.2f}s")
    print(f"  {'─' * 38}")
    print(f"  Total                     : {total:>8.2f}s")
    print("─" * 60)


if __name__ == "__main__":
    main()
