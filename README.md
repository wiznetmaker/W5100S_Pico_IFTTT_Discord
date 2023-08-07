# W5100S_Pico_IFTTT_Discord

Hello! Are you having a good day!


Today, I made a project with an interesting theme. It's a very simple and fun project.

I have five friends. They love playing games. I enjoy playing games after work with these friends every day

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/ca458a9f-217f-4084-b0c3-704bcb3bad03)

Do you happen to know a game called LOL? This game, called League of Legends, is difficult to play unless five people gather. So I have to let you know if I can play tonight or not. If I don't tell them, my crazy friends won't stay still.

However, I am very lazy to chat. It's especially annoying to do it during work hours. It's not a big deal, but I'm sure there are people who sympathize.

So I decided to make a device that can simply tell you my status with a button. I'm sure I'll press the button at least once..

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/30d24eeb-0b8e-4fc2-9c3b-ac43c79d62a2)

I made a simple button. Pull-up 3.3V.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/faadff2e-7b08-486f-8911-bd4e7aa735fc)

It connects to the Pico board. I finished it with silicon to secure it.And the Pico board is connected to the W5100S board. This is the best way to use Ethernet.

## IFTTT

I must now create an action progression through IFTTT.

https://ifttt.com/explore

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/3de96494-8820-406f-8222-7b79acff861c)

IFTTT connects applications that we commonly use.

After signing up, you can create an applets.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/fc9cff60-ff48-4229-992c-9883dc0b81c7)

Click "IF Then" first.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/1255daf6-9430-4639-8948-45a35af6a387)

Select "Webhooks".

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/479b3fa7-22f6-4000-83a5-8524ebbdd6d7)

Select "Receive a web request" because it is not sent to Json.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/36fe3ba0-d7f7-4772-92a8-71e3dbadb600)

Enter the applets name you want.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/e5f53d03-064f-49d3-a1bf-4116727656ca)

When you're done, then it's "Then That". Select an action.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/89225044-3857-4158-88d4-2954588574eb)

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/ffa38c49-a236-4c91-9cb0-2ff800a8cc79)

I can select Discord to select the activities.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/0cbb2242-b2fb-4aba-965c-f5b7ee5e9616)

After connecting to the discord, enter the desired channel. You can also format messages.

IFTTT is complete.


## Firmware

First, you need to update the Pico to the WIZnet 5K version. This exclusive FW was carried out by referring to Virtor's project.

https://maker.wiznet.io/viktor/projects/how-to-connect-raspberry-pi-pico-to-twitter-using-ethernet-hat-and-ifttt/

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/f658d976-403b-4307-b0c5-6108808fc647)

Now, next.

I proceeded with micro python. H, Similarly, the dedicated FW provided by Victor is also a micro-Python version.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/a02d2791-f595-4390-9c37-393d7781a0f6)

I imported the libraries to use.. In addition, set the 5 connected buttons to pull-up.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/7b579a96-2f49-4bc2-b12c-a3ecf572f6b7)

And it starts the W5x00 chip.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/abff6820-38c5-43cc-b3e3-e1d4384fa194)

Creates a message to send when the button is pressed.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/8734d4db-9bf7-4ae4-b280-325cd9b8cd24)

The message that will be sent according to the button is set like this.

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/e4de09bd-d788-46f5-b8ca-9b88bb0b5b72)

And if you pass the message to that code, you're done. For "your_key", enter the key of apps issued by IFTTT!

## Operating

![image](https://github.com/wiznetmaker/W5100S_Pico_IFTTT_Discord/assets/111826791/f1aa143c-42f5-488c-8612-a5505d1bf998)

It works very well! Now I can communicate my situation well without having to chat directly!

https://youtube.com/shorts/q9OgWt0Xajg?feature=share


