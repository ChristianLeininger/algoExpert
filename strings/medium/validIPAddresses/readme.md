# Valid IP Addresses

## 1. Problem Statement

The problem is to write a function that determines where to add periods to a decimal string so that the resulting string is a valid IP address. A valid IP address must:

-   Consist of 4 parts separated by periods.
-   Each part must be a number from 0 to 255.
-   The parts must not start with a '0' unless the part is exactly '0'.

### Example <br /> 
 For the input string '19216811', <br />
  the program would output all valid IP addresses that can be generated from these digits by inserting periods at different positions . <br /> 
 Here are a couple of possible outputs: - '192.168.1.1' - '192.16.81.1' - '19.216.8.11' <br />
 There may be other valid IP addresses that can be generated from the input string, and the program should output all of them.
