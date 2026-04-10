import requests
import os
import httpx
import json



TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")
TINYFISH_BASE_URL = "https://agent.tinyfish.ai/v1/automation/run-sse"


class TinyFishService:

    @staticmethod
    async def search_jobs():

        headers = {
            "X-API-Key": TINYFISH_API_KEY,
            "Content-Type": "application/json"
        }

        payload = {
            "url": "https://news.ycombinator.com/jobs",
            "goal": """
            Extract the first 15 job postings.
            For each, get:
            - title
            - url
            - posted date

            Return JSON array:
            [
              {
                "title": "",
                "url": "",
                "posted": ""
              }
            ]
            """
        }

        collected = ""

        async with httpx.AsyncClient(timeout=60) as client:
            async with client.stream(
                "POST",
                TINYFISH_BASE_URL,
                headers=headers,
                json=payload
            ) as response:

                async for line in response.aiter_lines():
                    if line.startswith("data:"):
                        collected += line.replace("data:", "").strip()

        # ✅ Convert to JSON safely
        try:
            return json.loads(collected)
        except Exception:
            return {"raw_response": collected}


    @staticmethod
    def parse_jobs(response_json):
        jobs = []

        result = response_json.get("result", {})

        for job in result.get("jobs", []):
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company"),
                "location": job.get("location"),
                "url": job.get("url")
            })

        return jobs