class Profile:
    def __init__(self, name, list_interest):
        self.list_interest = list_interest
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.list_interest}"
    
    def count(self):
        return(len(self.list_interest))
        
    def check(self, interest):
        if(interest in self.list_interest):
            return("Yes")
        else:
            return("No")

profile = Profile("Lox", ["sleep", "eat", "tikTk", "fart"])
print(profile.count())
print(profile.check("sleep"))
print(profile)
