# misc/audio-frequency-stego
### wooshi

## Description
What a mundane song, it's just the same note repeated over and over. But could there perhaps be two different notes?
### Downloads
[audio_frequency_stego.wav](Assets\audio-frequency-stego\audio_frequency_stego.wav)

## Solution
We open the file in Sonic Visualizer and view Peak Frequency Spectrogram<br/>
We see that there are 2 possible values, and they are divided into equal sections<br/><br/>
<img src="Assets\audio-frequency-stego\audio-frequency-stego-screencap.PNG" width="60%" height="60%"><br/><br/>
Thus, we can infer it is binary encoded<br/>
We transcribe it to get: `011001100110110001100001011001110111101101110011011011000011000101100111011010000101111101110000001100010111010001100011011010000101111101100011011010000011010001101110011001110011001101111101`<br/>
Decoding it, we get the flag



> flag{sl1gh_p1tch_ch4ng3}