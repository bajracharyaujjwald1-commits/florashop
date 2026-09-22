from django.shortcuts import get_object_or_404, redirect, render
from apps.payment.models import Transaction, TransactionStatus
from apps.payment.services import initiate_khalti_payment, verify_khalti_payment
from apps.purchase.models import PaymentStatus, Purchase


# apps/payment/views.py

def initiate_payment(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)

    # Ensure name is NEVER empty or blank
    customer_name = (
        request.user.get_full_name().strip()
        if request.user.is_authenticated and request.user.get_full_name()
        else (request.user.username if request.user.is_authenticated else "Customer")
    )

    customer_email = (
        request.user.email
        if request.user.is_authenticated and request.user.email
        else "customer@example.com"
    )

    customer_info = {
        "name": customer_name,
        "email": customer_email,
        "phone": "9812345678",  # Standard valid 10-digit Nepali test number
    }

    # Call Khalti API via service helper
    khalti_response = initiate_khalti_payment(
        amount_rs=purchase.total,
        purchase_id=purchase.id,
        purchase_name=f"Order #{purchase.id} - {purchase.product.name}",
        customer_info=customer_info,
    )

    if "payment_url" in khalti_response and "pidx" in khalti_response:
        Transaction.objects.create(
            purchase=purchase,
            pidx=khalti_response["pidx"],
            amount=int(float(purchase.total)),
            status=TransactionStatus.PENDING,
        )
        return redirect(khalti_response["payment_url"])

    return render(
        request,
        "payment/callback.html",
        {
            "status": "Failed",
            "message": f"Khalti Error: {khalti_response}",
            "purchase": purchase,
        },
    )


def payment_callback(request):
    pidx = request.GET.get("pidx")
    status = request.GET.get("status")
    transaction = None
    purchase = None
    verification_data = {}
    if pidx:
        transaction = Transaction.objects.filter(pidx=pidx).first()
        if transaction:
            purchase = transaction.purchase

    if pidx and status == "Completed":
        remote_status = str(verification_data.get("status", "")).lower()
        verification_data = verify_khalti_payment(pidx)

        if verification_data.get("status") == "Completed":
            # Update Transaction
            transaction.status = TransactionStatus.COMPLETED
            transaction.save()

            # Update Purchase Model
            purchase = transaction.purchase
            purchase.is_purchase_verified = True
            purchase.payment_status = PaymentStatus.PAID
            purchase.save()

            context = {
                "purchase": purchase,
                "transaction": transaction,
                "status": "Completed",
            }
            # Correct render syntax with request and template path
            return render(request, "payment/callback.html", context)

    # Fallback if verification fails or payment was canceled
    if purchase:
        purchase.payment_status = PaymentStatus.CANCELLED
        purchase.save()
        transaction.status = TransactionStatus.FAILED
        transaction.save()

    return render(
        request,
        "payment/callback.html",
        {
            "status": "Failed",
            "message": "Payment verification failed or was canceled.",
            "purchase":purchase,
            "transaction":transaction,
        },
    )

    # If verification failed or was canceled, grab transaction if pidx exists
    purchase = None
    if pidx:
        transaction = Transaction.objects.filter(pidx=pidx).first()
        if transaction:
            purchase = transaction.purchase

    return render(
        request,
        "payment/callback.html",
        {
            "status": "Failed",
            "message": "Payment verification failed or was canceled.",
            "purchase": purchase,
        },
    )