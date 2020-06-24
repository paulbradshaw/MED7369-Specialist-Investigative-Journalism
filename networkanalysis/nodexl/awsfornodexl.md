# Setting up a remote server for Excel (Nodexl) on AWS

*The instructions here are taken from [this video workshop](https://www.youtube.com/watch?v=zaanqYAxYJY&feature=youtu.be), and you can also [find similar instructions here](https://www.smrfoundation.org/2018/01/02/using-nodexl-in-the-cloud/).*

Sign up for a free account at https://aws.amazon.com/ - you will need to provide card details but no payment will be taken for the first year.

Once you're signed up, you'll be taken to the [Management Console](https://us-east-2.console.aws.amazon.com/console/home?region=us-east-2#).

In *Find Services* search for **EC2** and select it to start building an EC2 'resource'.

Click on **Running instances**

The list will be empty to begin with. Click **Launch instance**

Search for a Windows 'instance'. Make sure you select one which is labelled 'Free tier eligible'. At the time of writing we choose *Microsoft Windows Server 2019 Base*.

You will be presented with a list of options. Again, only one is labelled 'Free tier eligible': *t2.micro* (if you want to pay *m5a large* is recommended).

Select that free option *t2.micro* and click **Configure instance details**.

You'll be taken to *Step 3: Configure Instance Details*. Just click **Next** on this page.

In *Step 4: Add Storage* keep it at 30GB to avoid being charged (although you may be able to increase it slightly before charging kicks in). Click **Next**.

*Step 5: Add Tags*: Add a *Key* of **Name** and *Value* of **NODEXL**.

*Step 6: Configure Security Group* is an important step, as it allows remote desktop connections. Make sure *Create a new security group* is selected (unless you've already done this before) and click **Review and launch**.

You'll get a warning on the Step 7 page: *Improve your instances' security. Your security group, launch-wizard-1, is open to the world.*

That's fine - it has to be open so you can connect to it.

Click **Launch**.

You'll be asked to *Select an existing key pair or create a new key* in a new window. Click on the dropdown and select **Create a new key pair**.

You need to specify a name for the key: we can choose *NODEXL* (it's arbitrary).

Click **Download key pair**.

Make sure you keep the downloaded key in a safe and secure place.

Click **Launch instance**.

It will now start creating the instance. It will show you a link to that instance (with a name like *i-0e905411c2cd36e8f*). Click on that link to see the instance (and any others) in your [instances page](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances:sort=instanceId)

Creating the new instance will take a few minutes.

Once it's created, click the **Connect** button above the list (the instance should be selected by default).

A new window should appear: *Connect to your instance*.

Click on the button in the middle of that: **Download Remote Desktop File**.

This will download a file to your computer ending in `.rdp`. Keep that screen open because you'll need it.

To open that file you'll need to download the **Microsoft Remote Desktop client** [from the Mac App Store](https://apps.apple.com/us/app/microsoft-remote-desktop/id1295203466?mt=12).

Once you've got that installed, open it.

Then double-click on the RDP file you downloaded.

The app will be used to open the file and connect to the remote server.

Eventually you will be asked to log in. The username will be filled in as 'Administrator' but the password will need entering. Now to get that password...

Return to the page you had open, with *Download Remote Desktop File* on it. Below that button is one that says **Get Password**. Click this.

A password will be revealed. Copy this and paste it into the password box you needed to fill.

You should also keep a copy of this somewhere, so you don't have to repeat this process each time.

## Inside the remote server

The remote windows machine should now boot up in a new window. You will be looking at its desktop.

You need to download Chrome - to do this open Internet Explorer and **do not accept the default security settings** (choose the alternative: *Don't use recommended settings*).

*Note: If you forget to do this, then [follow the instructions here](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-windows-file-download-ie/) to undo that.*

Once you've downloaded Chrome and installed it, go to https://www.office.com/?auth=2 (you may need to log in with your student email address) and look for the **Install Office** button in the upper right corner. This takes some finding as they seem to want you to access the cloud version of the software.

When you click on that, wait for it to download, then double-click or open the .exe file to install Office.

Once that's installed, you need to install NodeXL too: you can [find a link to download NodeXL on the NodeXL gallery](https://www.nodexlgraphgallery.org/Pages/Registration.aspx).

When that's installed, double-click on the NodeXL shortcut added to the desktop to create a new project.

It will open Excel with a new spreadsheet using NodeXL. A few things to note:

* The spreadsheet itself will already be populated with some headings
* On the right there will be a *Document Actions* window that can be expanded to show options when viewing networks
* The menus at the top include a *NodeXL Pro* menu. This is worth having visible as it provides options such as importing data from Twitter, etc.

## Stopping the virtual machine

From https://www.smrfoundation.org/2018/01/02/using-nodexl-in-the-cloud/:
Virtual Machines can be started and stopped. A stopped machine is lost forever.  However, a running virtual machine machine can be saved in a snapshot to a file that can later be restored.

In the navigation pane, choose Instances, and select the instance. Choose Actions, select Instance State, and then choose Stop. If Stop is disabled, either the instance is already stopped or its root device is an instance store volume. In the confirmation dialog box, choose Yes, Stop. It can take a few minutes for the instance to stop.

To restart the stopped instance, select the instance, choose Actions, Instance State, Start. In the confirmation dialog box, choose Yes, Start. It can take a few minutes for the instance to enter the running state.

If you stop an EC2 instance no charges apply for the usage of the EC2, however some charges apply for the storage used by the file copy of the stopped EC2 instance.

You can find more information about Stopping and Starting AWS EC2 Virtual Machines here:

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html

## Teaching resources

See https://www.smrfoundation.org/nodexl/teaching-with-nodexl/teaching-resources/ for lots of sample data etc.
