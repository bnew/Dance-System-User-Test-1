# User Test 1: Quick & Dirty Thesis Show

<img src="/doc/usertest.png" alt="Score for User Test"/>

### Dependencies:
- TouchDesigner & Ableton with [TDAbleton](https://docs.derivative.ca/TDAbleton) set up. 
- Maschine for midi to use 'midi voice control' component. Otherwise, simply remove the component and use the 'voice controllers' component directly.

### track controller
A track controller controls one track inside of ableton. The 'digits' in the component's name corresponds to its track number in ableton. This allows the selected track to persist across sessions.
<img src="/doc/trackcontroller.png" alt="screenshot of track controller custom parameters">

- What is the volume level for ‘off’ and on? This allows users to feel their presence impacting the voice when entering the space.
- Does it control a ‘rack’ device? This allows it to control parameters on instruments and effects. 
	- If so, how many parameters (macros) does it control?
- Does it control clips by switching between them? This allows musical patterns to be changed by the ‘dance amount’

For clip control of a group track, the clips can be overrode with a table input as seen for the drum track.

### midi voice control
Takes in buttons and sliders from my midi controller and breaks it up to send to their respective voices

### voice controller / visual feedback
Has all voice controller buttons + sliders. The buttons and sliders can be controlled by inputs (ie midi) or can be used directly. 
<img src="/doc/voicecontrollers.png" alt="screenshot of voice controllers">


### collective voice
With 2 or 4 voice controllers connected to this component, the 'collective voice  controller' looks for a single voice to be present for it be activated. It's dance amount is binary, and is 1 when the average of all voices connected are at 90% dance amount. Currently this collective voice controls the drum track.


### ableton
In order for a composition in ableton to be controllable. It needs a few things.

- TDAbleton needs a master component on the master track in ableton
- Any track that has rack components must have them encapsulated in a TDInstrument component
- Each controllable rack element has its own macro and range mappings inside of ableton
- Any clip that is longer than 1/2 a bar and will be switched between needs the ‘Legato’ setting enabled in the clip launching preferences
- Any 'mixing' is best done with utility plug ins on the end of a track so as not to interfere with the 'presence' control
- All values 

### demo
[watch a demo here](https://vimeo.com/328255247)


### bugs
Sometimes macro controls do not match the amount listed in the track_controller. To fix this at the moment, just change the value once and it will be reconnect properly.


### todo
- Make components with dance amount and presence inputs not order dependent but name dependent instead.
- Allow for macros to be 'curved' so they can change their value at different rates.
- Hot switching of 2 and 4 voices.