from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/ping", verify=False)
        self.client.get("/api/version", verify=False)
