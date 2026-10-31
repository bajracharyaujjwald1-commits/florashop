import requests
from django.conf import settings


def initiate_khalti_payment(
    amount_rs, purchase_id, purchase_name, customer_info
):
    """Initiates payment with Khalti API and returns pidx & payment_url.

    Note: Khalti requires the amount in PAISA (1 NPR = 100 Paisa).
    """
    # Safe conversion from Decimal/Float to Paisa Integer
    amount_paisa = int(float(amount_rs) * 100)

    payload = {
        "return_url": settings.KHALTI_RETURN_URL,
        "website_url": settings.KHALTI_WEBSITE_URL,
        "amount": amount_paisa,
        "purchase_order_id": str(purchase_id),
        "purchase_order_name": purchase_name,
        "customer_info": {
            "name": customer_info.get("name", "Customer"),
            "email": customer_info.get("email", "customer@example.com"),
            "phone": 9800000005,
        },
    }

    # 'Key' MUST be capitalized in Khalti's Authorization header
    headers = {
        "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            settings.KHALTI_INITIATE_URL,
            headers=headers,
            json=payload,  # requests handles json.dumps automatically
            timeout=10,
        )
        data = response.json()

        # Debug print to terminal if Khalti responds with an error status
        if response.status_code != 200:
            print("--- KHALTI INITIATE ERROR ---")
            print("Status Code:", response.status_code)
            print("Response:", data)
            print("----------------------------")

        return data
    except requests.exceptions.RequestException as e:
        print("Khalti Request Exception:", e)
        return {"error": str(e)}


def verify_khalti_payment(pidx):
    """Queries Khalti's Lookup API to verify transaction status on the backend."""
    payload = {"pidx": pidx}
    headers = {
        "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            settings.KHALTI_LOOKUP_URL,
            headers=headers,
            json=payload,
            timeout=10,
        )
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}