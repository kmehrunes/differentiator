# Differentiator

**This is an Afternoon Project -quick small projects that make life a bit easier-**

A simple Python script which generates or read a recursive directory diff file and creates a diff directory where each file gets its own diff file in the same relative path as its original file.

## Example

To generate both the directories diff file and a diff file for each file in unified format:
> *python differentiator.py diff u ~/original/ns-3.26/src/ ~/modified/ns-3.26/src/ ~/diffs/ unified.diff*

To view the output directory
> *tree ~/diffs/*


    |
    ├── core
    │   └── model
    │       ├── assert.h.diff 
    │       ├── default-simulator-impl.cc.diff
    │       └── simulator.cc.diff
    ├── fd-net-device
    │   ├── examples
    │   │   └── fd-emu-ping.cc.diff
    │   ├── helper
    │   │   ├── emu-fd-router-device-helper.cc.diff
    │   │   ├── emu-fd-router-device-helper.h.diff
    │   │   ├── fd-router-device-helper.cc.diff
    │   │   ├── fd-router-device-helper.h.diff
    │   │   └── raw-sock-creator.cc.diff
    │   ├── model
    │   │   ├── checksum.cc.diff
    │   │   ├── checksum.h.diff
    │   │   ├── fd-net-device.cc.diff
    │   └── wscript.diff
    ├── flow-monitor
    │   ├── helper
    │   │   └── flow-monitor-helper.cc.diff
    │   └── model
    │       ├── flow-classifier.h.diff
    │       ├── ipv4-flow-classifier.cc.diff
    │       ├── ipv4-flow-classifier.h.diff
    │       ├── ipv6-flow-classifier.cc.diff
    │       └── ipv6-flow-classifier.h.diff
    ├── internet
    │   ├── helper
    │   │   ├── ipv4-address-helper.cc.diff
    │   │   └── ipv4-address-helper.h.diff
    │   ├── model
    │   │   ├── arp-l3-protocol.cc.diff
    │   │   ├── arp-l3-protocol.h.diff
    │   │   ├── global-router-interface.cc.diff
    │   │   ├── ipv4-header.cc.diff
    │   │   ├── ipv4-header.h.diff
    │   │   ├── ipv4-interface.cc.diff
    │   │   ├── ipv4-l3-protocol.cc.diff
    │   │   ├── ipv4-l3-protocol.h.diff
    │   │   ├── ipv4-routing-table-entry.cc.diff
    │   │   ├── ipv4-routing-table-entry.h.diff
    │   │   ├── ipv4-static-routing.cc.diff
    │   │   ├── ipv4-static-routing.h.diff
    │   │   ├── ipv6-l3-protocol.cc.diff
    │   │   ├── ipv6-l3-protocol.h.diff
    │   │   ├── tcp-header.cc.diff
    │   │   ├── tcp-header.h.diff
    │   │   ├── tcp-option-rfc793.cc.diff
    │   │   ├── udp-header.cc.diff
    │   │   └── udp-header.h.diff
    │   └── wscript.diff
    ├── lte
    │   ├── helper
    │   │   ├── lte-helper.h.diff
    │   │   ├── point-to-point-epc-helper.cc.diff
    │   │   └── point-to-point-epc-helper.h.diff
    │   ├── model
    │   │   ├── epc-enb-application.cc.diff
    │   │   ├── epc-enb-application.h.diff
    │   │   ├── epc-tft-classifier.cc.diff
    │   │   ├── epc-ue-nas.cc.diff
    │   │   ├── lte-common.h.diff
    │   │   ├── lte-enb-mac.cc.diff
    │   │   ├── lte-enb-net-device.cc.diff
    │   │   ├── lte-enb-net-device.h.diff
    │   │   ├── lte-enb-phy.cc.diff
    │   │   ├── lte-net-device.cc.diff
    │   │   ├── lte-net-device.h.diff
    │   │   ├── lte-phy.cc.diff
    │   │   ├── lte-rlc-um.cc.diff
    │   │   ├── lte-ue-mac.cc.diff
    │   │   ├── lte-ue-net-device.cc.diff
    │   │   ├── lte-ue-net-device.h.diff
    │   │   ├── lte-ue-phy.cc.diff
    │   │   ├── lte-ue-rrc.cc.diff
    │   │   └── lte-ue-rrc.h.diff
    │   └── test
    │       ├── lte-test-entities.cc.diff
    │       └── lte-test-entities.h.diff
    ├── network
    │   ├── model
    │   │   ├── buffer.cc.diff
    │   │   ├── net-device.cc.diff
    │   │   ├── net-device.h.diff
    │   │   ├── node.cc.diff
    │   │   └── node.h.diff
    │   ├── test
    │   │   └── error-model-test-suite.cc.diff
    │   └── utils
    │       ├── packet-socket.cc.diff
    │       └── packet-socket.h.diff
    ├── point-to-point
    │   └── model
    │       ├── point-to-point-net-device.cc.diff
    │       └── point-to-point-net-device.h.diff
    ├── tap-bridge
    │   └── model
    │       ├── tap-bridge.cc.diff
    │       └── tap-bridge.h.diff
    ├── traffic-control
    │   └── model
    │       ├── traffic-control-layer.cc.diff
    │       └── traffic-control-layer.h.diff
    ├── unified.diff [The file generated by 'diff']
    ├── wave
    │   ├── examples
    │   │   └── wave-simple-device.cc.diff
    │   ├── model
    │   │   ├── vendor-specific-action.cc.diff
    │   │   ├── vendor-specific-action.h.diff
    │   │   ├── vsa-manager.cc.diff
    │   │   ├── vsa-manager.h.diff
    │   │   └── wave-net-device.h.diff
    │   └── test
    │       └── mac-extension-test-suite.cc.diff
    └── wifi
        └── model
            ├── ap-wifi-mac.cc.diff
            ├── block-ack-manager.cc.diff
            ├── mac-low.cc.diff
            ├── sta-wifi-mac.cc.diff
            ├── wifi-net-device.cc.diff
            ├── wifi-net-device.h.diff
            ├── wifi-phy.cc.diff
            ├── wifi-phy-state-helper.cc.diff
            ├── yans-wifi-phy.cc.diff
            └── yans-wifi-phy.h.diff
