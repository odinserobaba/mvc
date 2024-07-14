from textual.app import App
from textual.widgets import Header, Footer, ScrollView, Button, Static
from controllers.log_controller import LogController
from controllers.kafka_controller import KafkaController
from controllers.endpoint_controller import EndpointController
import json


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.log_controller = LogController(namespace='default')
        self.kafka_controller = KafkaController(
            brokers=['localhost:9092'], topic='my_topic')
        self.endpoint_controller = EndpointController(
            endpoints=['http://example.com/api'])

    async def on_mount(self) -> None:
        self.body = ScrollView()
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(self.body, edge="left", size=50)

        button = Button(label="Collect Logs", name="collect_logs")
        button.on_click = self.collect_logs
        await self.body.update(button)

        button = Button(label="Process Kafka Messages", name="process_kafka")
        button.on_click = self.process_kafka
        await self.body.update(button)

        button = Button(label="Call Endpoints", name="call_endpoints")
        button.on_click = self.call_endpoints
        await self.body.update(button)

    async def collect_logs(self) -> None:
        self.log_controller.collect_logs()
        await self.body.update(Static("Logs collected!"))

    async def process_kafka(self) -> None:
        self.kafka_controller.process_messages()
        await self.body.update(Static("Kafka messages processed!"))

    async def call_endpoints(self) -> None:
        self.endpoint_controller.call_endpoints()
        await self.body.update(Static("Endpoints called!"))

    async def display_json(self, json_data: str) -> None:
        data = json.loads(json_data)
        formatted_json = json.dumps(data, indent=4)
        await self.body.update(Static(formatted_json))
