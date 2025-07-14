# VLSM (Variable Length Subnet Masking) Guide

## What is VLSM?

Variable Length Subnet Masking (VLSM) is a technique that allows you to subnet a network using different subnet mask lengths for different subnets. This maximizes the efficient use of IP addresses by allocating exactly the number of host addresses needed for each subnet.

## Key Concepts

### 1. Powers of 2
- 2^1 = 2
- 2^2 = 4  
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256

### 2. Subnet Mask Notation
- /24 = 255.255.255.0 (8 host bits = 254 usable hosts)
- /25 = 255.255.255.128 (7 host bits = 126 usable hosts)
- /26 = 255.255.255.192 (6 host bits = 62 usable hosts)
- /27 = 255.255.255.224 (5 host bits = 30 usable hosts)
- /28 = 255.255.255.240 (4 host bits = 14 usable hosts)
- /29 = 255.255.255.248 (3 host bits = 6 usable hosts)
- /30 = 255.255.255.252 (2 host bits = 2 usable hosts)

## VLSM Process

### Step 1: List Requirements
Order your subnets from largest to smallest number of hosts needed.

### Step 2: Calculate Subnet Size
For each subnet, find the smallest power of 2 that accommodates the required hosts + 2 (network and broadcast addresses).

### Step 3: Assign Subnets
Start with the largest subnet and assign IP ranges sequentially.

## Example Problem

**Given:** Network 192.168.1.0/24
**Requirements:**
- Subnet A: 50 hosts
- Subnet B: 25 hosts  
- Subnet C: 10 hosts
- Subnet D: 5 hosts

### Solution:

#### Step 1: Order by size (largest first)
1. Subnet A: 50 hosts
2. Subnet B: 25 hosts
3. Subnet C: 10 hosts
4. Subnet D: 5 hosts

#### Step 2: Calculate required subnet sizes
- Subnet A: 50 + 2 = 52 hosts needed → 2^6 = 64 → /26 (6 host bits)
- Subnet B: 25 + 2 = 27 hosts needed → 2^5 = 32 → /27 (5 host bits)
- Subnet C: 10 + 2 = 12 hosts needed → 2^4 = 16 → /28 (4 host bits)
- Subnet D: 5 + 2 = 7 hosts needed → 2^3 = 8 → /29 (3 host bits)

#### Step 3: Assign IP ranges
Starting with 192.168.1.0/24:

**Subnet A (/26 - 64 addresses):**
- Network: 192.168.1.0/26
- Range: 192.168.1.1 - 192.168.1.62
- Broadcast: 192.168.1.63
- Next available: 192.168.1.64

**Subnet B (/27 - 32 addresses):**
- Network: 192.168.1.64/27
- Range: 192.168.1.65 - 192.168.1.94
- Broadcast: 192.168.1.95
- Next available: 192.168.1.96

**Subnet C (/28 - 16 addresses):**
- Network: 192.168.1.96/28
- Range: 192.168.1.97 - 192.168.1.110
- Broadcast: 192.168.1.111
- Next available: 192.168.1.112

**Subnet D (/29 - 8 addresses):**
- Network: 192.168.1.112/29
- Range: 192.168.1.113 - 192.168.1.118
- Broadcast: 192.168.1.119
- Next available: 192.168.1.120

## Quick Reference Table

| Hosts Needed | Power of 2 | Subnet Mask | CIDR | Usable Hosts |
|--------------|------------|-------------|------|--------------|
| 1-2          | 2^2 = 4    | /30         | 255.255.255.252 | 2 |
| 3-6          | 2^3 = 8    | /29         | 255.255.255.248 | 6 |
| 7-14         | 2^4 = 16   | /28         | 255.255.255.240 | 14 |
| 15-30        | 2^5 = 32   | /27         | 255.255.255.224 | 30 |
| 31-62        | 2^6 = 64   | /26         | 255.255.255.192 | 62 |
| 63-126       | 2^7 = 128  | /25         | 255.255.255.128 | 126 |
| 127-254      | 2^8 = 256  | /24         | 255.255.255.0   | 254 |

## Common Mistakes to Avoid

1. **Forgetting the +2 rule**: Always add 2 to the host requirement (for network and broadcast addresses)
2. **Not ordering by size**: Always start with the largest subnet first
3. **Overlapping subnets**: Make sure each subnet starts where the previous one ends
4. **Wrong power of 2**: Choose the next power of 2 that's greater than or equal to your requirement

## Tips

- Always work from largest to smallest subnet
- Double-check your math with powers of 2
- Verify that subnets don't overlap
- Leave room for future growth when possible
- Use online calculators to verify your work