from rest_framework.response import Response
from rest_framework.decorators import api_view

# DATE TIME
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils.timezone import make_aware, is_naive

# SWAGGER
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# CUSTOM
from ..models import Purchase
from ..serializers import PurchaseDepthSerializer
from .general import query_by_date_product_earnings

@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "start_date",
            openapi.IN_QUERY,
            description="Start date for filtering (YYYY-MM-DD format)",
            type=openapi.TYPE_STRING,
            required=True,
        ),
        openapi.Parameter(
            "end_date",
            openapi.IN_QUERY,
            description="End date for filtering (YYYY-MM-DD format)",
            type=openapi.TYPE_STRING,
            required=True,
        ),
    ],
    responses={200: PurchaseDepthSerializer(many=True)},
)
@api_view(["GET"])
def get_product_earnings(request):
    try:
        start_date_str = request.GET["start_date"]
        end_date_str = request.GET["end_date"]
        
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

        if is_naive(start_date):
            start_date = make_aware(start_date)
        if is_naive(end_date):
            end_date = make_aware(end_date)

        
        date_range = [end_date, start_date]
        product_transactions = query_by_date_product_earnings(Purchase, PurchaseDepthSerializer, date_range=date_range)

        product_earnings = 0
        
        for product_transaction in product_transactions:
            product_earnings += float(product_transaction["price"]) * float(product_transaction["quantity"])
        
        return Response({"product_earning": product_earnings, "data": product_transactions})
        
    except (KeyError, ValueError) as e:
        return Response({"error": str(e)}, status=400)

@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "start_date",
            openapi.IN_QUERY,
            description="(YYYY-MM-DD format), Will compute the product_earning starting [Start date] to past month",
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={200: PurchaseDepthSerializer(many=True)},
)
@api_view(["GET"])
def get_product_earnings_by_month(request):
    start_date_str = request.GET.get("start_date")

    try:
        if start_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            if is_naive(start_date):
                start_date = make_aware(start_date)
        else:
            start_date = make_aware(datetime.now())

        end_date = start_date - relativedelta(months=1)
        date_range = [start_date, end_date]

        product_transactions = query_by_date_product_earnings(Purchase, PurchaseDepthSerializer, date_range=date_range)
        
        product_earnings = 0
        
        for product_transaction in product_transactions:
            product_earnings += float(product_transaction["price"]) * float(product_transaction["quantity"])
        
        return Response({"product_earning": product_earnings, "data": product_transactions})
    except ValueError:
        return Response(
            {"error": "Invalid date format. Use YYYY-MM-DD."}, status=400
        )


@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "start_date",
            openapi.IN_QUERY,
            description="(YYYY-MM-DD format), Will compute product_earning starting [Start date] to past year",
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={200: PurchaseDepthSerializer(many=True)},
)
@api_view(["GET"])
def get_product_earnings_by_this_year(request):
    start_date_str = request.GET.get("start_date")

    try:
        if start_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            if is_naive(start_date):
                start_date = make_aware(start_date)
        else:
            start_date = make_aware(datetime.now())

        end_date = start_date - relativedelta(years=1)
        date_range = [start_date, end_date]

        product_transactions = query_by_date_product_earnings(Purchase, PurchaseDepthSerializer, date_range=date_range)

        product_earnings = 0
        
        for product_transaction in product_transactions:
            product_earnings += float(product_transaction["price"]) * float(product_transaction["quantity"])
        
        return Response({"product_earning": product_earnings, "data": product_transactions})
    except ValueError:
        return Response(
            {"error": "Invalid date format. Use YYYY-MM-DD."}, status=400
        )


@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "start_date",
            openapi.IN_QUERY,
            description="(YYYY-MM-DD format), Will compute product_earning starting [Start date] to past week",
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={200: PurchaseDepthSerializer(many=True)},
)
@api_view(["GET"])
def get_product_earnings_by_this_week(request):
    start_date_str = request.GET.get("start_date")

    try:
        if start_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            if is_naive(start_date):
                start_date = make_aware(start_date)
        else:
            start_date = make_aware(datetime.now())

        end_date = start_date - relativedelta(weeks=1)
        date_range = [start_date, end_date]

        product_transactions = query_by_date_product_earnings(Purchase, PurchaseDepthSerializer, date_range=date_range)

        product_earnings = 0
        
        for product_transaction in product_transactions:
            product_earnings += float(product_transaction["price"]) * float(product_transaction["quantity"])
        
        return Response({"product_earning": product_earnings, "data": product_transactions})
    except ValueError:
        return Response(
            {"error": "Invalid date format. Use YYYY-MM-DD."}, status=400
        )

@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "start_date",
            openapi.IN_QUERY,
            description="(YYYY-MM-DD format), Will compute the product_earning today",
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={200: PurchaseDepthSerializer(many=True)},
)
@api_view(["GET"])
def get_product_earnings_by_this_day(request):
    start_date_str = request.GET.get("start_date")

    try:
        if start_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            if is_naive(start_date):
                start_date = make_aware(start_date)
        else:
            start_date = make_aware(datetime.now())

        end_date = start_date - relativedelta(days=1)
        date_range = [start_date, end_date]

        product_transactions = query_by_date_product_earnings(Purchase, PurchaseDepthSerializer, date_range=date_range)

        product_earnings = 0
        
        for product_transaction in product_transactions:
            product_earnings += float(product_transaction["price"]) * float(product_transaction["quantity"])
        
        return Response({"product_earning": product_earnings, "data": product_transactions})
    except ValueError:
        return Response(
            {"error": "Invalid date format. Use YYYY-MM-DD."}, status=400
        )
