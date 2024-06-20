import objc
from Foundation import *
from IOKit import IOService
from IOKit.usb import kIOUSBDeviceClassName

def find_usb_location_id(vendor_id, product_id):
    # Set up a matching dictionary
    matching_dict = IOService.IOServiceMatching(kIOUSBDeviceClassName)
    IOService.CFDictionarySetValue(
        matching_dict,
        "idVendor",
        objc._C_UINT(vendor_id)
    )
    IOService.CFDictionarySetValue(
        matching_dict,
        "idProduct",
        objc._C_UINT(product_id)
    )

    # Find the first matching service
    service = IOService.IOServiceGetMatchingService(kIOMasterPortDefault, matching_dict)
    if service:
        # Get the locationID
        location_id = IOService.IORegistryEntryGetProperty(service, "locationID", None)
        IOService.IOObjectRelease(service)
        return location_id
    else:
        print("No matching USB device found.")
        return None

# 示例使用
vendor_id = 0x05ac  # 替换为实际的 Vendor ID
product_id = 0x828f  # 替换为实际的 Product ID
location_id = find_usb_location_id(vendor_id, product_id)
print(f"Location ID: {location_id}")
