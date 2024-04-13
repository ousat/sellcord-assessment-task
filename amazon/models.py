import uuid
from django.db import models

# choice values for return tracking status
RETURN_TRACKING_CHOICES = ((1, "INITIATED"), (2, "IN PROGRESS"), (3, "RETURNED"))

# choice values for dispute tracking status
DISPUTE_TRACKING_CHOICES = (
    (1, "RAISED"),
    (2, "ACTIVE"),
    (3, "INACTIVE"),
    (4, "CLOSED"),
    (5, "DUPLICATE"),
)


# common columns in all models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# model for customers
class Customer(BaseModel):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField()


# model for orders
class Order(BaseModel):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=50)
    customer_details = models.ForeignKey("Customer", on_delete=models.CASCADE)


# model for returns
class Return(BaseModel):
    return_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    return_reason = models.TextField()
    return_tracking = models.IntegerField(choices=RETURN_TRACKING_CHOICES, default=1)
    original_order = models.ForeignKey("Order", on_delete=models.CASCADE)


# model for disputes
class Dispute(BaseModel):
    dispute_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original_order = models.ForeignKey("Order", on_delete=models.CASCADE)
    dispute_reason = models.TextField()
    status_tracking = models.IntegerField(choices=DISPUTE_TRACKING_CHOICES, default=1)
    resolution = models.TextField(max_length=100)
