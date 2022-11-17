class UserModel:
    def __init__(self) -> None:
        pass

class User:
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, UID, item: UserModel):
        self.users[UID] = item

    def remove_user(self, UID):
        del self.users[UID]

    def modify_user(self, UID):
        pass
        
class SubscriptionModel:
    def __init__(self, args) -> None:
        self.streaming_service: str = args['streaming_service']
        self.plan_name: str = args['plan_name']
        self.plan_price: int = args['plan_price']

class Subscription:
    def __init__(self) -> None:
        self.subscriptions = {}

    def add_subscription(self, subID, item: SubscriptionModel):
        self.subscriptions[subID] = item

    def remove_subscription(self, subID):
        del self.subscriptions[subID]

class MediaModel:
    def __init__(self, args) -> None:
        self.titleType: str = args['titleType']
        self.primaryTitle: str = args['primaryTitle']
        self.originalTitle: str = args['originalTitle']
        self.isAdult: bool = args['isAdult'] if 'isAdult' in args else None
        self.startYear: int = args['startYear'] if 'startYear' in args else None
        self.endYear: int = args['endYear'] if 'endYear' in args else None
        self.runtimeMinutes: int = args['runtimeMinutes'] if 'runtimeMinutes' in args else None
        self.genres: list[str] = args['genres'] if 'genres' in args else None

class Media:
    def __init__(self) -> None:
        self.media = {}

    def add_media(self, tconst, item: MediaModel):
        self.media[tconst] = item

    def remove_media(self, tconst):
        del self.media[tconst]



