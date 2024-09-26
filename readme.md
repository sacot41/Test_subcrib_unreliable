# Test project for bug in Thingsboard Python SDK

Thingsboard Python SDK seem to have bug; subcription for device under a gateway is not reliable.

Step to reproduce : 
1. Connect to Thingsboard.cloud has a gateway with the TBGatewayMqttClient class.
2. Connect a device with the method "gw_connect_device".
3. Subscript to all attribute with method "gw_subscribe_to_all_device_attributes".
4. Test that we receive attribute update. This should work. 
4. Wait some time. Typically, it's under 5 minutes.
5. Test again attribute update. Callback defined in "gw_subscribe_to_all_device_attributes" will not receive any update.

I test it under python 3.7 and 3.11.

