# 🚀 QUICK START - VLSM Network in Packet Tracer

## 1. Create Topology (2 minutes)

**Add devices:**
- 4 x Router 2911
- 4 x PC

**Connect devices:**
```
PC1 ---- R1 ===== R2 ---- PC2
          ||       ||
          ||       ||
PC4 ---- R4 ===== R3 ---- PC3
```

**Cables needed:**
- PC to Router: Straight-through ethernet cables (Fa0/0)
- Router to Router: Serial DCE/DTE cables (Se0/0/x)

## 2. Configure Routers (5 minutes)

**Copy & Paste these configurations:**

### R1
```cisco
enable
configure terminal
hostname R1
interface FastEthernet0/0
ip address 192.168.1.1 255.255.255.128
no shutdown
exit
interface Serial0/0/0
ip address 192.168.1.173 255.255.255.252
clock rate 64000
no shutdown
exit
ip route 192.168.1.128 255.255.255.224 192.168.1.174
ip route 192.168.1.160 255.255.255.248 192.168.1.174
ip route 192.168.1.168 255.255.255.252 192.168.1.174
ip route 192.168.1.176 255.255.255.252 192.168.1.174
ip route 192.168.1.180 255.255.255.252 192.168.1.174
exit
copy running-config startup-config
```

### R2
```cisco
enable
configure terminal
hostname R2
interface FastEthernet0/0
ip address 192.168.1.129 255.255.255.224
no shutdown
exit
interface Serial0/0/0
ip address 192.168.1.174 255.255.255.252
no shutdown
exit
interface Serial0/0/1
ip address 192.168.1.177 255.255.255.252
clock rate 64000
no shutdown
exit
ip route 192.168.1.0 255.255.255.128 192.168.1.173
ip route 192.168.1.160 255.255.255.248 192.168.1.178
ip route 192.168.1.168 255.255.255.252 192.168.1.178
ip route 192.168.1.180 255.255.255.252 192.168.1.178
exit
copy running-config startup-config
```

### R3
```cisco
enable
configure terminal
hostname R3
interface FastEthernet0/0
ip address 192.168.1.161 255.255.255.248
no shutdown
exit
interface Serial0/0/0
ip address 192.168.1.178 255.255.255.252
no shutdown
exit
interface Serial0/0/1
ip address 192.168.1.181 255.255.255.252
clock rate 64000
no shutdown
exit
ip route 192.168.1.0 255.255.255.128 192.168.1.177
ip route 192.168.1.128 255.255.255.224 192.168.1.177
ip route 192.168.1.172 255.255.255.252 192.168.1.177
ip route 192.168.1.168 255.255.255.252 192.168.1.182
exit
copy running-config startup-config
```

### R4
```cisco
enable
configure terminal
hostname R4
interface FastEthernet0/0
ip address 192.168.1.169 255.255.255.252
no shutdown
exit
interface Serial0/0/0
ip address 192.168.1.182 255.255.255.252
no shutdown
exit
ip route 192.168.1.0 255.255.255.128 192.168.1.181
ip route 192.168.1.128 255.255.255.224 192.168.1.181
ip route 192.168.1.160 255.255.255.248 192.168.1.181
ip route 192.168.1.172 255.255.255.252 192.168.1.181
ip route 192.168.1.176 255.255.255.252 192.168.1.181
exit
copy running-config startup-config
```

## 3. Configure PCs (2 minutes)

Click each PC → Desktop → IP Configuration → Static:

| PC | IP Address | Subnet Mask | Default Gateway |
|----|------------|-------------|-----------------|
| PC1 | 192.168.1.2 | 255.255.255.128 | 192.168.1.1 |
| PC2 | 192.168.1.130 | 255.255.255.224 | 192.168.1.129 |
| PC3 | 192.168.1.162 | 255.255.255.248 | 192.168.1.161 |
| PC4 | 192.168.1.170 | 255.255.255.252 | 192.168.1.169 |

## 4. Test Network (1 minute)

From any PC, open Command Prompt and test:

```
ping 192.168.1.2    # PC1
ping 192.168.1.130  # PC2  
ping 192.168.1.162  # PC3
ping 192.168.1.170  # PC4
```

**All pings should succeed! 🎉**

## 🔧 Troubleshooting

If something doesn't work:

1. **Check router interfaces:** `show ip interface brief`
2. **Check routing table:** `show ip route`
3. **Verify PC settings:** Click PC → Desktop → IP Configuration

---

**Total setup time: ~10 minutes**

For detailed explanations, see the other documentation files in this repository!