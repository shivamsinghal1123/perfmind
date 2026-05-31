"""
PerfMind 🧠
AI-powered Requirements Generator for Performance Engineers

Author: Shivam Singhal
GitHub: https://github.com/shivamsinghal1123/perfmind
"""

from perfmind.generator import NFRGenerator
from perfmind.utils import print_banner, save_output
from perfmind.exporter import NFRDocumentExporter


def main():
    print_banner()

    print("Welcome to PerfMind — AI-powered NFR Requirements Generator\n")
    print("=" * 60)

    # Step 1: Get application description from user
    print("\nDescribe your application (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    app_description = "\n".join(lines).strip()

    if not app_description:
        print("No description provided. Exiting.")
        return

    # Step 2: Optional — get existing user stories
    print("\nDo you have user stories or acceptance criteria to include? (y/n): ", end="")
    has_stories = input().strip().lower()
    user_stories = ""
    if has_stories == "y":
        print("Paste your user stories (press Enter twice when done):")
        story_lines = []
        while True:
            line = input()
            if line == "" and story_lines and story_lines[-1] == "":
                break
            story_lines.append(line)
        user_stories = "\n".join(story_lines).strip()

    # Step 3: Generate NFR requirements
    print("\n⏳ PerfMind is analysing your application and generating NFR requirements...\n")

    generator = NFRGenerator()
    result = generator.generate(
        app_description=app_description,
        user_stories=user_stories
    )

    if result:
        print("\n" + "=" * 60)
        print("✅ NFR REQUIREMENTS GENERATED SUCCESSFULLY")
        print("=" * 60 + "\n")
        print(result)

        # Step 4: Save output
        output_path = save_output(result, app_description)
        print(f"\n💾 Output saved to: {output_path}")
    else:
        print("❌ Failed to generate requirements. Please check your API key and try again.")

    # Step 4: Export result in .docx format
    print("\nExport format:")
    print("1. Word Document (.docx) — recommended for clients")
    print("2. Markdown (.md) — for developers")
    export_choice = input("\nChoose (1 or 2): ").strip()

    if export_choice == "1":
        exporter = NFRDocumentExporter()
        output_path = exporter.export(result, app_description)
        print(f"\n💾 Word document saved to: {output_path}")
    else:
        output_path = save_output(result, app_description)
        print(f"\n💾 Markdown saved to: {output_path}")


if __name__ == "__main__":
    main()
