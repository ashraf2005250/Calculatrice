# calc_simple.py
import operator

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def main():
    raw = input("Entrez un calcul (ex: 2 +3): ").strip()
    
    a_str, op, b_str = raw.split() # suppose "a op b"
    
    a, b = float(a_str), float(b_str)
    
    if op not in OPS:
        raise ValueError(f"Opérateur inconnu: {op}")
    
    
    print(OPS[op](a, b))
    
    
if __name__ == "__main__":
    main()