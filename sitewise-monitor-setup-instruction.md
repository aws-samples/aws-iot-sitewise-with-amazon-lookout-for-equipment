                                  ## SiteWise Monitor Setup Instruction
## About

Follow the steps in this file to create your AWS IoT SiteWise Monitor portal so you can visualize device performance metrics and results of the machine learning inferences returned by Amazon Lookout for Equipment.

### Create the IoT SiteWise Monitor portal 

A portal is the web app that references IoT SiteWise assets and hosts dashboards. A portal must be created before you can start creating dashboards.

1.	Navigate to the AWS IoT SiteWise console
2.	Open the navigation pane by choosing the three bars in the upper left corner.
3.	In the navigation pane, choose Portals, and then Create portal.
4.	Under Portal name, enter a portal name of your choice.
5.	Under User authentication, choose IAM.
6.	Under Email, enter a valid email address where you have access to.
7.	Under Permissions, choose Create and use a new service role.
8.	Choose Next.
9.	Under Alarms, deselect Enable alarms.
10.	Under Edge Configuration, deselect Enable this portal at the edge.
11.	Choose Create.
12.	Under Invite administrators, under Users or Roles, choose the user or role you are using, and then choose Next.
13.	Under Assign users, do not choose any user or role, choose Assign users.
14.	Under Portals you should find the portal with the name of your choice.
15.	To access your Monitor portal, choose the link which starts with https:// located right from your portal name.

### Browse the asset library 

By browsing the asset library you can get a first impression about the visualizations for your data.

### In your Monitor portal

1.	Choose Assets.
2.	Under Assets, expand Demo Pump Station Asset, there are two child assets: Demo Pump Asset 1 and Demo Pump Asset 2.
3.	Under Demo Pump Asset 1 in the right pane you should see the measurements and metrics that you have defined in the pump asset model.
4.	Feel free to browse around

### Create a project 

To build dashboards later first you need to create a project.

1.	Projects
2.	Create project
3.	Project name: Replace with a project name of your choice
4.	Project description: Replace with your project description
5.	Create project

### Add project assets 

Each project contains assets based. Based on these assets you can create dashboards to visualize your data.

1.	Project assets
2.	Go to asset library
3.	Select Demo Pump Station Asset
4.	Add asset to project
5.	Check: Select existing project
6.	Select an existing project you created in the previous section
7.	Add asset to project
