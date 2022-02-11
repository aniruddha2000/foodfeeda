from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
)
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import NGO, Donner


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token["email"] = user.email

        return token


class DonnerDetailSerializer(ModelSerializer):
    class Meta:
        model = Donner
        exclude = (
            "is_superuser",
            "is_staff",
            "last_login",
            "password",
            "country",
            "user_permissions",
            "groups",
        )


class NGODetailSerializer(ModelSerializer):
    class Meta:
        model = NGO
        exclude = (
            "is_superuser",
            "is_staff",
            "last_login",
            "password",
            "country",
            "user_permissions",
        )


class DonnerRegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=Donner.objects.all())]
    )

    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = Donner
        fields = (
            "id",
            "email",
            "password",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            # "country",
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
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Donner.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            state=validated_data["state"],
            city=validated_data["city"],
            pin=validated_data["pin"],
            DOB=validated_data["DOB"],
            profile_photo=validated_data["profile_photo"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class NGORegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=Donner.objects.all())]
    )

    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = NGO
        fields = (
            "id",
            "email",
            "password",
            "password2",
            "name",
            "phone_number",
            # "country",
            "state",
            "city",
            "pin",
            "ngo_approval_cert",
        )
        extra_kwargs = {
            "name": {"required": True},
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = NGO.objects.create(
            email=validated_data["email"],
            name=validated_data["name"],
            phone_number=validated_data["phone_number"],
            # country=validated_data["country"],
            state=validated_data["state"],
            city=validated_data["city"],
            pin=validated_data["pin"],
            ngo_approval_cert=validated_data["ngo_approval_cert"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class DonnerChangePasswordSerializer(ModelSerializer):
    password = CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)
    old_password = CharField(write_only=True, required=True)

    class Meta:
        model = Donner
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class NGOChangePasswordSerializer(ModelSerializer):
    password = CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)
    old_password = CharField(write_only=True, required=True)

    class Meta:
        model = NGO
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
