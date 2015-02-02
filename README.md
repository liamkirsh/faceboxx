# faceboxx
Faceboxx is an open source tool that uses Facebook Messaging as a cloud storage service. It currently serves as a proof of concept and uses a Facebook account that was created to test the script, and is set to break the file into 10MB chunks as per the constant specified in chunk.py.

To run, execute gui.py and enter a username and password when prompted. Then select the "browse" button to select a file on your computer that is greater than 10MB large. Make sure that Firefox is installed in the default location on your system and that you have a working Internet connection.

Currently, the encrypted zip function uses the pyminizip library, which only works on Linux (https://github.com/smihica/pyminizip/issues/3). A version that works with the 7zip commandline interface is in the works.
