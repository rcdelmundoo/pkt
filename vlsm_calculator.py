#!/usr/bin/env python3
"""
VLSM (Variable Length Subnet Masking) Calculator
This script helps calculate VLSM subnets efficiently.
"""

import ipaddress
import math
from typing import List, Tuple, Dict

class VLSMCalculator:
    def __init__(self, base_network: str):
        """
        Initialize with a base network (e.g., '192.168.1.0/24')
        """
        self.base_network = ipaddress.IPv4Network(base_network, strict=False)
        self.current_address = self.base_network.network_address
        
    def calculate_subnet_size(self, hosts_needed: int) -> Tuple[int, int]:
        """
        Calculate the required subnet size for given number of hosts.
        Returns (subnet_bits, total_addresses)
        """
        # Add 2 for network and broadcast addresses
        total_needed = hosts_needed + 2
        
        # Find the next power of 2 that fits
        subnet_bits = math.ceil(math.log2(total_needed))
        total_addresses = 2 ** subnet_bits
        
        return subnet_bits, total_addresses
    
    def create_subnet(self, hosts_needed: int, name: str = "") -> Dict:
        """
        Create a subnet with the specified number of hosts.
        Returns subnet information.
        """
        subnet_bits, total_addresses = self.calculate_subnet_size(hosts_needed)
        
        # Calculate prefix length
        host_bits = subnet_bits
        prefix_length = 32 - host_bits
        
        # Create the subnet
        try:
            subnet = ipaddress.IPv4Network(f"{self.current_address}/{prefix_length}", strict=False)
            
            # Check if subnet fits in base network
            if not self.base_network.supernet_of(subnet):
                raise ValueError(f"Subnet doesn't fit in base network {self.base_network}")
            
            subnet_info = {
                'name': name,
                'hosts_needed': hosts_needed,
                'network': str(subnet.network_address),
                'prefix_length': prefix_length,
                'subnet_mask': str(subnet.netmask),
                'first_host': str(subnet.network_address + 1),
                'last_host': str(subnet.broadcast_address - 1),
                'broadcast': str(subnet.broadcast_address),
                'total_addresses': total_addresses,
                'usable_hosts': total_addresses - 2,
                'network_cidr': str(subnet)
            }
            
            # Update current address for next subnet
            self.current_address = subnet.broadcast_address + 1
            
            return subnet_info
            
        except Exception as e:
            raise ValueError(f"Error creating subnet: {e}")
    
    def calculate_vlsm(self, requirements: List[Tuple[str, int]]) -> List[Dict]:
        """
        Calculate VLSM for multiple subnet requirements.
        requirements: List of (subnet_name, hosts_needed) tuples
        """
        # Sort by hosts needed (largest first)
        sorted_requirements = sorted(requirements, key=lambda x: x[1], reverse=True)
        
        subnets = []
        
        for name, hosts_needed in sorted_requirements:
            try:
                subnet_info = self.create_subnet(hosts_needed, name)
                subnets.append(subnet_info)
            except ValueError as e:
                print(f"Error creating subnet '{name}': {e}")
                break
                
        return subnets
    
    def print_subnet_table(self, subnets: List[Dict]):
        """
        Print a formatted table of subnet information.
        """
        print("\n" + "="*100)
        print("VLSM SUBNET ALLOCATION TABLE")
        print("="*100)
        print(f"{'Subnet':<15} {'Hosts':<8} {'Network':<18} {'CIDR':<6} {'First Host':<15} {'Last Host':<15} {'Broadcast':<15}")
        print("-"*100)
        
        for subnet in subnets:
            print(f"{subnet['name']:<15} "
                  f"{subnet['hosts_needed']:<8} "
                  f"{subnet['network']:<18} "
                  f"/{subnet['prefix_length']:<5} "
                  f"{subnet['first_host']:<15} "
                  f"{subnet['last_host']:<15} "
                  f"{subnet['broadcast']:<15}")
        
        print("-"*100)
        print(f"Next available address: {self.current_address}")
        print("="*100)

def main():
    """
    Example usage and interactive mode
    """
    print("VLSM Calculator")
    print("===============")
    
    # Example calculation
    print("\nExample: Subnetting 192.168.1.0/24")
    
    calc = VLSMCalculator("192.168.1.0/24")
    
    requirements = [
        ("Sales", 50),
        ("Engineering", 25),
        ("Marketing", 10),
        ("HR", 5)
    ]
    
    subnets = calc.calculate_vlsm(requirements)
    calc.print_subnet_table(subnets)
    
    # Interactive mode
    print("\n" + "="*50)
    print("INTERACTIVE MODE")
    print("="*50)
    
    try:
        base_net = input("\nEnter base network (e.g., 192.168.1.0/24): ").strip()
        if not base_net:
            base_net = "192.168.1.0/24"
            
        calc = VLSMCalculator(base_net)
        
        requirements = []
        print("\nEnter subnet requirements (press Enter with empty name to finish):")
        
        while True:
            name = input("Subnet name: ").strip()
            if not name:
                break
                
            try:
                hosts = int(input(f"Number of hosts needed for {name}: "))
                requirements.append((name, hosts))
            except ValueError:
                print("Please enter a valid number of hosts.")
                continue
        
        if requirements:
            print(f"\nCalculating VLSM for {base_net}...")
            subnets = calc.calculate_vlsm(requirements)
            calc.print_subnet_table(subnets)
        else:
            print("No requirements entered.")
            
    except KeyboardInterrupt:
        print("\n\nExiting...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()