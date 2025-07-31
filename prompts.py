import httpx

OPENROUTER_API_KEY = "sk-"  # Replace with your OpenRouter key
MODEL = "google/gemma-3-4b-it:free"

def generate_questions_prompt(info):
    techs = [t.strip() for t in info['tech_stack'].split(',')]
    prompt = (
        f"You are a technical interviewer bot.\n"
        f"The candidate has {info['experience']} years of experience and is applying for the position of {info['position']}.\n"
        f"Their tech stack includes: {', '.join(techs)}.\n\n"
        f"Generate 3 to 5 technical questions per technology. Format clearly under each technology name.\n"
        f"Only return the questions."
    )
    return prompt

def get_llm_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1024,
        "temperature": 0.7
    }

    try:
        response = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
