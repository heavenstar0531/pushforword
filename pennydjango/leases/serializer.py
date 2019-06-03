from rest_framework import serializers

from penny.serializers import AgentSerializer
from listings.serializer import PrivateListingSerializer
from leases.models import Lease


# Serializers define the API representation.
class LeaseSerializer(serializers.ModelSerializer):
    listing = PrivateListingSerializer()
    status = serializers.CharField(source='get_status_display')
    created_by = AgentSerializer()

    class Meta:
        model = Lease
        fields = (
            'id', 'short_id', 'listing', 'offer', 'length_of_lease',
            'move_in_date', 'op', 'total_broker_fee', 'status', 'created_by',
            'created', 'modified', 'detail_link'
        )
