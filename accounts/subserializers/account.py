from rest_framework import serializers
from accounts.models import Account
from accounts.helpers import validate_email


#https://stackoverflow.com/questions/44063644/django-rest-framework-serializer-different-fields-in-multiple-views
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` and 'exclude' argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            not_allowed = set(exclude)
            for exclude_name in not_allowed:
                self.fields.pop(exclude_name)


class AccountRegisterSerializer(DynamicFieldsModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'password1', 'registration_state', 'phone_number', 'plan_id', 'groups')
        read_only_fields = ('registration_state', )

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        password1 = validated_data.get('password1', None)

        if password is None:
            raise serializers.ValidationError({
                'password': 'Password must be provided'
            })

        if password1 is None or password != password1:
            raise serializers.ValidationError({
                'password1': "Passwords don't match"
            })

        if username is None or not validate_email(username):
            raise serializers.ValidationError({
                'username': 'A valid email must be provided'
            })

        user = Account(
            username=username,
            registration_state=2  # -> 'step2'
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class AccountRetrieveUpdateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'phone_number', 'plan_id', 'groups', 'registration_state')
        read_only_fields = ('id', 'plan_id', 'groups')

