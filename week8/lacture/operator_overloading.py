#operator overloading 
class Vault:
    def __init__(self,g,s,k):
        self.g = g
        self.s = s
        self.k = k 
    def __str__(self):
        return f"{self.g} gal, {self.s} sik, {self.k} knut"
    
    def __add__(self, other):
        g = self.g + other.g
        s = self.s + other.s
        k = self.k + other.k

        return Vault(g,s,k)
    
def main():
    v1 = Vault(120,40,80)
    v2 = Vault(80,200,30)
    v3 = Vault(120,40,40)
    print(v1)
    print(v2)
    total = v1 + v2 + v3
    print(total)
    print(dir(v1))

if __name__ == "__main__":
    main()