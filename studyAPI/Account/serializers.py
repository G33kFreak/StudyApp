from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    EmailField,
    CharField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

User = get_user_model()

class UserCreateSeriaizer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        ]

        extra_kwargs = {"password":
                            {"write_only": True}
                        }
        
        def create(self, validated_data):
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            first_name = validated_data['first_name']
            last_name = validated_data['last_name']
            user_obj = User(
                username = username,
                email = email,
                first_name = first_name,
                last_name = last_name
            )

            user_obj.set_password(password)
            user_obj.save()
            return validated_data

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(required=False)
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self, data):
        email = data.get("email", None)
        password = data["password"]
        if not email:
            raise ValidationError("Incorrect email")

        user = User.objects.filter(
            Q(email=email)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Incorrect email")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password, please try again")

        data["token"] = "RANDOM TOKEN"

        return data