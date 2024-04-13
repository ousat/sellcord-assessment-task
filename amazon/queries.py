from amazon.models import Customer, Order, Return, Dispute


def create_customer(data):
    """
    add entry to customer model
    """
    try:
        customer = Customer.objects.create(name=data["name"], address=data["address"])
        return customer.id, 1
    except Exception:
        return "Error", 0


def list_customers():
    """
    list all entries in customer model
    """
    return list(Customer.objects.values("id", "name", "address"))


def create_order(data):
    """
    add entry to orders model
    """
    try:
        customer = Customer.objects.get(id=data["customer_id"])
        order_entry = Order.objects.create(item=data["item"], customer_details=customer)
        return str(order_entry.order_id), 1
    except Exception:
        return "Error", 0


def list_orders():
    """
    list entries from order model
    """
    return list(
        Order.objects.values(
            "order_id", "item", "customer_details__id", "customer_details__name"
        )
    )


def create_return(data):
    """
    add entry to return model
    """
    try:
        original_order = Order.objects.get(order_id=data["order_id"])
        return_entry = Return.objects.create(
            original_order=original_order, return_reason=data["return_reason"]
        )
        return str(return_entry.return_id), 1
    except Exception:
        return "Error", 0


def list_returns():
    """
    list entries in returns model
    """
    return list(
        Return.objects.values(
            "return_id", "return_reason", "return_tracking", "original_order__order_id"
        )
    )


def create_dispute(data):
    """
    create entry in dispute model
    """
    try:
        original_order = Order.objects.get(order_id=data["order_id"])
        dispute_entry = Dispute.objects.create(
            original_order=original_order, dispute_reason=data["dispute_reason"]
        )

        return str(dispute_entry.dispute_id), 1
    except Exception:
        return "Error", 0


def list_disputes():
    """
    list values from dispute model
    """
    disputes = list(
        Dispute.objects.values(
            "dispute_id",
            "original_order__item",
            "original_order__order_id",
            "original_order__customer_details__name",
            "dispute_reason",
            "status_tracking",
            "resolution",
            "created_at",
            "updated_at",
        )
    )
    return disputes
