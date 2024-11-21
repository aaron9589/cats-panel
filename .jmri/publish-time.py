import jmri
import java

# Script to Publish the Internal fast clock to an MQTT topic.

# Define the MQTT topic and Memory variable
mqtt_topic = "jmri/memory/currentTime"
memory_variable_name = "IMCURRENTTIME"

try:
    # Get the Memory variable
    memory = jmri.InstanceManager.memoryManagerInstance().getMemory(memory_variable_name)

    if memory is None:
        raise ValueError("Memory variable '" + memory_variable_name + "' not found.")

    # Get the MQTT Adapter
    mqttAdapter = jmri.InstanceManager.getDefault(jmri.jmrix.mqtt.MqttSystemConnectionMemo).getMqttAdapter()

    if mqttAdapter is None:
        raise ValueError("MQTT Adapter is not configured. Check your JMRI MQTT setup.")

    # Listener to monitor changes to the Memory variable
    class MemoryChangeListener(java.beans.PropertyChangeListener):
        def __init__(self, memory, mqttAdapter, topic):
            self.memory = memory
            self.mqttAdapter = mqttAdapter
            self.topic = topic

        def propertyChange(self, event):
            new_value = self.memory.getValue()
            if new_value is not None:
                self.mqttAdapter.publish(self.topic, str(new_value).encode('utf-8'))
                print("Published '" + str(new_value) + "' to MQTT topic '" + self.topic + "'")
            else:
                print("Memory value is None, skipping publish.")

    # Attach the listener to the Memory variable
    listener = MemoryChangeListener(memory, mqttAdapter, mqtt_topic)
    memory.addPropertyChangeListener(listener)

    # Initial publish
    initial_value = memory.getValue()
    if initial_value is not None:
        mqttAdapter.publish(mqtt_topic, str(initial_value).encode('utf-8'))
        print("Initial publish: '" + str(initial_value) + "' to MQTT topic '" + mqtt_topic + "'")
    else:
        print("Initial Memory value is None, no publish.")

    print("Script initialized, listener attached.")

except Exception as e:
    print("Error: " + str(e))
