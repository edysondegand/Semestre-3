class Heure:
    """Représente une heure de la journée (h, m, s)."""
    
    def __init__(self, h: int, m: int, s: int):
        # TODO: Initialiser et valider les attributs
        if h>24 or h<0:
            raise ValueError("Pas dans la gamme")
        if m>59 or m<0:
            raise ValueError("Pas dans la gamme de minute")
        if s>59 or s<0:
            raise ValueError("Pas dans la gamme de seconde")
        
        self.h=h
        self.m=m
        self.s=s

    @classmethod
    def from_secondes(cls, total_secondes: int) -> "Heure":
        # TODO: Calculer h, m, s et retourner une nouvelle instance `cls(...)`
        total=total_secondes%(24*3600)
        h, r=divmod(total,3600)
        m,s=divmod(r,60)
        return cls(h,m,s)
    
    def __repr__(self) -> str:
        # TODO
        return f"Heure{self.h,self.m,self.s}"

    def __str__(self) -> str:
        # TODO
        return f"{self.h}:{self.m}:{self.s}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Heure):
            return NotImplemented
        # TODO: Comparer self et other
        return (self.h,self.m,self.s)==(other.h,other.m,other.s)

# --- Tests à valider ---
h1 = Heure(1, 1, 1)
print(f"repr(h1): {repr(h1)}")
print(f"str(h1): {str(h1)}")

# Test du classmethod
total_secs = 3661 # 1 heure, 1 minute, 1 seconde
h2 = Heure.from_secondes(total_secs)
assert h2.h == 1 and h2.m == 1 and h2.s == 1

# Test de l'égalité
h3 = Heure(1, 1, 1)
assert h1 == h2
assert h1 == h3
assert h2 != Heure(1, 1, 2)

print("Tests de l'exercice 4 passés avec succès !")