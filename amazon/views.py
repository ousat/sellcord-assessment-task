import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from amazon.queries import (
    create_customer,
    list_customers,
    create_order,
    list_orders,
    create_dispute,
    list_disputes,
    create_return,
    list_returns,
)

DISPUTE_STATUS = ["RAISED", "ACTIVE", "INACTIVE", "CLOSED", "DUPLICATE"]


def disputes_page(request):
    """
    render dispute page
    """
    return render(request, "disputes.html")


@csrf_exempt
def save_customer(request):
    """
    save customer API
    """
    data = json.loads(request.body)
    customer_id, status = create_customer(data)
    if status == 0:
        return JsonResponse(
            {"error": "failed to create customer, please check the values"}
        )
    return JsonResponse({"id": str(customer_id)})


@csrf_exempt
def get_customers(request):
    """
    get customers API
    """
    data = list_customers()
    return JsonResponse({"customers": data})


@csrf_exempt
def save_order(request):
    """
    save order API
    """
    data = json.loads(request.body)
    order_id, status = create_order(data)
    if status == 0:
        return JsonResponse(
            {"error": "failed to create order, please check the values"}
        )
    return JsonResponse({"id": str(order_id)})


@csrf_exempt
def get_orders(request):
    """
    get orders API
    """
    data = list_orders()
    return JsonResponse({"orders": data})


@csrf_exempt
def save_return(request):
    """
    save return API
    """
    data = json.loads(request.body)
    return_id, status = create_return(data)
    if status == 0:
        return JsonResponse(
            {"error": "failed to create return, please check the values"}
        )
    return JsonResponse({"id": str(return_id)})


@csrf_exempt
def get_returns(requst):
    """
    get returns API
    """
    data = list_returns()
    return JsonResponse({"returns": data})


@csrf_exempt
def save_dispute(request):
    """
    save dispute API
    """
    data = json.loads(request.body)
    dispute_id, status = create_dispute(data)
    if status == 0:
        return JsonResponse(
            {"error": "failed to create order, please check the values"}
        )
    return JsonResponse({"id": str(dispute_id)})


def get_disputes(requst):
    """
    returns list of disputes in html table format
    """
    data = list_disputes()
    if len(data) > 0:
        response = "<table><thead><tr><td>Dispute Id</td><td>Customer Name</td><td>Item Id</td><td>Item Name</td><td>Dispute Reason</td><td>Dispute Tracking Status</td><td>Resolution</td><td>Create Time</td><td>Last Update Time</td></tr></thead><tbody>"
        for entry in data:
            response = (
                response
                + f"<tr><td>{str(entry['dispute_id'])} </td>"
                + f"<td>{entry['original_order__customer_details__name']}</td>"
                + f"<td>{str(entry['original_order__order_id'])} </td>"
                + f"<td> {entry['original_order__item']}</td>"
                + f"<td> {entry['dispute_reason']}</td>"
                + f"<td>{DISPUTE_STATUS[entry['status_tracking'] - 1]}</td>"
                + f"<td>{entry['resolution']}</td>"
                + f"<td>{(entry['created_at'].strftime('%m/%d/%Y  %H:%M:%S'))}</td>"
                + f"<td>{(entry['updated_at'].strftime('%m/%d/%Y  %H:%M:%S'))}</td></tr>"
            )
        response = response + "</tbody></table>"
    else:
        response = ""
    return HttpResponse(response)
