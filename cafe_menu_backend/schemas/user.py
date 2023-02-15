from cafe_menu_backend.extensions import ma


class UserSchema(ma.Schema):
    github_login = ma.Str(required=True)
    name = ma.Str(required=True)
    avatar = ma.Str()

    class Meta:
        fields = (
            "github_login",
            "name",
            "avatar",
        )


user_schema = UserSchema()
