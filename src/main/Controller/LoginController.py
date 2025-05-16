def show_message(message):
    """显示消息"""
    print("\n" + "-"*30)
    print(message)
    print("-"*30 + "\n")


def get_input():
    """获取用户输入"""
    username = input("用户名：").strip()
    password = input("密码：").strip()
    return username, password


class LoginCLI:
    def __init__(self):
        self.auth_service = AuthService()

    def run(self):
        """主程序循环"""
        while True:
            username, password = get_input()
            success, message = self.auth_service.login(username, password)
            show_message(message)
            if success:
                break