from rest_framework import serializers


class AddressSerializer(serializers.Serializer):

    address = serializers.CharField(max_length=100)
    output_format = serializers.ChoiceField(choices=["xml", "json"])
    