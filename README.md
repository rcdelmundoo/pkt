# VLSM Static Routing Network - Packet Tracer Lab

This repository contains all the files needed to build a complete VLSM (Variable Length Subnet Masking) static routing network in Cisco Packet Tracer.

## 📋 Project Overview

**Network Requirements:**
- Base Network: 192.168.1.0/24
- Subnet Requirements: 64, 18, 4, 2, 2, 2 hosts
- 4 Routers connected in a line topology
- Static routing implementation
- Full connectivity between all devices

## 📁 Files Included

| File | Description |
|------|-------------|
| `packet_tracer_setup.md` | Complete setup guide and topology overview |
| `vlsm_guide.md` | VLSM theory and calculation examples |
| `vlsm_calculator.py` | Python script for VLSM calculations |
| `R1_config.txt` | Router 1 complete configuration |
| `R2_config.txt` | Router 2 complete configuration |
| `R3_config.txt` | Router 3 complete configuration |
| `R4_config.txt` | Router 4 complete configuration |
| `PC_configs.txt` | PC IP configuration settings |
| `verify_network.txt` | Network verification and testing commands |

## 🚀 Quick Start

### 1. Open Packet Tracer and Create Topology
```
PC1 ---- R1 ===== R2 ---- PC2
          ||       ||
          ||       ||
PC4 ---- R4 ===== R3 ---- PC3
```

### 2. Add Devices
- 4 x Router 2911 (or 2901)
- 4 x PC
- Connect with appropriate cables

### 3. Configure Routers
Copy and paste the configuration from each `Rx_config.txt` file into the corresponding router's CLI.

### 4. Configure PCs
Use the IP settings from `PC_configs.txt` to configure each PC.

### 5. Test Network
Follow the verification steps in `verify_network.txt` to ensure everything works.

## 🔧 VLSM Subnet Breakdown

| Subnet | Hosts | Network | Mask | Router | Usage |
|--------|-------|---------|------|---------|-------|
| LAN1 | 64 | 192.168.1.0/25 | 255.255.255.128 | R1 | Main LAN |
| LAN2 | 18 | 192.168.1.128/27 | 255.255.255.224 | R2 | Department LAN |
| LAN3 | 4 | 192.168.1.160/29 | 255.255.255.248 | R3 | Small office |
| LAN4 | 2 | 192.168.1.168/30 | 255.255.255.252 | R4 | Point-to-point |
| WAN1 | 2 | 192.168.1.172/30 | 255.255.255.252 | R1-R2 | Router link |
| WAN2 | 2 | 192.168.1.176/30 | 255.255.255.252 | R2-R3 | Router link |
| WAN3 | 2 | 192.168.1.180/30 | 255.255.255.252 | R3-R4 | Router link |

## 🖥️ Device IP Addresses

### Router Interfaces
- **R1**: Fa0/0 (192.168.1.1), Se0/0/0 (192.168.1.173)
- **R2**: Fa0/0 (192.168.1.129), Se0/0/0 (192.168.1.174), Se0/0/1 (192.168.1.177)
- **R3**: Fa0/0 (192.168.1.161), Se0/0/0 (192.168.1.178), Se0/0/1 (192.168.1.181)
- **R4**: Fa0/0 (192.168.1.169), Se0/0/0 (192.168.1.182)

### PC IP Addresses
- **PC1**: 192.168.1.2/25 (Gateway: 192.168.1.1)
- **PC2**: 192.168.1.130/27 (Gateway: 192.168.1.129)
- **PC3**: 192.168.1.162/29 (Gateway: 192.168.1.161)
- **PC4**: 192.168.1.170/30 (Gateway: 192.168.1.169)

## ✅ Expected Test Results

When properly configured, all devices should be able to communicate:

**Successful Pings:**
- PC1 → PC2, PC3, PC4 ✓
- PC2 → PC1, PC3, PC4 ✓
- PC3 → PC1, PC2, PC4 ✓
- PC4 → PC1, PC2, PC3 ✓

**Traceroute Example (PC1 to PC4):**
```
PC1 → R1 → R2 → R3 → R4 → PC4
```

## 🔧 Tools Included

### VLSM Calculator (`vlsm_calculator.py`)
A Python script that automatically calculates VLSM subnets:
```bash
python3 vlsm_calculator.py
```
- Interactive mode for custom networks
- Automatic subnet ordering (largest first)
- Detailed subnet information tables

## 📚 Learning Objectives

This lab demonstrates:
- ✅ VLSM subnet calculation and implementation
- ✅ Static routing configuration
- ✅ Router interface configuration
- ✅ Network connectivity testing
- ✅ Troubleshooting network issues

## 🔍 Troubleshooting

Common issues and solutions:

| Issue | Solution |
|-------|----------|
| Serial interface down | Set clock rate on DCE interface |
| No connectivity | Check static routes and interface IPs |
| Partial connectivity | Verify all routes are configured |
| PC can't ping gateway | Check PC IP configuration |

## 📖 Additional Resources

- **VLSM Theory**: See `vlsm_guide.md` for detailed explanations
- **Packet Tracer Setup**: See `packet_tracer_setup.md` for step-by-step instructions
- **Verification**: See `verify_network.txt` for testing procedures

## 🎯 Lab Extensions

Try these additional challenges:
1. Add more PCs to each LAN segment
2. Implement OSPF instead of static routing
3. Add VLANs to segment the LANs further
4. Configure access control lists (ACLs)
5. Add redundant links and implement load balancing

---

**📝 Note:** While I cannot create a binary PKT file directly, these configuration files make it very easy to build the network manually in Packet Tracer. Simply copy and paste the configurations, and you'll have a fully functional VLSM static routing network!