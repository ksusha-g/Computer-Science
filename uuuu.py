class StreamingSubscription:
    def __init__(self, name, subtype, activation, qual, number):
        self.name = name
        self.subtype = subtype
        self.activation = activation
        self.qual = qual
        self.number = number

    def __str__(self):
        return f"{self.name}\n{self.subtype}\n{self.activation}\n{self.qual}\n{self.number}"

    def check_sub(self):
        if (self.activation):
            return("Subscription is active!!")
        else:
            return("Needed to pay!")

    def check_qual(self):
        if (self.qual == "4K"):
            return("4K is avaliable")
        else:
            return("4K is not avaliable")

    def check_numb(self):
        return( f"Max devices: {self.number}")

profile = StreamingSubscription("Katyub", "Premium", True, "4K", 4)
print(profile.check_sub())
print(profile.check_qual())
print(profile.check_numb())
print(profile)
