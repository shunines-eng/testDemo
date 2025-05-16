def show_message(message):
    """显示消息"""
    print("\n" + "-" * 30)
    print(message)
    print("-" * 30 + "\n")

# 增加可选参数
show_message("long message", "short message")


def get_input():
    """获取用户输入"""
    username = input("用户名：").strip()
    password = input("密码：").strip()
    return username, password


class LoginCLI:
    def __init__(self):
        self.auth_service = AuthService()
        
    @property
    def login_message(self):
        """获取和显示登录消息"""
        if not hasattr(self, 'show_message'):
            self.show_message("请点这里...", "请重新输入你的信息")
        
        return self.show_message
        

    def run(self):
        """主程序循环"""
        while True:
            username, password = get_input()
            success, message = self.auth_service.login(username, password, max_attempts=3)
            # 根据成功的状态决定输出内容
            if success:
                print("\n" + "-" * 30)
                print(f"用户{'成功登录' if success else '失败'}")
                print(message or "未成功登录")
                print("-"*30 + "\n")
            elif not success:
                print("尝试再次登录，已尝试三次")
            else:
                break
