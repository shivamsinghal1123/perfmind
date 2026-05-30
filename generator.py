"""
PerfMind — Core NFR Generator
Uses Claude API to generate structured Non-Functional Requirements
"""

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()


class NFRGenerator:
    """
    Generates structured NFR (Non-Functional Requirements) documents
    using Claude AI based on application description and user stories.
    """

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found. "
                "Please add it to your .env file."
            )
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = os.getenv("ANTHROPIC_MODEL")

    def _build_prompt(self, app_description: str, user_stories: str = "") -> str:
        """Build the prompt for Claude to generate NFR requirements."""

        user_stories_section = ""
        if user_stories:
            user_stories_section = f"""
User Stories / Acceptance Criteria:
{user_stories}
"""

        return f"""You are PerfMind — an expert Performance Engineering AI with 40+ years of experience in Non-Functional Testing.

Your job is to analyse the application description below and generate a comprehensive, structured NFR (Non-Functional Requirements) document that a Performance Engineer can use immediately.

Application Description:
{app_description}
{user_stories_section}

Generate a structured NFR Requirements Document with the following sections:

## 1. PERFORMANCE REQUIREMENTS
- Response Time SLAs (define P50, P90, P95, P99 targets)
- Throughput requirements (requests per second / transactions per minute)
- Concurrent user targets (normal load, peak load, stress load)

## 2. SCALABILITY REQUIREMENTS
- Horizontal / Vertical scaling expectations
- Auto-scaling triggers and thresholds
- Data volume growth projections

## 3. RELIABILITY & AVAILABILITY
- Uptime SLA (e.g. 99.9%)
- Recovery Time Objective (RTO)
- Recovery Point Objective (RPO)
- Acceptable error rate under load

## 4. INFRASTRUCTURE REQUIREMENTS
- Recommended environment setup for performance testing
- Minimum hardware/cloud specs for test environment
- Network bandwidth considerations

## 5. PERFORMANCE TEST SCENARIOS
List the top 5-7 critical performance test scenarios for this application, in priority order.

## 6. NFR RISKS & ASSUMPTIONS
- Key risks that could impact performance
- Assumptions made in these requirements
- Questions that must be answered by the client before testing begins

## 7. RECOMMENDED PERFORMANCE TEST TYPES
Which test types are recommended and why:
- Load Test
- Stress Test
- Spike Test
- Soak/Endurance Test
- Scalability Test

Be specific, practical and actionable. Base your recommendations on the application type and description provided. Where information is missing, clearly flag it as [NEEDS CLARIFICATION] so the engineer knows what to ask the client.
"""

    def generate(self, app_description: str, user_stories: str = "") -> str:
        """
        Generate NFR requirements document using Claude API.

        Args:
            app_description: Description of the application
            user_stories: Optional user stories or acceptance criteria

        Returns:
            Structured NFR requirements document as string
        """
        try:
            prompt = self._build_prompt(app_description, user_stories)

            message = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return message.content[0].text

        except anthropic.AuthenticationError:
            print("❌ Invalid API key. Please check your ANTHROPIC_API_KEY in .env file.")
            return None
        except anthropic.RateLimitError:
            print("❌ Rate limit hit. Please wait a moment and try again.")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            return None
