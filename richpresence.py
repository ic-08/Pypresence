from pypresence import Presence
import time

client_id = '946962588183429190'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop



print("Client connected. Game has started...")
while True:  # The presence will stay on as long as the program is running
    day = time.time() - 1645845841
    day = day // 60 // 60 // 24
    RPC.update(state = f"Playing for {round(day)} day...", details="Studying Alone... (1 of 4)" , start = 1645845841, small_image = 'img.png', large_image = "crop_65465_", party_id= "ae488379-351d-4a4f-ad32-2b9b01c91657")  # Set the presence
    time.sleep(15)
