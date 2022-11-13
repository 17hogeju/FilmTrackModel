class User:
    def __init__(self, email, uid) -> None:
        self.watched = {}
        self.to_watch = {}
        self.subscriptions = {}
        self.username = email
        self.__uid = uid
        
    def modify_watched(self):
        pass
    def modify_to_watch(self):
        pass
    def modify_subscription(self):
        pass
    def modify_username(self):
        pass

class Subscription:
    def __init__(self, service_name, plans) -> None:
        self.service_name = service_name
        self.plans = plans

    def modify_plans(self):
        pass

class Media:
    def __init__(self, primary_title, original_title, title_type, genres) -> None:
        self.primary_title = primary_title
        self.original_title = original_title
        self.title_type = title_type
        self.genres = genres
