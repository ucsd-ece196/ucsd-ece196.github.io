# PCB Design Guidelines
_Written by George Troulis_

## Workshop Slides

<iframe src="https://docs.google.com/presentation/d/1vvlrvJ8wAHZMyEDkiLNV__9mrOlkvEyQ8KUJIGJHEWo/embed" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## TL;DR Steps to make a PCB

### 1. Schematic

  * Place components on schematic
  * Wire components (wires and/or net labels)
  * Assign footprints to components
  * Annotate all components
  * Perform Electrical Check

### 2. PCB

  * Import components from schematic
  * Position components **and** mounting holes
  * Draw board cutout
  * Add dimensions (on Eco1.User layer)
  * Route component tracks
  * Place copper fills (GND and/or V+)
  * Place SilkScreen labels, name, version, and date
  * Perform Design Rule Check

### 3. Ordering PCB
  * Export Gerber files + Drill Files, and zip them all
  * Find manufacturer (JLCPCB or OSHPark are common)
  * Upload zipped gerbers
  * Tweak settings (change soldermask color, lead-free finish etc)
  * Ensure rendered PCB looks ok
  * Order it and wait!


## KiCad Shortcuts

### Schematic Editor

| Key Combo | Performed Action |
| :---:     | :---             |
|  A        | Place Component  |
|  E        | Edit Component Properties |
|  W        | Place Wire       |
|  R        | Rotate Component |
|  L        | Net Label        |

### PCB Editor

| Key Combo | Performed Action |
| :---:     | :---             |
|  X        | Place Track      |
|  D        | Move Track       |
|  U        | Select Entire Track |
|  R        | Rotate Component |
|  V        | Toggle Top/Bottom layer |
|  B        | Fill all Pours   |
|  Ctrl+B   | Unfill all Pours |

## Common KiCad Components

### Schematic Components

| KiCad Name | Component |
| :---:      | :---             |
|  R         | Resistor         |
|  C         | Capacitor        |
|  LED       | LED              |
|  SW_Push   | PushButton       |
|  Conn_01x?? | Pin Header (?? can be any number) |

<!--
### PCB Footprints

 | Component      | Footprints |
 | :---:          | :---:            |
 |  Resistor      | Resistor         |
 |  C             | Capacitor        |
 |  LED           | LED              |
 |  SW_Push       | PushButton       |
-->


## Helpful Tips

!!! note
    These are just guidelines, not required rules. Still, it is generally good practice to follow these

### 1. Make Traces As Thick As Possible

### 2. Use a GND or V+ Copper Pour

### 3. Add Plenty Of Silkscreen

Silcscreen is like notes on your PCB. Some useful things to include are:

1. Label Pins and Connectors; If you have Serial or I2C, label which pin is which
2. Add your name, date, and PCB version! You may make a second version of your PCB someday, who knows
3. Add a Logo perhaps. Not necessary, but always fun to do

## Homework (Check Slides/Gradescope for Due Date)

!!! Question
    **Flavor Text:** Everytime you need to use an LED with an Arduino,
    you have to connect it with a resistor, and the breadboard  circuit
    can get messy. Would be nice to just 'plug in an LED to a breadboard' and
    have it work with no other components.

    **Assignment:** Design a small PCB that has the following components:

    * LED
    * Resistor
    * 01x02 Pin Header

    **Deliverables:**

    * Screenshot of Schematic
    * Screenshot of PCB

    **Submission:** Submit this on Gradescope

    **Note:** Yes this is a very simple PCB. But it should be enough to give
    you some confidence in using a PCB design tool. Sometimes, very simple PCBs
    can be very useful.

