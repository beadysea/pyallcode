#!/usr/bin/env python3
"""
Example script demonstrating cross-platform COM port discovery
and basic usage of the refactored SOLID API (fa_robot.Robot)
"""

from ..pyallcode import Robot

def main():
    # Create robot instance
    robot = Robot(verbose=1)
    
    print("=== Cross-Platform Port Discovery Demo ===\n")
    
    # 1. List all available ports
    print("1. All available serial ports:")
    ports = Robot.list_available_ports()
    if ports:
        for port in ports:
            print(f"   - {port}")
    else:
        print("   No serial ports found")
    print()
    
    # 2. List ports with detailed information
    print("2. Detailed port information:")
    detailed_ports = Robot.list_ports_detailed()
    if detailed_ports:
        for device, description, hwid in detailed_ports:
            print(f"   Device: {device}")
            print(f"   Description: {description}")
            print(f"   Hardware ID: {hwid}")
            print()
    else:
        print("   No serial ports found")
    
    # 3. Find potential robot ports
    print("3. Potential robot/Arduino ports:")
    robot_ports = Robot.find_robot_ports()
    if robot_ports:
        for port_info in robot_ports:
            print(f"   Device: {port_info['device']}")
            print(f"   Description: {port_info['description']}")
            print(f"   Hardware ID: {port_info['hwid']}")
            print()
    else:
        print("   No potential robot ports found")
    
    # 4. Attempt auto-connection
    print("4. Attempting auto-connection to robot...")
    # Try to auto-connect by iterating candidate ports
    connected = False
    for info in robot_ports:
        device = info['device']
        try:
            # Windows: accept 'COM3' and also a number; Linux/Mac: path
            port_id = device[3:] if device.startswith('COM') else device
            robot.open(port_id)
            connected = True
            break
        except Exception as e:
            print(f"   Skipping {device}: {e}")

    if connected:
        print("✓ Successfully connected to robot!")
        # Test basic communication
        try:
            api_version = robot.sensors.get_api_version()
            print(f"   Robot API Version: {api_version}")
            # Example: turn on LED 0 briefly
            robot.leds.on(0)
            robot.leds.off(0)
        except Exception as e:
            print(f"   Communication test failed: {e}")
        finally:
            robot.close()
            print("   Connection closed")
    else:
        print("✗ Failed to auto-connect to robot")
    
    print("\n=== Manual Connection Example ===")
    
    # 5. Manual connection example
    if detailed_ports:
        first_port = detailed_ports[0][0]
        print(f"Trying manual connection to first available port: {first_port}")
        
        try:
            # For Windows COM ports, extract just the number
            if first_port.startswith('COM'):
                port_id = first_port[3:]  # Remove 'COM' prefix
            else:
                port_id = first_port  # Use full path for Linux/Mac
            
            robot.open(port_id)
            print("✓ Manual connection successful!")
            robot.close()
            print("   Connection closed")
            
        except Exception as e:
            print(f"✗ Manual connection failed: {e}")
    
    print("\nDemo completed!")

if __name__ == "__main__":
    main()