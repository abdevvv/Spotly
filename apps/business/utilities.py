from rest_framework.validators import ValidationError


from apps.business.models import Business


def get_business(business_id):
        business = Business.objects.filter(id=business_id,is_activated=True)
        if not business.exists():
            raise ValidationError({'detail':"The business is not valid"})
        business = business.first()
        return business