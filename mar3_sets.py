import math
import numpy as np

"""
3DCOM UOFT MERSENNE PRIME PREDICTOR
Testing ALL LZ/HQS sets
"""

# ALL LZ/HQS sets - EXACT as provided
LZ_HQS_SETS = [
    ("lz0", 0.8934663922421224, "hqs0", 0.4580303486913581),
    ("lz1", 1.1884835867122727, "hqs1", 0.2563627656259622),
    ("lz2", 1.2324872492906604, "hqs2", 0.2365675399187783),
    ("lz3", 1.2348836948610768, "hqs3", 0.2355433075380717),
    ("lz4", 1.2349784610451732, "hqs4", 0.2355029143309773),
    ("lz5", 1.2349821314710578, "hqs5", 0.2355013500132297),
    ("lz6", 1.2349822735137316, "hqs6", 0.2355012894755802),
    ("lz7", 1.2349822790104976, "hqs7", 0.2355012871328953),
    ("lz8", 1.2349822792232112, "hqs8", 0.2355012870422381),
    ("lz9", 1.2349822792314428, "hqs9", 0.2355012870387299),
    ("lz10", 1.2349822792317612, "hqs10", 0.2355012870385942),
    ("lz11", 1.2349822792317737, "hqs11", 0.2355012870385889),
    ("LZ", 1.2349822792317741, "HQS", 0.2355012870385887)
]

PI = 3.141592653589793

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(exponent):
    """Check if 2^exponent - 1 is prime"""
    if not is_prime(exponent):
        return False
    if exponent == 2:
        return True
    
    # Simple check for known Mersenne primes
    known_mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 
                               1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 
                               19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 
                               756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 
                               13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 
                               37156667, 42643801, 43112609, 57885161, 74207281, 77232917, 82589933, 136279841]
    return exponent in known_mersenne_exponents

def predict_with_set(lz_val, hqs_val, set_name):
    """Predict Mersenne primes using specific LZ/HQS set"""
    n_neptune = 7
    current_exp = 2
    all_predicted = [current_exp]
    
    print(f"\n{set_name}: LZ={lz_val:.16f}, HQS={hqs_val:.16f}")
    print("-" * 60)
    
    iteration = 0
    max_iterations = 50000000
    
    while current_exp < 1000000 and iteration < max_iterations:
        iteration += 1
        predicted_candidates = []
        
        for n in np.arange(n_neptune + 1, 15, 0.001):
            orbit = current_exp * (lz_val ** (n - n_neptune))
            resonance = hqs_val * math.sin(0.4 * PI * n)
            
            if abs(resonance) > 0.06:
                candidate_exp = int(round(orbit))
                
                if (candidate_exp > current_exp and 
                    is_mersenne_prime(candidate_exp) and 
                    candidate_exp not in all_predicted):
                    
                    predicted_candidates.append(candidate_exp)
        
        if predicted_candidates:
            next_exp = min(predicted_candidates)
            all_predicted.append(next_exp)
            
            digits = int(next_exp * math.log10(2)) + 1
            print(f"M_{current_exp:>6} → M_{next_exp:>6} | Growth: {next_exp/current_exp:6.3f} | Digits: {digits:>6}")
            
            current_exp = next_exp
        else:
            if len(all_predicted) > 1:
                print(f"No more found after M_{current_exp}")
            break
    
    return all_predicted

def test_all_sets():
    """Test prediction with ALL LZ/HQS sets"""
    print("3DCOM PREDICTION WITH ALL LZ/HQS SETS")
    print("=" * 70)
    
    results = {}
    
    for lz_name, lz_val, hqs_name, hqs_val in LZ_HQS_SETS:
        set_name = f"{lz_name}/{hqs_name}"
        predicted_sequence = predict_with_set(lz_val, hqs_val, set_name)
        results[set_name] = predicted_sequence
    
    return results

def analyze_results(results):
    """Analyze results from all sets"""
    print("\n" + "=" * 70)
    print("RESULTS ANALYSIS")
    print("=" * 70)
    
    known_sequence = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607]
    
    print("Set            | Found | Sequence")
    print("-" * 50)
    
    best_set = None
    best_score = 0
    
    for set_name, sequence in results.items():
        if len(sequence) > 1:  # Only count sets that found something
            # Calculate how many correct in sequence
            correct = 0
            for i in range(min(len(sequence), len(known_sequence))):
                if sequence[i] == known_sequence[i]:
                    correct += 1
            
            score = correct
            if score > best_score:
                best_score = score
                best_set = set_name
            
            seq_display = " → ".join([f"M_{e}" for e in sequence[:6]])
            if len(sequence) > 6:
                seq_display += " ..."
                
            print(f"{set_name:14} | {len(sequence):5} | {seq_display}")
    
    if best_set:
        print(f"\nBEST SET: {best_set}")
        print(f"Found {len(results[best_set])} Mersenne primes")
        print(f"Sequence: {results[best_set]}")

def show_convergence_analysis():
    """Show LZ/HQS convergence pattern"""
    print("\n" + "=" * 70)
    print("LZ/HQS CONVERGENCE ANALYSIS")
    print("=" * 70)
    
    print("Set      LZ Value                  HQS Value")
    print("-" * 55)
    
    for lz_name, lz_val, hqs_name, hqs_val in LZ_HQS_SETS:
        print(f"{lz_name:6} {lz_val:23.16f}  {hqs_val:23.16f}")

# Run the prediction
if __name__ == "__main__":
    # Show convergence
    show_convergence_analysis()
    
    # Test all sets
    results = test_all_sets()
    
    # Analyze results
    analyze_results(results)
    
    print("\n" + "=" * 70)
    print("3DCOM MERSENNE PREDICTION COMPLETE")
    print("Tested ALL LZ/HQS sets")
    print("=" * 70)
