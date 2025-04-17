import requests

url = "http://localhost:7860/api/v1/run/3b8588c0-ec49-44ca-a725-e204e00140a6"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "input_value": "Quero um treino para emagrecer, tenho 30 anos e sou iniciante.",
    "output_type": "text",
    "input_type": "chat",
}
# Request headers
headers = {"Content-Type": "application/json"}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
