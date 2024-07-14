from textual.app import App
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Vertical, Horizontal
from textual.reactive import Reactive
import json

from controllers.log_controller import LogController
from controllers.kafka_controller import KafkaController
from controllers.endpoint_controller import EndpointController


class MyApp(App):
    show_message: Reactive[str] = Reactive("")

    def __init__(self, ssh_host, ssh_user, ssh_key_path, kafka_topic, endpoints):
        super().__init__()
        self.log_controller = LogController(
            ssh_host, ssh_user, ssh_key_path, namespace='default')
        self.kafka_controller = KafkaController(
            ssh_host, ssh_user, ssh_key_path, kafka_topic)
        self.endpoint_controller = EndpointController(endpoints)

    async def on_mount(self) -> None:
        # Create Header and Footer
        header = Header()
        footer = Footer()

        # Create containers for the left side (buttons) and the right side (displays)
        self.button_container = Vertical(
            Button(label="Collect Logs", name="collect_logs"),
            Button(label="Process Kafka Messages", name="process_kafka"),
            Button(label="Call Endpoints", name="call_endpoints"),
            id="buttons",
        )

        self.message_display = Static(
            self.show_message, name="message_display")
        self.json_display = Static(name="json_display")

        self.main_container = Vertical(
            self.message_display,
            self.json_display
        )

        # # Add Header and Footer to the main view

        # await self.on_mount.add_widget(header)
        # await self.on_mount.add_widget(footer)

        # # Add the left side container with the buttons
        # await self.root.add_widget(self.button_container)

        # # Add the main content area
        # await self.root.add_widget(self.main_container)

        # Bind button events to methods
        self.button_container.query_one(
            name="collect_logs").on_click = self.collect_logs
        self.button_container.query_one(
            name="process_kafka").on_click = self.process_kafka
        self.button_container.query_one(
            name="call_endpoints").on_click = self.call_endpoints

    async def on_button_pressed(self, button: Button) -> None:
        if button.name == "collect_logs":
            await self.collect_logs()
        elif button.name == "process_kafka":
            await self.process_kafka()
        elif button.name == "call_endpoints":
            await self.call_endpoints()

    async def collect_logs(self) -> None:
        self.log_controller.collect_logs()
        self.show_message = "Logs collected!"
        await self.update_message_display()

    async def process_kafka(self) -> None:
        self.kafka_controller.process_messages()
        self.show_message = "Kafka messages processed!"
        await self.update_message_display()

    async def call_endpoints(self) -> None:
        self.endpoint_controller.call_endpoints()
        self.show_message = "Endpoints called!"
        await self.update_message_display()

    async def display_json(self, json_data: str) -> None:
        data = json.loads(json_data)
        formatted_json = json.dumps(data, indent=4)
        await self.json_display.update(formatted_json)

    async def update_message_display(self) -> None:
        await self.message_display.update(self.show_message)


if __name__ == "__main__":
    ssh_host = 'localhost'
    ssh_user = 'user'
    ssh_key_path = 'path_to_your_ssh_key'
    kafka_topic = 'test_topic'
    endpoints = ['http://example.com/api']

    app = MyApp(ssh_host, ssh_user, ssh_key_path, kafka_topic, endpoints)
    app.run()
