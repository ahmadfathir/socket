# socket
A **socket** is a software endpoint that enables communication between two machines over a network. It serves as an interface for sending and receiving data, typically using **IP (Internet Protocol)** and a transport protocol like **TCP (Transmission Control Protocol)** or **UDP (User Datagram Protocol)**.

### **Key Components of a Socket:**
1. **IP Address** – Identifies the machine (e.g., `192.168.1.1` or `example.com`).
2. **Port Number** – Specifies the application/service (e.g., `80` for HTTP, `443` for HTTPS).
3. **Protocol** – Defines the communication rules (TCP or UDP).

---

## **TCP vs UDP Sockets**
| Feature          | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
|------------------|-------------------------------------|------------------------------|
| **Connection**   | Connection-oriented (requires handshake) | Connectionless (no handshake) |
| **Reliability**  | Reliable (retransmits lost packets) | Unreliable (no retransmission) |
| **Ordering**     | Guarantees in-order delivery | No ordering guarantees |
| **Speed**        | Slower (due to overhead) | Faster (low overhead) |
| **Use Cases**    | Web browsing (HTTP/HTTPS), Email (SMTP), File Transfer (FTP) | Video streaming (VoIP, YouTube), Online gaming, DNS queries |

---

### **TCP Socket Example (Reliable, Ordered)**
- Used when data integrity is critical.
- Establishes a connection with `SYN`, `SYN-ACK`, `ACK` (3-way handshake).
- Ensures packets arrive in order.
- Example: Loading a webpage (HTTP).

### **UDP Socket Example (Fast, Connectionless)**
- Used when speed matters more than reliability.
- No handshake; just sends data.
- Packets may arrive out of order or get lost.
- Example: Live video streaming (where occasional packet loss is acceptable).

---

### **Summary**
- **TCP Sockets** → Reliable, ordered, slower (best for critical data).
- **UDP Sockets** → Fast, lightweight, unreliable (best for real-time applications).

---
### license
This socket is made for campus assignment needs.
