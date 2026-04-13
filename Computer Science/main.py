class CloudStorage():

    maxStorage = 100

    def __init__(self, usedStorage):
        self.usedStorage = usedStorage

    def checkStorage(self):
        if (self.maxStorage - self.usedStorage) > 0:
            return f'Всего: {self.maxStorage} гб\nДоступно: {self.maxStorage - self.usedStorage} гб'
        else: 
            return f'Свободное место закончилось\nЛимит превышен на {abs(self.maxStorage - self.usedStorage)} гб'


user1 = CloudStorage(54)
user2 = CloudStorage(116)

print(user1.checkStorage())
print(user2.checkStorage())

CloudStorage.maxStorage = 200

print(user1.checkStorage())
print(user2.checkStorage())
