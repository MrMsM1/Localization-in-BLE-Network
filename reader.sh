#!/bin/bash

# MQTT broker details
broker_address="192.168.235.221"
port=1883
topic="/topic"

# File to save messages
file_path="data.txt"

# Subscribe to MQTT topic and save messages to file
mosquitto_sub -h "$broker_address" -p "$port" -t "$topic" | while IFS= read -r message; do
    echo "$message" >> "$file_path"
    echo "$message" >> "$file_path"
    echo "Message received: $message"
    #echo >> "$file_path"  # Add a newline to separate messages in the file
done
