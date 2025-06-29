import datetime
import os


class Logger():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logs_file = os.path.join(project_dir, 'logs', f'{datetime.datetime.now().strftime('%d.%m.%Y-%H.%M.%S')}.log')

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.logs_file, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += f"\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):
        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)
