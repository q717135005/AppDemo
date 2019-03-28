import allure


class Test_001:

    @allure.step(title="我是第一个测试步骤的名字")
    def test_001(self):
        # allure.attach("我是步骤描述", "我是具体描述的内容")  # 默认生成.txt文件
        allure.attach("我是步骤描述", "我是具体描述的内容", allure.attach_type.TEXT)
        print("-->test_001")
        assert True

    @allure.step(title="测试步骤xx")
    def test002(self):
        with open("./screen/data.png", "rb") as f:
            # 将图片添加到测试报告
            allure.attach("图片名字", f.read(), allure.attach_type.PNG)
        assert True
