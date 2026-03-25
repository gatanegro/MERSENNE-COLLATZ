#!/usr/bin/env python3
"""
Shell-Leg Lattice Builder - Upward Growth
Builds lattice from seeds 2 and 3 upward using binary patterns.

The tree grows from small numbers (base) upward to Mersenne exponents.
When multiple exponents share a prefix, that creates a branch point.

Usage:
    python lattice_upward.py --export
    python lattice_upward.py --verbose
"""

import json
from dataclasses import dataclass, field
from typing import Dict, Set, List, Tuple, Optional
from collections import defaultdict
import argparse


# ============================================================================
# KNOWN MERSENNE EXPONENTS WITH THEIR BINARY PATTERNS 
# ============================================================================

# Patterns from BASE 2 (seed=2)
PATTERNS_BASE_2 = {
    5: "1",
    17: "001",
    19: "011",
    89: "11001",
    521: "00001001",
    607: "01011111",
    1279: "011111111",
    2203: "0010011011",
    2281: "0011101001",
    4253: "00010011101",
    4423: "00101000111",
    9689: "010111011001",
    9941: "011011010101",
    11213: "101111001101",
    19937: "0110111100001",
    21701: "1010011000101",
    23209: "1101010101001",
    44497: "10110111010001",
    86243: "101000011100011",
    132049: "0000001111010001",
    756839: "111000110001100111",
    3021377: "11100001101001000001",
    1257787: "0110011000100111011",
    1398269: "1010101010111111101",
    2976221: "11010110100111011101",
    20996011: "10000000101111110101011",
    24036583: "11011101100010011100111",
    37156667: "001101101111011100111011",
    42643801: "100010101011000101011001",
    43112609: "100100011101100010100001",
    74207281: "0011011000101000000110001",
    77232917: "0100110100111101100010101",
    82589933: "0111011000011100011101101",
    136279841: "00000111110111011100100001",
}

# Patterns from BASE 3 (seed=3)
PATTERNS_BASE_3 = {
    7: "1",
    13: "01",
    31: "111",
    61: "1101",
    107: "01011",
    127: "11111",
    3217: "0010010001",
    110503: "010111110100111",
    216091: "0100110000011011",
    859433: "010001110100101001",
    6972593: "010100110010010110001",
    13466917: "0011010111110100100101",
    25964951: "00011000011000110010111",
    30402457: "10011111110011110011001",
    32582657: "11100010010110000000001",
    57885161: "011100110100000111101001",
}

# Combine all patterns
ALL_PATTERNS = {
    **{exp: (2, pattern) for exp, pattern in PATTERNS_BASE_2.items()},
    **{exp: (3, pattern) for exp, pattern in PATTERNS_BASE_3.items()}
}


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class Vertex:
    """A vertex in the lattice"""
    value: int
    children: List['Vertex'] = field(default_factory=list)
    parents: List['Vertex'] = field(default_factory=list)
    exponents: Set[int] = field(default_factory=set)  # Mersenne exponents that pass through
    
    def __hash__(self):
        return hash(self.value)
    
    def __repr__(self):
        return f"Vertex({self.value}, children={len(self.children)}, exponents={len(self.exponents)})"


@dataclass
class Branch:
    """A branch point where multiple exponents diverge"""
    vertex: int
    depth: int
    children: List[int]
    exponents: List[int]


class UpwardLattice:
    """
    Builds lattice upward from seeds 2 and 3 using binary patterns.
    
    The tree grows from small numbers (base) upward to Mersenne exponents.
    Each pattern is applied from the seed upward to reach its exponent.
    """
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.seeds = [2, 3]
        
        # All vertices in the lattice
        self.vertices: Dict[int, Vertex] = {}
        
        # Create seed vertices
        for seed in self.seeds:
            self.vertices[seed] = Vertex(value=seed)
        
        # Track all paths
        self.paths: Dict[int, Tuple[int, str]] = {}
        
        # Track branch points
        self.branches: Dict[int, Branch] = {}
        
        # Statistics
        self.stats = {
            'total_vertices': len(self.vertices),
            'total_paths': 0,
            'branch_points': 0,
            'max_depth': 0
        }
    
    def apply_pattern(self, seed: int, pattern: str, exponent: int) -> List[int]:
        """
        Apply a pattern upward from seed to reach exponent.
        Returns the sequence of vertices along the path.
        """
        vertices = [seed]
        current = seed
        
        for bit in pattern:
            if bit == '0':
                current = current * 2  # shell
            else:
                current = current * 2 + 1  # leg
            vertices.append(current)
        
        # Verify we reached the target exponent
        if vertices[-1] != exponent:
            raise ValueError(f"Pattern {pattern} from seed {seed} gives {vertices[-1]}, expected {exponent}")
        
        return vertices
    
    def add_path(self, exponent: int, seed: int, pattern: str):
        """Add a path to the lattice"""
        vertices = self.apply_pattern(seed, pattern, exponent)
        
        # Store the path
        self.paths[exponent] = (seed, pattern)
        
        # Add all vertices to the lattice
        for i, val in enumerate(vertices):
            if val not in self.vertices:
                self.vertices[val] = Vertex(value=val)
            
            # Mark that this Mersenne exponent passes through this vertex
            self.vertices[val].exponents.add(exponent)
            
            # Connect to next vertex
            if i < len(vertices) - 1:
                next_val = vertices[i + 1]
                if next_val not in self.vertices:
                    self.vertices[next_val] = Vertex(value=next_val)
                
                # Add child relationship
                if self.vertices[next_val] not in self.vertices[val].children:
                    self.vertices[val].children.append(self.vertices[next_val])
                
                # Add parent relationship
                if self.vertices[val] not in self.vertices[next_val].parents:
                    self.vertices[next_val].parents.append(self.vertices[val])
        
        # Update statistics
        self.stats['total_paths'] += 1
        self.stats['total_vertices'] = len(self.vertices)
        self.stats['max_depth'] = max(self.stats['max_depth'], len(vertices) - 1)
        
        if self.verbose:
            print(f"  Added path: {exponent} from seed {seed} | pattern {pattern} | depth {len(vertices)-1}")
    
    def build_from_patterns(self):
        """Build the complete lattice from all patterns"""
        print(f"\n{'='*60}")
        print(f"BUILDING LATTICE UPWARD FROM SEEDS {self.seeds}")
        print(f"{'='*60}\n")
        
        for exponent, (seed, pattern) in ALL_PATTERNS.items():
            self.add_path(exponent, seed, pattern)
        
        print(f"Built lattice with {self.stats['total_vertices']} vertices")
        print(f"  {self.stats['total_paths']} paths to Mersenne exponents")
    
    def find_branch_points(self):
        """Identify branch points where multiple exponents diverge"""
        self.branches.clear()
        
        # Sort vertices by value (ascending)
        sorted_vertices = sorted(self.vertices.values(), key=lambda v: v.value)
        
        for vertex in sorted_vertices:
            # A branch point has multiple children
            if len(vertex.children) >= 2:
                # Get all exponents that pass through this vertex
                exponents = list(vertex.exponents)
                
                # Get all children values
                children_vals = [c.value for c in vertex.children]
                
                # Calculate depth (distance from nearest seed)
                depth = self.get_depth(vertex)
                
                self.branches[vertex.value] = Branch(
                    vertex=vertex.value,
                    depth=depth,
                    children=children_vals,
                    exponents=exponents
                )
        
        self.stats['branch_points'] = len(self.branches)
        
        if self.verbose:
            print(f"\nFound {len(self.branches)} branch points")
    
    def get_depth(self, vertex: Vertex) -> int:
        """Calculate the depth of a vertex (distance from nearest seed)"""
        # BFS from seeds to find shortest path
        from collections import deque
        
        visited = set()
        queue = deque()
        
        for seed in self.seeds:
            if seed in self.vertices:
                queue.append((self.vertices[seed], 0))
                visited.add(seed)
        
        while queue:
            current, depth = queue.popleft()
            if current.value == vertex.value:
                return depth
            for child in current.children:
                if child.value not in visited:
                    visited.add(child.value)
                    queue.append((child, depth + 1))
        
        return -1
    
    def get_path_vertices(self, exponent: int) -> Optional[List[int]]:
        """Get the full vertex path for a given exponent"""
        if exponent not in self.paths:
            return None
        
        seed, pattern = self.paths[exponent]
        vertices = [seed]
        current = seed
        
        for bit in pattern:
            if bit == '0':
                current = current * 2
            else:
                current = current * 2 + 1
            vertices.append(current)
        
        return vertices
    
    def print_summary(self):
        """Print lattice summary"""
        print(f"\n{'─'*60}")
        print(f"LATTICE SUMMARY")
        print(f"{'─'*60}")
        print(f"Seeds:                {self.seeds}")
        print(f"Total vertices:       {self.stats['total_vertices']}")
        print(f"Total paths:          {self.stats['total_paths']}")
        print(f"Branch points:        {self.stats['branch_points']}")
        print(f"Max depth:            {self.stats['max_depth']}")
    
    def print_branches(self):
        """Print all branch points"""
        if not self.branches:
            print("\nNo branch points found")
            return
        
        print(f"\n{'─'*60}")
        print(f"BRANCH POINTS (where multiple exponents diverge)")
        print(f"{'─'*60}")
        
        sorted_branches = sorted(self.branches.values(), key=lambda b: b.vertex)
        
        for branch in sorted_branches:
            print(f"\nVertex: {branch.vertex} (depth {branch.depth})")
            print(f"  Children: {branch.children}")
            print(f"  Exponents passing through: {sorted(branch.exponents)}")
    
    def print_paths(self, max_paths: int = 20):
        """Print all paths"""
        print(f"\n{'─'*60}")
        print(f"PATHS TO MERSENNE EXPONENTS")
        print(f"{'─'*60}")
        
        sorted_paths = sorted(self.paths.items())
        
        for i, (exponent, (seed, pattern)) in enumerate(sorted_paths[:max_paths]):
            vertices = self.get_path_vertices(exponent)
            depth = len(vertices) - 1 if vertices else 0
            legs = pattern.count('1')
            shells = pattern.count('0')
            
            print(f"\nM{exponent}: {exponent}")
            print(f"  Seed: {seed}")
            print(f"  Pattern: {pattern}")
            print(f"  Legs: {legs}, Shells: {shells}, Depth: {depth}")
            print(f"  Path: {' → '.join(str(v) for v in vertices)}")
        
        if len(sorted_paths) > max_paths:
            print(f"\n... and {len(sorted_paths) - max_paths} more paths")
    
    def export_to_json(self, filename: str = 'lattice_upward.json'):
        """Export lattice to JSON"""
        export = {
            'seeds': self.seeds,
            'statistics': self.stats,
            'paths': {},
            'vertices': {},
            'branches': []
        }
        
        # Export paths
        for exponent, (seed, pattern) in self.paths.items():
            vertices = self.get_path_vertices(exponent)
            export['paths'][str(exponent)] = {
                'seed': seed,
                'pattern': pattern,
                'vertices': vertices,
                'legs': pattern.count('1'),
                'shells': pattern.count('0'),
                'depth': len(vertices) - 1
            }
        
        # Export vertices
        for value, vertex in self.vertices.items():
            export['vertices'][str(value)] = {
                'children': [c.value for c in vertex.children],
                'parents': [p.value for p in vertex.parents],
                'exponents': list(vertex.exponents)
            }
        
        # Export branches
        for branch in self.branches.values():
            export['branches'].append({
                'vertex': branch.vertex,
                'depth': branch.depth,
                'children': branch.children,
                'exponents': branch.exponents
            })
        
        with open(filename, 'w') as f:
            json.dump(export, f, indent=2)
        
        print(f"\nExported lattice to {filename}")
    
    def print_tree_structure(self, max_depth: int = 5):
        """Print a visual representation of the tree structure"""
        print(f"\n{'─'*60}")
        print(f"TREE STRUCTURE (up to depth {max_depth})")
        print(f"{'─'*60}")
        
        # BFS from seeds
        from collections import deque
        
        visited = set()
        queue = deque()
        
        for seed in self.seeds:
            if seed in self.vertices:
                queue.append((self.vertices[seed], 0, ""))
                visited.add(seed)
        
        while queue:
            vertex, depth, prefix = queue.popleft()
            
            if depth > max_depth:
                continue
            
            # Indicate if this is a branch point or has Mersenne exponents
            markers = []
            if vertex.value in self.branches:
                markers.append("🌿")
            if vertex.exponents:
                markers.append(f"★{list(vertex.exponents)[0] if len(vertex.exponents)==1 else len(vertex.exponents)}")
            
            marker_str = f" [{', '.join(markers)}]" if markers else ""
            
            print(f"{'  ' * depth}{prefix}{vertex.value}{marker_str}")
            
            for i, child in enumerate(vertex.children):
                is_last = (i == len(vertex.children) - 1)
                new_prefix = "└── " if is_last else "├── "
                queue.append((child, depth + 1, new_prefix))


def main():
    parser = argparse.ArgumentParser(
        description="Shell-Leg Lattice Builder - Upward growth from seeds"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print detailed output"
    )
    parser.add_argument(
        "--export", "-e",
        type=str,
        default="lattice_upward.json",
        help="Export to JSON file"
    )
    parser.add_argument(
        "--show-paths", "-p",
        action="store_true",
        help="Show all paths"
    )
    parser.add_argument(
        "--show-branches", "-b",
        action="store_true",
        help="Show branch points"
    )
    parser.add_argument(
        "--show-tree", "-t",
        action="store_true",
        help="Show tree structure"
    )
    parser.add_argument(
        "--max-depth", "-d",
        type=int,
        default=5,
        help="Max depth for tree display"
    )
    
    args = parser.parse_args()
    
    # Create and build lattice
    lattice = UpwardLattice(verbose=args.verbose)
    lattice.build_from_patterns()
    lattice.find_branch_points()
    
    # Print results
    lattice.print_summary()
    
    if args.show_branches:
        lattice.print_branches()
    
    if args.show_paths:
        lattice.print_paths()
    
    if args.show_tree:
        lattice.print_tree_structure(max_depth=args.max_depth)
    
    # Export
    lattice.export_to_json(args.export)
    
    return lattice


if __name__ == "__main__":
    lattice = main()
