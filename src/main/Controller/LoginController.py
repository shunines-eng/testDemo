from typing import Optional

# 仅管理员可以登录
class Manager:
    def __init__(self):
        self.is_manager = False
    
    @property
    def is_manager(self) -> bool:
        return self._is_manager
    
    @is_manager.setter
    def is_manager(self, value: bool) -> None:
        self._is_manager = value

    @property
    def get_roles(self) -> list[str]:
        """获取当前管理者的角色列表"""
        if not hasattr(self, '_roles'):
            self._roles = set()
        return list(self._roles)
    
    def _manage_check(self):
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
            if not self.is_manager and success:
                print("\n" + "-" * 30)
                show_message("请使用管理员登录")
                return None
                
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
# 根据实际情况调整可用函数和变量

print("运行示例：")  # 输出提示信息
```

```
def show_message(message):
    """显示消息"""
    print("\n" + "-" * 30)
    print(message)
    print("-" * 30 + "\n")

# 增加可选参数
show_message("long message", "short message")


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
