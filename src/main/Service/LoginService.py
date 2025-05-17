# 增加注释以帮助其他开发者理解该服务类的登录逻辑
"""
@brief 该service类负责用户登录验证 logic

@param username: 必须指定的唯一标识符（username），可能是字符串或某种可比较类型的值
@param password: 需要的唯一密码（password），通常是字符串类型
返回值:
tuple，包含布尔值和角色名对应的成功信息
"""
class AuthService:
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
