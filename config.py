from typing import Self, Optional
from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow',
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",  # разделитель для вложенных переменных
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig

    # test_data: Optional[TestDataConfig] = None
    # http_client: Optional[HTTPClientConfig] = None

    allure_results_dir: DirectoryPath

    @classmethod
    def initialize(cls) -> Self:  # Возвращает экземпляр класса Settings
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует

        # test_cfg = TestDataConfig(image_png_file=FilePath("./testdata/files/image.png"))
        # http_cfg = HTTPClientConfig(url=HttpUrl("http://localhost:8000"), timeout=100.0)


        # Передаем allure_results_dir в инициализацию настроек
        return Settings(allure_results_dir=allure_results_dir)

        # return Settings(
        #     test_data=test_cfg,
        #     http_client=http_cfg,
        #     allure_results_dir=allure_results_dir
        # )


settings = Settings.initialize()


