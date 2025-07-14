# Packet Tracer VLSM Static Routing Network Setup

## Quick Start Guide

### Step 1: Create Topology in Packet Tracer

1. **Add Devices:**
   - 4 x Router 2911 (or 2901)
   - 4 x PC
   - Optional: 4 x Switch 2960 (if you want switches between routers and PCs)

2. **Device Placement:**
   ```
   PC1 ---- R1 ===== R2 ---- PC2
             ||       ||
             ||       ||
   PC4 ---- R4 ===== R3 ---- PC3
   ```

3. **Physical Connections:**
   - R1 Fa0/0 to PC1 (or Switch1)
   - R1 Se0/0/0 to R2 Se0/0/0 (Serial DCE/DTE)
   - R2 Fa0/0 to PC2 (or Switch2)
   - R2 Se0/0/1 to R3 Se0/0/0 (Serial DCE/DTE)
   - R3 Fa0/0 to PC3 (or Switch3)
   - R3 Se0/0/1 to R4 Se0/0/0 (Serial DCE/DTE)
   - R4 Fa0/0 to PC4 (or Switch4)

### Step 2: Configure Clock Rates (Important!)

On DCE interfaces, set clock rate. Check which end is DCE with `show controllers serial x/x/x`

Typically:
- R1 Se0/0/0 (DCE) → R2 Se0/0/0 (DTE)
- R2 Se0/0/1 (DCE) → R3 Se0/0/0 (DTE)  
- R3 Se0/0/1 (DCE) → R4 Se0/0/0 (DTE)

```cisco
interface serial0/0/0
clock rate 64000
```

### Step 3: Apply Router Configurations

Copy the configuration from each router file (R1_config.txt, R2_config.txt, etc.) and paste into the respective router's CLI.

### Step 4: Configure PCs

Set the IP configurations as specified in the PC_configs.txt file.

### Step 5: Test and Verify

Use the verification commands in verify_network.txt to test connectivity.

## Network Details

### VLSM Subnet Allocation
| Subnet | Purpose | Network | Mask | Usable IPs | Router |
|--------|---------|---------|------|------------|---------|
| LAN1 | R1 LAN | 192.168.1.0/25 | 255.255.255.128 | .1-.126 | R1 |
| LAN2 | R2 LAN | 192.168.1.128/27 | 255.255.255.224 | .129-.158 | R2 |
| LAN3 | R3 LAN | 192.168.1.160/29 | 255.255.255.248 | .161-.166 | R3 |
| LAN4 | R4 LAN | 192.168.1.168/30 | 255.255.255.252 | .169-.170 | R4 |
| WAN1 | R1-R2 | 192.168.1.172/30 | 255.255.255.252 | .173-.174 | Link |
| WAN2 | R2-R3 | 192.168.1.176/30 | 255.255.255.252 | .177-.178 | Link |
| WAN3 | R3-R4 | 192.168.1.180/30 | 255.255.255.252 | .181-.182 | Link |

### Interface Assignments
- **R1**: Fa0/0 (.1), Se0/0/0 (.173)
- **R2**: Fa0/0 (.129), Se0/0/0 (.174), Se0/0/1 (.177)
- **R3**: Fa0/0 (.161), Se0/0/0 (.178), Se0/0/1 (.181)
- **R4**: Fa0/0 (.169), Se0/0/0 (.182)

## Troubleshooting Tips

1. **No Connectivity:**
   - Check cable connections
   - Verify interface status: `show ip interface brief`
   - Check routing table: `show ip route`

2. **Serial Links Down:**
   - Ensure clock rate is set on DCE interface
   - Check if both ends are configured: `no shutdown`

3. **Partial Connectivity:**
   - Verify static routes are correct
   - Check next-hop addresses match interface IPs

4. **PC Cannot Ping:**
   - Verify PC IP configuration
   - Check default gateway setting
   - Test router interface: ping router's Fa0/0 from PC

## Expected Ping Results

All devices should be able to ping all other devices:
- PC1 (192.168.1.2) ↔ PC2 (192.168.1.130) ↔ PC3 (192.168.1.162) ↔ PC4 (192.168.1.170)
- Any PC should reach any router interface