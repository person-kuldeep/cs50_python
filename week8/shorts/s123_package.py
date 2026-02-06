class Package:
    def __init__(self,id,sender,receiver,weight):
        self.id = id 
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
    
    def __str__(self):
        return f"Package {self.id}: {self.sender} to {self.receiver} of {self.weight} kg --> costs: ${self.shipping_cost(1.5)}"
    def shipping_cost(self, cost_per_kg):
        return self.weight * cost_per_kg
    
def main():
    packages = [
        Package(1,"a","b",10),
        Package(2,"v","k",3)
    ]
    for package in packages:
        print(package)

if __name__ == "__main__":
    main()