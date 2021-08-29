## Instruction to Create the SiteWise dashboard to visualize SiteWise data flow in blog step 1

1. Select "Create dashboard".
2. Expand "Demo Pump Station Asset" under "Asset" on the right panel.
3. Click "Demo Pump Asset 1", you should be able to see all asset properties associated with this asset.
![alt text](https://github.com/aws-samples/aws-iot-sitewise-with-amazon-lookout-for-equipment/blob/main/imag/fig1.JPG?raw=true)
4. Drag Sensor 0-5 properties from Demo Pump Asset 1 to the left, and sensor values should be shown with Line plot. If SiteWise simulator is successfully setup, the sensor value should be shown as data continuously ingested over time.
5. Produce similar visuals for the rest of sensors in Demo Pump Asset 1.
6. Edit the name of widget as: Sensor 0-5.

7. Create the same visualization for Demo Pump Asset 2. 

8. Finally, replace the default dashboard name New dashboard with something meaningful, e.g. DemoPumpStation. Click on Save dashboard to save your dashboard.
![alt text](https://github.com/aws-samples/aws-iot-sitewise-with-amazon-lookout-for-equipment/blob/main/imag/sitewisemonitor1.JPG?raw=true)
## Instruction to Create the SiteWise dashboard to visualize Amazon Lookout for Equipment output in blog step 4
## Demo Pump Alarm
1. Three SiteWise alarms (“l4E Alarm (Demo Pump Asset 1)”, “l4E Alarm (Demo Pump Asset 2)” and “StationAbnormalyAlarm (Demo Pump Station Asset)”) are dragged from the right pane to the dashboard;
2. Choose Grid widget for this visual;
3. Change widget name as “Demo Pump Alarms”.
4. Change this dashboard name to "Demo Pump Station", because the original dashboard is augmented in this step to show asset management for all assets within AWS IoT SiteWise. 
![alt text](https://github.com/aws-samples/aws-iot-sitewise-with-amazon-lookout-for-equipment/blob/main/imag/sitewisemonitor_dashboard.JPG?raw=true)
## SensorX L4EScore visual
1. “Sensor0 L4EScore”, “Sensor6 L4EScore”, “Sensor12 L4EScore”, “Sensor18 L4EScore”, “Sensor24 L4EScore” are dragged from the right pane to the dashboard;
2. Choose Grid widget for this visual;
3. Setup a threshold on this visual, so high “Sensor6 L4EScore” can be shown as red color for warning.
4. Change widget name as “SensorX L4EScore”.
![alt text](https://github.com/aws-samples/aws-iot-sitewise-with-amazon-lookout-for-equipment/blob/main/imag/sensorX%20L4Escore.JPG?raw=true)

## Impeller Component L4EScore visual
1. “Sensor6 L4EScore”, “Sensor7 L4EScore”, “Sensor8 L4EScore”, “Sensor9 L4EScore”, “Sensor10 L4EScore” and “Sensor11 L4EScore” are dragged from the right pane to the dashboard;
2. Choose Bar widget for this visual;
3. Change widget name as “Impeller Component L4EScore”;
4. Adjust the time range on the top right of the dashboard, to zoom in this visual and evaluate sensor L4EScore diagnoized by Lookout for Equipement within 5 minutes interval.

![alt text](https://github.com/aws-samples/aws-iot-sitewise-with-amazon-lookout-for-equipment/blob/main/imag/impeller_l4e.JPG?raw=true)