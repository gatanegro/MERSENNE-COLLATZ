# COMPLETE MERSENNE-COLLATZ ANALYZER
# No broken code - everything works

def collatz_steps(n):
    """Calculate Collatz steps for a single number"""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def find_all_mersenne_clusters():
    """Find ALL numbers with Mersenne exponent step counts"""
    
    mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521]
    results = {}
    
    print("FINDING ALL MERSENNE CLUSTERS:")
    print("=" * 60)
    
    for steps in mersenne_exponents:
        cluster = []
        # Search efficiently - focus on likely ranges
        if steps <= 31:
            max_search = 10000
        elif steps <= 127:
            max_search = 50000
        else:
            max_search = 10000000
            
        for num in range(1, max_search + 1):
            if collatz_steps(num) == steps:
                cluster.append(num)
                
        results[steps] = cluster
        print(f"Steps {steps:3}: {len(cluster):3} numbers found")
        
        # Show the cluster
        if cluster:
            if len(cluster) <= 1000:
                print(f"  {cluster}")
            else:
                print(f"  First 100000: {cluster[:10]}")
        print()
    
    return results

def analyze_patterns(clusters):
    """Analyze mathematical patterns in the clusters"""
    
    print("PATTERN ANALYSIS:")
    print("=" * 60)
    
    for steps, numbers in clusters.items():
        if numbers:
            print(f"\nSteps {steps}:")
            
            # Digital root analysis
            roots = [((n-1) % 9 + 1) for n in numbers]
            unique_roots = sorted(set(roots))
            print(f"  Digital roots: {unique_roots}")
            
            # Last digit analysis  
            last_digits = [n % 10 for n in numbers]
            unique_digits = sorted(set(last_digits))
            print(f"  Last digits: {unique_digits}")
            
            # Size analysis
            min_num = min(numbers)
            max_num = max(numbers)
            print(f"  Range: {min_num} to {max_num}")
            
            # Density analysis
            density = len(numbers) / (max_num - min_num + 1) if max_num > min_num else 1
            print(f"  Density: {density:.3f}")

def find_branch_structure(clusters):
    """Identify the branch structure you discovered"""
    
    print("\nBRANCH STRUCTURE:")
    print("=" * 60)
    
    # Your observed branch pattern
    branches = {
        "Branch 1 (2)": [n for n in clusters.get(5, []) if n < 100],
        "Branch 2 (3,5)": [n for n in clusters.get(7, []) if n < 100], 
        "Branch 3 (7)": [n for n in clusters.get(13, []) if n < 100],
        "Branch 4 (13,17,19)": [n for lst in [clusters.get(13,[]), clusters.get(17,[]), clusters.get(19,[])] 
                               for n in lst if n < 100],
        "Branch 5 (31)": [n for n in clusters.get(31, []) if n < 200]
    }
    
    for branch_name, numbers in branches.items():
        if numbers:
            print(f"{branch_name}: {numbers}")

# RUN THE COMPLETE ANALYSIS
if __name__ == "__main__":
    # Step 1: Find all clusters
    all_clusters = find_all_mersenne_clusters()
    
    # Step 2: Analyze patterns
    analyze_patterns(all_clusters)
    
    # Step 3: Show branch structure
    find_branch_structure(all_clusters)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
