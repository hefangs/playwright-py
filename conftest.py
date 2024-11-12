# conftest.py
# log_file = ./logs/test.log 已经存在pytest.ini中
# 在 conftest.py 里面重新定义
import datetime


def pytest_configure(config):
	# 配置 pytest设置日志文件名
	current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	log_file = f"./logs/{current_time}.log"
	config.option.log_file = log_file
