from dataclasses import field
import email
import imp
from multiprocessing import AuthenticationError
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import (
    CharField, EmailField, ModelSerializer, Serializer, ValidationError)
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.exceptions import AuthenticationFailed
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from accounts.models import NGO, CustomUser, Donner


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token["email"] = user.email
        token["type"] = user.type

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
            "type",
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
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Donner.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            type=validated_data["type"],
            country=validated_data["country"],
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
            "type",
            "country",
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
            type=validated_data["type"],
            phone_number=validated_data["phone_number"],
            country=validated_data["country"],
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


class DonnerUpdateUserSerializer(ModelSerializer):

    class Meta:
        model = Donner
        fields = (
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

    def validate_email(self, value):
        user = self.context['request'].user
        if Donner.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.phone_number = validated_data['phone_number']
        instance.country = validated_data['country']
        instance.state = validated_data['state']
        instance.city = validated_data['city']
        instance.pin = validated_data['pin']
        instance.DOB = validated_data['DOB']
        instance.profile_photo = validated_data['profile_photo']

        instance.save()

        return instance


class NGOUpdateUserSerializer(ModelSerializer):

    class Meta:
        model = NGO
        fields = (
            "name",
            "phone_number",
            "country",
            "state",
            "city",
            "pin",
            "ngo_approval_cert",
        )

    def validate_email(self, value):
        user = self.context['request'].user
        if NGO.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.phone_number = validated_data['phone_number']
        instance.country = validated_data['country']
        instance.state = validated_data['state']
        instance.city = validated_data['city']
        instance.pin = validated_data['pin']
        instance.ngo_approval_cert = validated_data['ngo_approval_cert']

        instance.save()

        return instance


class EmailResetPasswordSerializer(Serializer):
    email = EmailField(min_length=5)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(Serializer):
    password = CharField(min_length=6, max_length=100, write_only=True)
    uidb64 = CharField(min_length=1, write_only=True)
    token = CharField(min_length=1, write_only=True)

    class Meta:
        fields = ["password", "uidb64", "token"]

    def validate(self, attrs):
        try:
            password = attrs.get("password")
            uidb64 = attrs.get("uidb64")
            token = attrs.get("token")

            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("The reset link is invalid", 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed("The reset link is invalid", 401)
