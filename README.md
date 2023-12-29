# Illawarra Line CATS Panel

Dispatcher Panel for [The Illawarra Line](https://illawarraline.net) HO Scale Model railroad.

## Requirements

- JMRI 5.4
- CATS 3.0

## File Structure

```bash
├── .jmri
│   ├── DispatcherPro_Tables.xml
│   ├── dispatcheroptions.xml
│   ├── dispatcher
│   │   └── traininfo
│   │       ├── Dispatch_Down_Train_From_Staging_Track_1.xml
│   │       ├── Dispatch_Down_Train_From_Staging_Track_2.xml
│   │       └── Dispatch_Up_Train_to_Staging_Track_1.xml
│   ├── masts.xml
│   └── resources
│       └── signals
│           └── cats-masts
│               ├── appearance-cats-virtual.xml
│               ├── aspects.xml
│               └── index.shtml
├── README.md
├── panel.xml

```

- .jmri: Supporting files to support the CATS-specific signal masts in JMRI, and DispatcherPro
- panel.xml: The CATS Panel XML file.
- DispatcherPro_Tables.xml:  the Blocks, Sections and Transits required for DispatcherPro
- /dispatcher/* : the templates to make dispatching trains easier.
- dispatcheroptions.xml: DispatcherPro Options file

## Install Guide

- Install specified CATS and JMRI Version, create a profile connecting to the MQTT Broker.
- Clone this repo
- Copy the contents of the .jmri folder to your JMRI profile folder - eg for mac: `/Users/<username>/Library/Preferences/JMRI/<ProfileName>.jmri/`
- configure your JMRI during start to load the following files:
  - DispatcherPro_Tables.xml
  - masts.xml
- start the panel with the cats script: `cats.csh /Path/To/Repo/panel.xml`
