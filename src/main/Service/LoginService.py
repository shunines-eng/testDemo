class LoginService:
    def __init__(self):
        self.user_repo = UserRepository()

    def login(self, username, password):
        """处理登录验证逻辑"""
        user = self.user_repo.get_user(username)

        if not user:
            return (False, "用户不存在")
        if user['password'] != password:
            return (False, "密码错误")
        return (True, f"{user['role']}登录成功")
