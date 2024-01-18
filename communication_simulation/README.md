# Communication Simulation

![Communication Simulation](https://i.ibb.co/q5Tq8h9/Screenshot-from-2024-01-18-10-42-15.png)

## Overview

The Communication Simulation project is designed to explore MQTT communication and test its capabilities before integration with ROS (Robot Operating System). This Python application comprises two main components:

- **publisher.py:** This serves as the client code, intended to run on the vehicle. It generates and sends random speed values to a specified topic for testing purposes.

- **subscriber.py:** This Python script is meant to run on the listener (referred to as the CMS in the accompanying figure). It subscribes to a specified topic, acting as a testbed for receiving and processing messages.

## Usage

To run the simulation, follow these steps:

1. **Rename .env.example to .env:** Fill in the MQTT broker credentials details in the `.env` file.

2. **Install Required Packages:** Execute the following command in your terminal to install the necessary packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Publisher:**
    - Execute the following command in the terminal:
      ```bash
      python3 publisher.py
      ```
    - Provide the requested inputs when prompted for client ID and topic. For example, use "av1" as the client ID and "av/updates/av1" as the topic.

4. **Run the Subscriber:**
    - Open another terminal window and execute the following command:
      ```bash
      python3 subscriber.py
      ```
    - Provide any desired client ID and subscribe to a wildcard topic. For instance, use "av/updates/#" as an example wildcard topic.

## Important Notes

- Ensure that the MQTT broker credentials are correctly configured in the `.env` file.
- The publisher and subscriber scripts provide a straightforward way to test MQTT communication in a simulated environment.
