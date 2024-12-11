def query_by_date(obj, obj_serializer, date_range):

    obs = obj.objects.filter(
        created_at__gte=date_range[1], created_at__lte=date_range[0]
    ).order_by("created_at")
    
    
    
    serialized_objects = obj_serializer(obs, many=True)

    
    return serialized_objects.data


def query_by_date_membership_earnings(obj, obj_serializer, date_range):
    
    obs = obj.objects.filter(
        registered_at__gte=date_range[1], registered_at__lte=date_range[0]
    ).order_by("registered_at")
    
    
    
    serialized_objects = obj_serializer(obs, many=True)

    
    return serialized_objects.data

def query_by_date_product_earnings(obj, obj_serializer, date_range):
    
    obs = obj.objects.filter(
        purchased_at__gte=date_range[1], purchased_at__lte=date_range[0]
    ).order_by("purchased_at")
    
    
    
    serialized_objects = obj_serializer(obs, many=True)

    
    return serialized_objects.data