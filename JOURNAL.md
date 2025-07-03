---
title: "Yet Another Metronome by Sreekar"
author: "Sreekar Ramisetty"
description: "Metronome with rotary encoder and OLED display"
created_at: "2024-06-04"
---
## June 4th, 2025, 6:32 PM<br>
I have a vision for where I want to take this project, but since I have finals tomorrow i'll just get a basic schematic whipped up (i have no idea what i'm doing)<br>
**literally like 30 seconds spent 😭**

## June 9th, 2025, 3:17 PM<br>
I did not in fact get anything done but finals are over so i can probably actually get started today<br>
hear me out tabletop flat design cause i'm scared of 90°, plate for mx switches and an oled cause i'm overconfident, but first let's get a basic pcb done<br>
wait no hear me out: rotary encoder. to encode your rotary movement. amirite amirite?<br>
**1 hour spent**

## June 12th, 2025, 9:01 PM<br>
ok time to wire up the oled and rotary encoder<br>
zawg how do i power ts<br>
ohhhh now i know the difference between vsys, vbus, and 3v3<br>
it's all wired in the schematic :yay:<br>
now time to find a speaker that's loud and preferably not expensive (good cheap fast ahh)<br>
oops i had the times i spent written in obsidian but not here better add those in<br>
alr i got a somewhat coherent schematic together i'm going to sleep now<BR>
**2 hours spent**<Br>
![image](https://github.com/user-attachments/assets/2f0a98d8-5abc-4798-82a3-cdeb3fe6c601)

## June 13th, 2025 12:04 PM<br>
if you're reading the actual markdown for some reason i must apologize for the way i format this<br>
so i want to put an led on here for visual feedback<br>
i could use just a single led or i could use a neopixel :wow:<br>
i think for the led i could just give it power every x ms and put a resistor in front of it<br>
after further research, i've decided to just use a single neopixel<br>
time to go back to the schematic<br>
**1 hour spent 😭**<Br>
![image](https://github.com/user-attachments/assets/9e1ceb6b-07de-433f-a93d-45f6c441fbab)


## June 15th, 2025 4:30 PM<br>
i guess it's time to pcb all over the place<br>
nvm my schematic has issues<br>
so i guess it's better to power oled with 3v3<br>
and my neopicel wasn't connected to anything somehow<br>
also i guess the buzzer should also use 3v3, honestly the buzzer is what i'm most worried about<br>
schematic should be finished now, it looks so tuff<br>

oh i guess the pins for the buzzer symbol don't match the ones on the footprint, i guess i should just reassign them<br>
**2 hours spent**

## June 18th, 2025 1:12 PM<br>
i fixed the buzzer and made a basic outline of how i want it on paper and on the pcb<Br>
![alt text](imgs/pcb_v1.png)<Br>
![alt text](imgs/epicsketch.png)<br>
**1 hour spent**

## June 22nd, 6:32 PM<Br>
got pcb outline finished and wired
![alt text](imgs/pcb_v2_maybe_idk.png)
**1 hour spent**

## June 29th, 7:30 PM<br>
ok i should run git push i've been editing ts locally this whole time 😭<br>
anyway i'm locking in now to make the case<br>
okay i think it'll be more stable if i make a round cutout for the rotary encoder instead of just having it completely exposed<br>
and i should also have a square border that is actually connected to the "plate" to give it some more stability<br>
![alt text](imgs/case_v2.png)<br>
wait i was going to sandwich mount it like a keyboard but i don't have mx switches, just a rotary encoder<br>
how do i mount ts 😭<br>
**3 hours spent**

## June 30th, 2:34 PM<br>
i thought about it and i looked at the mounting styles website and i think if i make a kind of tray mount style case it'll be fine<br>
![alt text](imgs/tray_mount.jpg)
so in my case the "plate" doesn't hold up the pcb in any way, it's just to cover and protect the pcb, so i'll have a couple more posts in the corners to hold it up, and probably something under the encoder to give it stability<br>
i made some slight adjustments to the pcb to give the screw a bit of clearance<br>
![alt text](imgs/pcb_v3.png)<br>
ok i'll just edit my sketch and go to sleep
**2 hours spent**

## July 1st, 3:22 PM<br>
i want to get ts finished today, luckily it's just continuing manual labor from yesterday  
okay i got the case put together  
![alt text](imgs/case_maybefinal.png)  
so this is in two pieces, the bottom case and a top covering.  
![alt extxusdcgfsihguofijdhsu](imgs/yams_real_2025-Jul-02_06-19-33PM-000_CustomizedView9141615810.png)  
there's a hole for the rotary encoder, and another hole on the side for power delivery to the xiao  
the pcb is held up with supports at the bottom of the case. there's a "post" in each corner, plus one directly under the rotary   encoder and one approximately in the middle to screw into.  
![alt text](imgs/posts.png)  
agh i forgot firmware see you tomorrow  
**2 hours spent**

## July 2st, 1:10 PM<br>
okay firmware should be pretty simple. i think i can even get away with using qmk cause that's what i'm familiar with  
ok so i am definitely not using qmk  
after much research and docs reading, i think i got a probably working firmware:  
![i aint reading allat](imgs/fw.png)  
you change the bpm with the rotary encoder, and push on it to turn off the metronome  
when a beat happens, the piezo buzzer chirps and the neopixel flashes  
yeah that's pretty much it :heavysob:  
thanks for reading make sure to like and subscribe  
**3 hours spent**