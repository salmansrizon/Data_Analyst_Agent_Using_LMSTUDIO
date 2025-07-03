import requests
from utils.config_loader import load_llm_config


def test_lm_api():
    llm_config = load_llm_config()

    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "model": llm_config["model_name"],
        "messages": [
            {"role": "user", "content": "Explain the concept of machine learning."}
        ],
        "temperature": llm_config["temperature"],
        "max_tokens": llm_config["max_tokens"],
    }

    try:
        print("Sending API Request:", payload)  # Debugging output
        response = requests.post(
            llm_config["base_url"],
            json=payload,
            headers=headers,
            timeout=llm_config["timeout"],
        )
        response.raise_for_status()

        # Debugging: Print the full API response
        print("API Response:", response.json())

        # Extract the response content
        if "choices" in response.json() and len(response.json()["choices"]) > 0:
            print(
                "LLM Response:",
                response.json()["choices"][0]["message"]["content"].strip(),
            )
        else:
            print("Unexpected API response format: 'choices' key is missing or empty.")
    except Exception as e:
        print(f"LM Studio API call failed: {str(e)}")


if __name__ == "__main__":
    test_lm_api()
