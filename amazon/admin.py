from django.contrib import admin
from amazon.models import Customer, Order, Return, Dispute

# Register your models here.


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Return)
admin.site.register(Dispute)
