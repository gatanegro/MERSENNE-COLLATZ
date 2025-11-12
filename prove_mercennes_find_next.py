def predict_next_mersenne():
    """Use the branch pattern to predict next Mersenne exponents"""
    
    # Known pattern: 2 → 3,5 → 7 → 13,17,19 → 31 → 61 → 89 → 107 → 127 → ?
    branch_sequence = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]
    
    # Analyze gaps to predict next
    gaps = [branch_sequence[i+1] - branch_sequence[i] for i in range(len(branch_sequence)-1)]
    print(f"Branch gaps: {gaps}")
    
    # Predict next in sequence
    next_predicted = 127 + gaps[-1]  # Simple extrapolation
    print(f"Predicted next Mersenne exponent: ~{next_predicted}")
    
    return next_predicted

predicted = predict_next_mersenne()
