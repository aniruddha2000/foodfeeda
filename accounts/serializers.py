from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
    ValidationError,
)
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from accounts.models import Donner, NGO


class DonnerRegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=Donner.objects.all())]
    )

    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = Donner
        fields = (
            "email",
            "password",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            "country",
            "state",
            "city",
            "pin",
            "DOB",
            "profile_photo",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Donner.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class NGORegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=Donner.objects.all())]
    )

    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = NGO
        fields = (
            "email",
            "password",
            "password2",
            "name",
            # "phone_number",
            # "country",
            # "state",
            # "city",
            # "pin",
            # "ngo_approval_cert",
        )
        extra_kwargs = {
            "name": {"required": True},
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = NGO.objects.create(
            email=validated_data["email"],
            name=validated_data["name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
