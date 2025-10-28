# import openai

# # openai.api_key = "REDACTED"

# SCAM_DETECT_PROMPT = """
# You are a financial security AI. Classify the following message as SAFE or SCAM and explain your reasoning.

# Message: "{message}"
# """

# def detect_scam(message):
#     prompt = SCAM_DETECT_PROMPT.format(message=message)
    
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # or use llama2 via HuggingFace
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.3
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"Error: {e}"


from transformers import pipeline

classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-sms-spam-detection")

SCAM_KEYWORDS = [
    "click here", "verify your account", "bank blocked", "lottery",
    "congratulations", "urgent", "account suspended", "reward","Share OTP"
    "KYC expired", "login to avoid closure", "send OTP", "win ₹"
]

def keyword_based_check(message):
    message_lower = message.lower()
    for kw in SCAM_KEYWORDS:
        if kw in message_lower:
            return True
    return False

def detect_scam(text):
    result = classifier(text)[0]  # ✅ fixed here
    label = result['label'].lower()
    confidence = result['score']

    if label == 'spam' or keyword_based_check(text):
        return f"⚠️ SCAM DETECTED\nConfidence: {confidence:.2f}\n⚡ Reason: Detected spam pattern or flagged keywords."
    else:
        return f"✅ Safe Message\nConfidence: {confidence:.2f}"
