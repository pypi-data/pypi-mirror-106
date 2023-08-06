from circle.resources.abstract import CreateableAPIResource


class Subscription(CreateableAPIResource):
    OBJECT_NAME = "notifications.subscriptions"
