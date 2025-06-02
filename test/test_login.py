import unittest
from unittest.mock import MagicMock
from main.Service.LoginService import LoginService
from main.Dao.LoginDao import LoginDao

class TestLoginService(unittest.TestCase):
    """登录服务单元测试"""
    
    def setUp(self):
        """初始化测试环境"""
        self.mock_db = MagicMock()
        self.dao = LoginDao(self.mock_db)
        self.service = LoginService(self.mock_db)
        
    def test_valid_login(self):
        """测试有效登录"""
        self.dao.validate_user = MagicMock(return_value=(True, ""))
        success, message = self.service.login("admin", "123456")
        self.assertTrue(success)
        self.assertIn("登录成功", message)
        
    def test_invalid_password(self):
        """测试错误密码"""
        self.dao.validate_user = MagicMock(return_value=(False, "密码错误"))
        success, message = self.service.login("admin", "wrong")
        self.assertFalse(success)
        self.assertEqual("密码错误", message)

if __name__ == "__main__":
    unittest.main()
